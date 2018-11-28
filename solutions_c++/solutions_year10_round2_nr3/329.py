#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
#define INF 1000000000
typedef long long tint;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<int,int> pint;

const int MAXN = 512, M = 100003;
int dp[MAXN][MAXN];
int C[MAXN][MAXN];

void comb()
{
	forn(n,MAXN) C[n][0] = 1;
	forsn(n,1,MAXN)
		forsn(k,1,n+1)
			C[n][k] = (C[n-1][k-1] + C[n-1][k]) % M;
}

void calc()
{
	forn(n,MAXN) dp[n][1] = 1;
	forsn(n,2,MAXN)
		forsn(k,2,n)
			forsn(r,1,k)
			{
				dp[n][k] += (C[n-k-1][k-r-1]*dp[k][r])%M;
				dp[n][k]%=M;
			}
}

int main()
{
	zMem(C); zMem(dp);
	comb();
	calc();
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int N; cin >> N;
		int res = 0;
		forsn(k,1,N) res += dp[N][k];
		res %= M;
		cout << "Case #" << tt+1 << ": " << res << endl;
	}
	return 0;
}
