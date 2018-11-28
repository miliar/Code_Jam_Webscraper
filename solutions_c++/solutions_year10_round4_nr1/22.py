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
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, ans, ii, jj;
char ss[10000];
char s[1001][1001];

void check(int x, int y, char c, int& g) {
	if (x < 0 || x >= 2*n-1) return;
	if (y < 0 || y >= 2*n-1) return;
	if (!isdigit(s[x][y])) return;
	if (s[x][y] != c) g = 0;
}

int main() {
//	freopen("a.in", "r", stdin);

//	freopen("A-small-attempt1.in", "r", stdin);
//	freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		scanf("%d", &n);
		gets(ss);
		F0(i,2*n-1) F0(j,2*n-1) s[i][j] = ' ';
		F0(i,2*n-1) {
			gets(s[i]);
		}
		F0(i,2*n-1) F0(j,2*n-1) if (!isdigit(s[i][j])) s[i][j] = ' ';
		ans = inf;
		F0(i,2*n-1) F0(j,2*n-1)  {
			int g = 1, l = 0;
			F0(ii,2*n-1) F0(jj,2*n-1) if (isdigit(s[ii][jj])) {
				l = max(l, abs(i-ii)+abs(j-jj));
				check(2*i-ii, jj, s[ii][jj], g);
				check(2*i-ii, 2*j-jj, s[ii][jj], g);
				check(ii, 2*j-jj, s[ii][jj], g);
			}

			if (g) {
				if (l < ans) ans = l;
			}
		}
		ans++;

		ans = ans*ans - n*n;
		
		printf("Case #%d: ", tt);
		cout << ans << endl;
	}
	
	return 0;
}
