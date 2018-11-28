#include<iostream>
#include<string>
#include<cstring>
using namespace std;

typedef long long ll;

int N;
ll K, R;
ll cumcost[1024];
int seat[1024];
int cumstep[1024];

int main() {
	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> R >> K >> N;
		for(int i = 0; i < N; ++i) {
			cin >> seat[i];
			cumcost[i] = -1;
			cumstep[i] = 0;
		}
		ll cost = 0;
		int at = 0;
		int step = 0;
		while(cumcost[at] == -1 && R > 0) {
			cumcost[at] = cost;
			cumstep[at] = step;
			int i = 0;
			ll k = 0;
			while(i < N && k + seat[(i+at)%N] <= K) {
				k += seat[(i+at)%N];
				i++;
			}
			cost += k;
			at = (i+at)%N;
			--R;
			++step;
		}
		ll diffstep = step - cumstep[at];
		ll diffcost = cost - cumcost[at];
		if(R == 0) goto here;
		cost += (R / diffstep) * diffcost;
		R %= diffstep;
		while(R > 0) {
			int i = 0;
			ll k = 0;
			while(i < N && k + seat[(i+at)%N] <= K) {
				k += seat[(i+at)%N];
				i++;
			}
			cost += k;
			at = (i+at)%N;
			--R;
		}
here:
		cout << "Case #" << tt << ": " << cost << endl;
	}
	return 0;
}
