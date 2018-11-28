#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "a.in"
#define OUTPUT "a.out"

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		int n,m,a; cin >> n >> m >> a;

		cout << "Case #" << i+1 << ": "; 
		for (int u=1; u<=n; u++) {
			if (a % u == 0 && a/u <= m) {
				cout << u << " 0 0 " << a/u << " 0 0" << endl;
				goto next;
			}
		}

		for (int x=0; x<=n; x++) {
			for (int y=0; y<=m; y++) {

				for (int xx=0; xx<=n; xx++) {
					for (int yy=0; yy<=m; yy++) {
						if (x*yy - xx*y == -a) {
							cout << "0 0 " << x << ' ' << y << ' ' << xx << ' ' << yy << endl;
							goto next;
						}
					}
				}
			}
		}

		cout << "IMPOSSIBLE\n";

next:;
	}

	return 0;
}