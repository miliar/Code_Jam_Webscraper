#include <iostream>

using namespace std;

const int X = 10;
const int Q = 1 << X;

#define AVAILABLE(x, q) ( (mask[(x)] & (q)) == 0 )

int main()
{
	static int dp[X][Q];

	static int bits[Q];
	static int mask[X];

	for(int i = 0; i < Q; i++) {
		bits[i] = 0;
		for(int j = i; j > 0; j >>= 1) { bits[i] += (j & 1); }
	}

	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int cx, cy;
		cin >> cy >> cx;

		for(int x = 0; x < cx; x++)
			mask[x] = 0;

		for(int y = 0; y < cy; y++) {
			for(int x = 0; x < cx; x++) {
				char ch;
				cin >> ch;
				if(ch == 'x') { mask[x] |= (1 << y); }
			}
		}

		int cq = 1 << cy;

		for(int q = 0; q < cq; q++) {
			dp[0][q] = AVAILABLE(0, q) ? bits[q] : 0;
		}

		for(int x = 1; x < cx; x++) {
			for(int q = 0; q < (1 << cy); q++) {
				dp[x][q] = 0;

				if(! AVAILABLE(x, q))
					continue;

				for(int r = 0; r < (1 << cy); r++) {
					if(((q << 1) & (r << 0)) != 0) { continue; }
					if(((q << 1) & (r << 1)) != 0) { continue; }
					if(((q << 1) & (r << 2)) != 0) { continue; }
					dp[x][q] = max(dp[x][q], dp[x-1][r] + bits[q]);
				}
			}
		}

		int ans = 0;

		for(int q = 0; q < (1 << cy); q++)
			ans = max(ans, dp[cx-1][q]);

		cout << "Case #" << iCase << ": " << ans << endl;
	}

	return 0;
}
