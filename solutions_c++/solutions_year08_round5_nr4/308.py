#include <iostream>

using namespace std;

const int N = 100;
const int M = 10007;

int main()
{
	static int  ans[N][N];
	static bool bad[N][N];

	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int w, h, r;
		cin >> w >> h >> r;

		for(int i = 0; i < w; i++) {
			for(int j = 0; j < h; j++) {
				ans[i][j] = 0;
				bad[i][j] = false;
			}
		}

		for(int i = 0; i < r; i++) {
			int x, y;
			cin >> x >> y;
			bad[x-1][y-1] = true;
		}

		ans[0][0] = 1;

		for(int y = 1; y < h; y++) {
			for(int x = 0; x < w; x++) {
				if(bad[x][y]) { continue; }
				if(x >= 1 && y >= 2) { ans[x][y] += ans[x-1][y-2]; }
				if(x >= 2 && y >= 1) { ans[x][y] += ans[x-2][y-1]; }
				ans[x][y] %= M;
			}
		}

		cout << "Case #" << iCase << ": " << ans[w-1][h-1] << endl;
	}

	return 0;
}
