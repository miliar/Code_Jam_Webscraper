#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> queue (N);
		for (int i = 0; i < N; ++i) cin >> queue[i];
		int index = 0;
		int cash = 0;
		for (int i = 0; i < R; ++i) {
			int pas = queue[index];
			int first = index;
			index = (index + 1)%N;
			while (index != first and pas + queue[index] <= k) {
				pas += queue[index];
				index = (index + 1)%N;
			}
			cash += pas;
		}
		cout << "Case #" << cas << ": " << cash << endl;
	}
}