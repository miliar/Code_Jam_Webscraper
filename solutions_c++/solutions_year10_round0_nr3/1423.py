
#include <iostream>

using namespace std;

int main() {

	FILE *ifp, *ofp;
	ifp = freopen("C-large.in", "r", stdin);
	ofp = freopen("C-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		int R, k, N;
		cin >> R >> k >> N;
		long long* G = new long long[N];
		for(int j = 0; j < N; j++) {
			cin >> G[j];
		}

		long long* mon = new long long[N];
		int* pj = new int[N];
		for(int j = 0; j < N; j++) {
			int tsum = G[j];
			int tj = 1;
			while((tj < N) && (tsum + G[(j+tj) % N] <= k)) {
				tsum += G[(j+tj) % N];
				tj++;
			}
			mon[j] = tsum;
			pj[j] = (tj + j) % N;
		}

		long long tmon = 0;
		int tpj = 0;
		for(int j = 0; j < R; j++) {
			tmon += mon[tpj];
			tpj = pj[tpj];
		}

		cout << "Case #" << i << ": " << tmon << endl;
	}

	fclose(ifp);
	fclose(ofp);
	return 0;
}
