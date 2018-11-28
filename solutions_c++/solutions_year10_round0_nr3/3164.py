#include <vector>
#include <iostream>
using namespace std;

int
main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int i = 0, sum = 0;
		vector<int> Q; Q.clear();

		int R, K, N;
		cin >> R >> K >> N;
		for (int n = 0; n < N; n++) {
			int gs;
			cin >> gs;
			Q.push_back(gs);
		}
		for (int r = 0; r < R; r++) {
			int np = 0;
			int nt = 0;
			while (np < K) {
				int g = Q[i];
				if (np + g > K) {
					break;
				}
				np += g;
				if (++i >= N) {
					i = 0;
				}
				if (++nt >= N) {
					break;
				}
			}
			sum += np;
		}
		cout << "Case #" << t << ": " << sum << endl;
	}
}
