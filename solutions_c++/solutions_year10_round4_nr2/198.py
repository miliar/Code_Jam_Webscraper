
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

#define maxn 1100

int cost[12][maxn];
int p;
int m[maxn];

int dp[12][maxn][22];


int main() {
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		cin >> p;
		int n;
		n = (1 << p);
		fup(i, 0, n - 1) cin >> m[i];
		fdo(i, p - 1, 0) {
			fup(j, 0, (1 << i) - 1) {
				cin >> cost[i][j];
			}
		}
		fdo(i, p, 0) {
			fup(j, 0, (1 << i) - 1) fup(d, 0, 20) dp[i][j][d] = inf;
		}

		fup(i, 0, n - 1) {
			dp[p][i][m[i]] = 0;
		}

		fdo(i, p - 1, 0) {
			fup(j, 0, (1 << i) - 1) {
				int l, r;
				l = j * 2;
				r = l + 1;
				fup(c1, 0, 20) {
					fup(c2, 0, 20) {
						if (dp[i + 1][l][c1] > inf / 2) continue;
						if (dp[i + 1][r][c2] > inf / 2) continue;
						int ncost = dp[i + 1][l][c1] + dp[i + 1][r][c2];
						if (c1 > 0 && c2 > 0) {
							dp[i][j][min(c1, c2) - 1] = mini(dp[i][j][min(c1, c2) - 1], ncost);
						}
						dp[i][j][min(c1, c2)] = mini(dp[i][j][min(c1, c2)], ncost + cost[i][j]);
					}
				}
			}
		}
	int wyn = inf;	
	fup(i, 0, 20) wyn = min(wyn, dp[0][0][i]);
	printf("Case #%d: %d\n", c, wyn);
		


	}
	return 0;
}


