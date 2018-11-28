#include <cstdio>
#include <cstdlib>
#include <queue>
#include <iostream>
using namespace std;

int t, na, nb;

int train_count[2]; // train_count[0/1] - how many trains we have at A/B.
int res[2]; // res[0/1] - how many trains will start from stop A/B.

enum ActionType {
	ACTION_TRAIN_LEAVES,	
	ACTION_TRAIN_CAN_GO,
};

struct TAction {
	int t, t2;
	int stop;
	ActionType type;

	bool operator<(const TAction& other) const {
		if(t != other.t) return t > other.t;
		else return t2 > other.t2;		
	}
};

priority_queue<TAction> heap;

void init() {
	TAction action;
	int t1, t2;

	while(!heap.empty()) heap.pop(); // Clear the priority queue.

	cin >> t;
	cin >> na >> nb;
	for(int i=0; i<na; ++i) {
		action.type = ACTION_TRAIN_LEAVES;

		scanf("%d:%d", &t1, &t2);		
		action.t = t1 * 100 + t2;

		scanf("%d:%d", &t1, &t2);		
		action.t2 = t1 * 100 + t2;

		action.stop = 0; // Stop A.

		heap.push(action);
	}

	for(int i=0; i<nb; ++i) {
		action.type = ACTION_TRAIN_LEAVES;

		scanf("%d:%d", &t1, &t2);		
		action.t = t1 * 100 + t2;

		scanf("%d:%d", &t1, &t2);		
		action.t2 = t1 * 100 + t2;

		action.stop = 1; // Stop B.

		heap.push(action);
	}
	
	train_count[0] = train_count[1] = 0;
	res[0] = res[1] = 0;
}

void solve() {
	TAction action;

	while(!heap.empty()) {
		action = heap.top();
		heap.pop();

		int stop = action.stop;

		if(action.type == ACTION_TRAIN_LEAVES) {	
			int mins = action.t2 % 100;
			int hours = action.t2 / 100;

			if(mins + t < 60) mins += t;
			else {
				hours += 1;
				mins = t + mins - 60;
			}

			int new_time = 100 * hours + mins;

			if(train_count[stop] > 0) {				
				TAction new_action = {new_time, -1, !stop, ACTION_TRAIN_CAN_GO};
				heap.push(new_action);
				train_count[stop]--;
			}
			else {
				res[stop]++; // We need another bus to start from this station.

				TAction new_action = {new_time, -1, !stop, ACTION_TRAIN_CAN_GO};
				heap.push(new_action);				
			}
		}
		else {
			train_count[stop]++;
		}
	}
}

int main(void) {
	int n;

	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	cin >> n;
	for(int i=1; i<=n; ++i) {
		init();
		solve();
		cout << "Case #" << i << ": " << res[0] << " " << res[1] << endl;
	}
	return 0;
}
