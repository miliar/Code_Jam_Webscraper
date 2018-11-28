#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.txt"
#define OUTPUT "out.txt"

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;

	for (int r=0; r<t; r++) {
		int s[101][101] = {0};
		bool U[101][101] = {0};
		int h,w, n; cin >> h >> w >> n;
		for (int x,y,i=0; i<n; i++) {
			cin >> x >> y;
			U[x][y] = true;
		}
		s[h][w] = 1;
		for (int i=h; i>=1; i--) {
			for (int u=w; u>=1; u--) {
				if (!U[i][u]) {
					for (int ii=i+1; ii<=h; ii++) {
						for (int uu=u+1; uu<=w; uu++) {
							if (!U[ii][uu] && (ii-i)*(ii-i) + (uu-u)*(uu-u) == 5)
								s[i][u] += s[ii][uu];
						}
					}
					s[i][u] %= 10007;
				}
			}
		}

		cout << "Case #" << r+1 << ": " << s[1][1] << endl;
	}

	return 0;
}