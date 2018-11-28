#include <iostream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <stack>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(a) (int)a.size()

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

char a[600][600];
li d[600][600];
li px[600][600], py[600][600]; 
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		int n, m, D, k;
		cin >> n >> m >> D;
		forn(i, n)
			forn(j, m){
				scanf(" %c", &a[i][j]);
				d[i][j] = (D + a[i][j] - '0');
				px[i][j] = i * (D + a[i][j] - '0');
				py[i][j] = j * (D + a[i][j] - '0');
				if(i > 0){
					d[i][j] += d[i - 1][j];
					px[i][j] += px[i - 1][j];
					py[i][j] += py[i - 1][j];
				}
				if(j > 0){
					d[i][j] += d[i][j - 1];
					px[i][j] += px[i][j - 1];
					py[i][j] += py[i][j - 1];
				}
				if(i > 0 && j > 0){
					d[i][j] -= d[i - 1][j - 1];
					px[i][j] -= px[i - 1][j - 1];
					py[i][j] -= py[i - 1][j - 1];
				}
			}
		bool was = false;
		int ans = -1;
		for(int k = min(n, m); k >= 3; --k){
			forn(i, n - k + 1){
				forn(j, n - k + 1){
					li PX = px[i + k - 1][j + k - 1];
					li PY = py[i + k - 1][j + k - 1];
					li mass = d[i + k - 1][j + k - 1];
					if(i > 0){
						PX -= px[i - 1][j + k - 1];
						PY -= py[i - 1][j + k - 1];
					    mass -= d[i - 1][j + k - 1];
					}
					if(j > 0){
						PX -= px[i + k - 1][j - 1];
						PY -= py[i + k - 1][j - 1];
						mass -= d[i + k - 1][j - 1];
					
					}
					if(i > 0 && j > 0){
						PX += px[i - 1][j - 1];
						PY += py[i - 1][j - 1];
						mass += d[i - 1][j - 1];
					}
					mass -= (D + a[i][j] - '0');
					mass -= (D + a[i + k - 1][j] - '0');
					mass -= (D + a[i][j + k - 1] - '0');
					mass -= (D + a[i + k - 1][j + k - 1] - '0');
					PX -= i * (D + a[i][j] - '0');
					PX -= i * (D + a[i][j + k - 1] - '0');
					PX -= (i + k - 1) * (D + a[i + k - 1][j] - '0');
					PX -= (i + k - 1) * (D + a[i + k - 1][j + k - 1] - '0');
					PY -= j * (D + a[i][j] - '0');
					PY -= (j + k - 1) * (D + a[i][j + k - 1] - '0');
					PY -= j * (D + a[i + k - 1][j] - '0');
					PY -= (j + k - 1) * (D + a[i + k - 1][j + k - 1] - '0');
					
					double ansx = double(i + double(k - 1)/2.0), ansy = double(j + double(k - 1) / 2.0);
					if(fabs(double(PX) / double(mass) - ansx) < 1e-8
						&& fabs(double(PY) / double(mass) - ansy) < 1e-8){
						was = true;
						ans = k;
						break;
					}
				}
				if(was)
					break;
			}
			if(was)
				break;
		}
		if(was)
			printf("Case #%d: %d\n", test + 1, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", test + 1);
		
	}
	return 0;
}