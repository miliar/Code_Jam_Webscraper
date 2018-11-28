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

int i, j, k, m, n, l, ans;
char ss[1000002];
string s[105];

int cnt[105], win[105], cc;
double wp[105], owp[105], oowp[105], ov[105];

int main() {
//	freopen("a.in", "r", stdin);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d:\n", tt);
		cin >> n;
		F0(i,n) cin >> s[i];
		F0(i,n) {
			cnt[i] = win[i] = 0;
			F0(j,n) if (s[i][j] == '1') {
				cnt[i]++; win[i]++;
			} else if (s[i][j] == '0') {
				cnt[i]++; 
			}
			wp[i] = 1.0 * win[i] / cnt[i];
		}
		F0(i,n) {
			cc = 0;
			owp[i] = 0;
			F0(j,n) if (s[j][i] != '.') {
				cc++;
				if (s[j][i] == '0') cnt[j]--;
				else if (s[j][i] == '1') { cnt[j]--; win[j]--; }
				owp[i] += 1.0 * win[j] / cnt[j];
				if (s[j][i] == '0') cnt[j]++;
				else if (s[j][i] == '1') { cnt[j]++; win[j]++; }
			}
			owp[i] /= cc;
		}
		F0(i,n) {
			cc = 0;
			oowp[i] = 0;
			F0(j,n) if (s[i][j] != '.') {
				oowp[i] += owp[j];
				cc++;
			}
			oowp[i] /= cc;
			ov[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		}
		F0(i,n) 
			printf("%.10lf\n", ov[i]);
	}
	
	return 0;
}
