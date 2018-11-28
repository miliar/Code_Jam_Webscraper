#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

int D,I,M,N;

int v[128];
int dp[128][256][2];

#define INF 1000000000

int icost(int d)
{
	if (M == 0) return INF;
	return I * ((d + (M-1)) / M);
}

int calc()
{
	forn(s,256) dp[0][s][0] = dp[0][s][0] = 0; //abs(v[0] - i);
	forsn(i,1,N+1)
	forn(valeInsertar,2)
	forn(s,256)
	{
		int &mejor = dp[i][s][valeInsertar] = dp[i-1][s][1] + D;
		forn(valor,256)
		if (abs(valor - s) <= M)
			mejor = min(mejor, abs(valor - v[i-1]) + dp[i-1][valor][1]);
		if (valeInsertar)
		forn(valor,256)
			mejor = min(mejor, icost(abs(s-valor)) + dp[i][valor][0]);
	}
	int res = INF;
	forn(s,256) res = min(res,dp[N][s][1]);
	return res;
}

int main()
{
	stdin = freopen("b.in","r",stdin);
	stdout = freopen("b.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		cin >> D >> I >> M >> N;
		forn(i,N) cin >> v[i];
		int res = calc();
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}



