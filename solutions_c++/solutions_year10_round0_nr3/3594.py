#include <iostream>
#include <deque>

using namespace std;

/* r			roller coaster run r times a day
 * k			roller coaster capacity
 * queue		list of group sizes */
long income(int r, int k, deque<int> &queue) {
	deque<int> passengers;
	long euros = 0;
	int current = 0;
	int group;
	
	for (int i=0; i<r; i++) {
		current = 0;
		while (!queue.empty() && (group=queue.front())+current <= k) {
			current += group;
			queue.pop_front();
			passengers.push_back(group);
		}
		euros += current;
		/* Move passengers back to queue */
		while (!passengers.empty()) {
			queue.push_back(passengers.front());
			passengers.pop_front();
		}
	}
	
	return euros;
}

int main(int argc, char *argv[]) {
	deque<int> queue;
	
	int num, r, k, groupnum, group;
	
	cin >> num;
	
	for (int i=1; i<num+1; i++) {
		cin >> r >> k >> groupnum;
		queue.clear();
		for (int j=0; j<groupnum; j++) {
			cin >> group;
			queue.push_back(group);
		}
		cout << "Case #" << i << ": " << income(r, k, queue) << endl;
	}
	return 0;
}
