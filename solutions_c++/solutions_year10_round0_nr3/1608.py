#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	int R, K, N;
	int G[2001], VR[1001];
	long long VA[1001];
	long long ans;
	int p, r, k;
	
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cerr << "Case " << (i + 1) << "/" << T << endl;
		
		ans = 0;
		
		cin >> R >> K >> N;
		for (int j = 0; j < N; ++j) {
			cin >> G[j];
			G[j + N] = G[j];
			VR[j] = -1;
			VA[j] = -1;
		}
		p = 0;
		r = 0;
		while (r < R) {
			if (VR[p] >= 0) {
				int rr = (R - r) / (r - VR[p]);
				if (rr > 0) {
					ans += (ans - VA[p]) * rr;
					r += (r - VR[p]) * rr;
					if (r == R) break;
				}
			}
			VR[p] = r;
			VA[p] = ans;
			k = K;
			for (int j = 0; j < N; ++j) {
				if (k < G[p]) break;
				ans += G[p];
				k -= G[p];
				++p;
			}
			p = p % N;
			++r;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
					
	}
	
    return EXIT_SUCCESS;
}
