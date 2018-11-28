#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <climits>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <list>
#include <algorithm>

using namespace std;

#define FORI(N) for (int i = 0; i < (N); i++)
#define FOREI(N) for (int i = 1; i <= (N); i++)
#define FORJ(N) for (int j = 0; j < (N); j++)
#define FOREJ(N) for (int j = 1; j <= (N); j++)
#define FORK(N) for (int k = 0; k < (N); k++)
#define FOREK(N) for (int k = 1; k <= (N); k++)
#define ALL(A) A.begin(), A.end()
#define EACH(A,T) for (typeof(A.begin()) T = A.begin(); T != A.end(); T++)
#define REP(N) while (N--)

#define sz size()
#define pb(N) push_back(N)
#define CLEAR(M,O) memset (M, C, sizeof(M))

typedef long long int lint;
typedef pair <lint, lint> ip;
typedef vector <ip> VI;

#define fi first
#define se second

lint dp[100001][3][3][3];

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int n;
		lint A,B,C,D,x0,y0,M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		VI a;
		lint x = x0, y = y0;
		FORI(n)
		{
			a.pb(ip(x,y));
			x = (A*x + B) % M;
			y = (C*y + D) % M;
		}
		FORI(3) FORJ(3) FORK(3) dp[0][i][j][k] = 0;
		dp[0][0][0][0] = 1;
 #define FORL(N) for (int l = 0; l < (N); l++)
        lint c = 0;
		FORI(n)
		{
			FORJ(3) FORK(3) FORL(3) dp[i+1][j][k][l] = dp[i][j][k][l];
			FORJ(3) FORK(3)
				dp[i+1][1][(a[i].fi+j)%3][(a[i].se+k)%3] += dp[i][0][j][k];
			FORJ(3) FORK(3)
			    dp[i+1][2][(a[i].fi+j)%3][(a[i].se+k)%3] += dp[i][1][j][k];
            FORJ(3) FORK(3)
			    if ((a[i].fi+j)%3 == 0 && (a[i].se+k)%3 == 0) c += dp[i][2][j][k];
		}
		cout << "Case #" << cc << ": " << c << endl;
	}
	return 0;
}
