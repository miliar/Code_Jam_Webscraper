#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, m, n, l, n1, n2, Num[1801][1801], ans;
int d[3504][3504], x[3504], y[3504], v[3504];
char s[801][801];

int dx[] = {1,1,0,0};
int dy[] = {-1,1,-1,1};

int rec(int i) {
	if (v[i]) return 0;
	v[i] = 1;
	for (int j = 1; j <= n2; j++)
		if (d[i][j]) {
			if (y[j]==0 || (v[y[j]]==0 && rec(y[j]))) {
				x[i] = j;
				y[j] = i;
				return 1;
			}
		}
	return 0;
}


int a[12][4000];
void maskebi()
{
	memset(a, 0, sizeof(a));
	for (i = 0; i < (1<<n); i++) {
		int f = 1, r = 0;
		for (j = 0; j < n; j++) if ((1<<j)&i) {
			if (s[0][j] != '.') { f = 0; break; }
			if (j+1 < n && ((1<<(j+1))& i)) { f = 0; break; }
			r++;
		}
		if (f) {
			a[0][i] = r; 
		} else a[0][i] = -inf;
	}
	for (i = 1; i < m; i++)
		for (j = 0; j < (1<<n); j++)
			a[i][j] = -inf;

	for (int row = 1; row < m; row++)
	for (int mask = 0; mask < (1<<n); mask++)
	if (a[row-1][mask] >= 0)
	{
		for (i = 0; i < (1<<n); i++) {
	
			int f = 1, r = 0;
			for (j = 0; j < n; j++) if ((1<<j)&i) {
				if (s[row][j] != '.') { f = 0; break; }
				if (j+1 < n && (1<<(j+1))& i) { f = 0; break; }
				if (j > 0 && ((1<<(j-1))&mask)) { f = 0; break; }
				if (j+1 < n && ((1<<(j+1))&mask)) { f = 0; break; }
				r++;
			}
			if (f) {
				a[row][i] = max(a[row][i], r + a[row-1][mask]);
			}
		}
	}
	ans = 0;
	F0(i,(1<<n)) ans = max(ans, a[m-1][i]);
	cout << ans << endl;
}

int main() {

//	freopen("x.in", "r", stdin);

//	freopen("C-small-attempt2.in", "r", stdin);
//	freopen("C-small-attempt2dva.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		memset(Num, 0, sizeof(Num));
		printf("Case #%d: ", tt);
		cin >> m >> n;
		gets(s[0]);
		F0(i,m) gets(s[i]);

/*		maskebi();
		continue; 
		cout << ans << endl; */
		n1 = n2 = 0;
		F0(i,m) {
			F0(j,n) if (s[i][j] != 'x') {
				if (j%2==0) {
					n1++;
					Num[i][j] = n1;
			} else {
					n2++;
					Num[i][j] = n2;
				}
			}
		}
		ans = 0;
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		memset(d, 0, sizeof(d));

		F0(i,m) {
			F0(j,n) if (s[i][j] == '.' && j%2==1) {
				F0(k,4) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (x >= 0 && y >= 0 && x < m && y < n && s[x][y] == '.') {
						d[Num[x][y]][Num[i][j]] = 1;
					}
				}
			}
		}
		F0(i,m) {
			F0(j,n) if (s[i][j] == '.' && j%2==0) {
				F0(k,4) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (x >= 0 && y >= 0 && x < m && y < n && s[x][y] == '.') {
						d[Num[i][j]][Num[x][y]] = 1;
					}
				}
			}
		}
	
		F1(i,n1) F1(j,n2) if (d[i][j] && x[i] == 0 && y[j] == 0) {
			x[i] = j;
			y[j] = i;
			ans++;
		}
		F1(i,n1) if (x[i] == 0) {
			memset(v, 0, sizeof(v));
			ans += rec(i);
		}  
		cout << n1 + n2-ans;
		printf("\n");
	}
	
	return 0;
}
