#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x)
{
    return x*x;
}

int gcd(int a, int b)
{
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

#define MAXN 505

int sum[MAXN][MAXN];
char mat[MAXN][MAXN];

int getsum(int x1, int y1, int x2, int y2) {
	int ret = sum[x2][y2];
	if(x1) ret -= sum[x1-1][y2];
	if(y1) ret -= sum[x2][y1-1];
	if(x1 && y1) ret += sum[x1-1][y1-1];
	return ret;
}

int main(int argc, char** argv)
{
	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int ti=1; ti<=t; ++ti) {
		int R, C, D;
		scanf("%d%d%d", &R, &C, &D);
		mset(sum, 0);
		mset(mat, 0);

		for(int i=0; i<R; ++i) {
			scanf("%s", mat[i]);
			for(int j=0; j<C; ++j) {
				sum[i][j] = (mat[i][j] - '0' + D);
				if(i) sum[i][j] += sum[i-1][j];
				if(j) sum[i][j] += sum[i][j-1];
				if(i&&j) sum[i][j] -= sum[i-1][j-1];
			}
		}

		int l = 3, r = min(R, C);
		int ans = 0;

		for(int sz=min(R,C); sz>=3; --sz) {
			bool findans = 0;
			for(int i=0; i+sz-1<R; ++i) {
				for(int j=0; j+sz-1<C; ++j) {
//					cout<<i<<" "<<j<<" "<<sz<<endl;
					int sumr = getsum(i, j, i, j+sz-1) - mat[i][j] - mat[i][j+sz-1] + 2*'0' - 2*D;
					int sumc = getsum(i, j, i+sz-1, j) - mat[i][j] - mat[i+sz-1][j] + 2*'0'- 2*D;
					for(int k = 1; k<sz/2; ++k) {
						sumr += getsum(i, j, i+k, j+sz-1) - mat[i][j] - mat[i][j+sz-1] + 2*'0'- 2*D;
						sumc += getsum(i, j, i+sz-1, j+k) - mat[i][j] - mat[i+sz-1][j] + 2*'0'- 2*D;
					}
//					dbg(sumr);
//					dbg(sumc);


					sumr -= getsum(i+sz-1, j, i+sz-1, j+sz-1) - mat[i+sz-1][j] - mat[i+sz-1][j+sz-1] + 2*'0'- 2*D;
					sumc -= getsum(i, j+sz-1, i+sz-1, j+sz-1) - mat[i][j+sz-1] - mat[i+sz-1][j+sz-1] + 2*'0'- 2*D;
					
					for(int k = 1; k<sz/2; ++k) {
						sumr -= getsum(i+sz-k-1, j, i+sz-1, j+sz-1) - mat[i+sz-1][j] - mat[i+sz-1][j+sz-1] + 2*'0'- 2*D;
						sumc -= getsum(i, j+sz-k-1, i+sz-1, j+sz-1) - mat[i][j+sz-1] - mat[i+sz-1][j+sz-1] + 2*'0'- 2*D;
					}
//					dbg(sumr);
//					dbg(sumc);
					
					if(!sumr && !sumc) {
						findans = 1;
						goto loop;
					}
				}
			}
			loop: if(findans) {
				ans = sz;
				break;
			}
		}
		printf("Case #%d: ", ti);
		if(!ans) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
    return (EXIT_SUCCESS);
}

