#include <iostream>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		int R, k, N;
		cin >> R >> k >> N;
		int queue[N];
		for(int j = 0; j < N; j++) {
			cin >> queue[j];
		}
		int money = 0;
		int cursor = 0;
		for(int j = 0; j < R; j++) {
			int avail = k;
			for(int itrs = 0; itrs < N; itrs++) {
				if(avail < queue[cursor]) break;
				avail -= queue[cursor];
				money += queue[cursor];
				cursor++;
				if(cursor >= N) cursor = 0;
			}
		}
		cout << "Case #" << i+1 << ": " << money << endl;
	}
}
