#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int q=1; q<=T; q++) {
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> we(N), ile(N), dl(N);
		for (int i=0; i<N; i++) {
			cin >> we[i];
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				int id = (i+j)%N;
				if (ile[i] + we[id] > k)
					break;
				ile[i] += we[id];
				dl[i] ++;
			}
		}

		long long ret = 0;
		int beg = 0;
		for (int i=0; i<R; i++) {
			ret += ile[beg];
			beg = (beg + dl[beg]) % N;
		}
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}