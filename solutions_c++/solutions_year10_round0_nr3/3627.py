#include <iostream>
#include <queue>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		int R, k, N; //per day, capacity, groups;
		cin >> R >> k >> N;
		queue<int> que;
		for(int j = 0; j < N; j++) {
			int g;
			cin >> g;
			que.push(g);
		}
		int euros = 0;
		while(R-- > 0) {
		//	cerr << "R = " << R << ", ";
			int taken = 0;
			int n = 0;
			while(taken + que.front() <= k && n < N) {
				int g = que.front();
				//cerr << "g = " << g << ", ";
				taken += g;
				//cerr << "taken = " << taken << ", ";
				que.pop();
				que.push(g);
				n++;
			}
			euros += taken;
			//cerr << "EUROS = " << euros << ", ";
		}
		//cerr << endl;
		cout << "Case #" << i << ": " << euros << endl;
	}
	return 0;
}