#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;
 
#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FORI(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOR(i,a,b) for(LET(i,a);i < (b);++i)
#define FORZ(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define CS c_str()
#define PB push_back
#define SZ size()
#define INF (int)1e9+1
const int mod = 10007;
int U[][2] = {{2, 1}, {2, -1}, {1, 2}, {-1, 2},{1, -2}, {-1, -2}, {-2, 1}, {-2, -1}};
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	printf("Case #%d: ",nc);
	int H = GI, W = GI;
	int R = GI;
	bool pos[H][W];
	memset(pos, 0, sizeof pos);
	while(R--)
	{
	    int a = GI, b = GI;
	    a--, b--;
	    pos[a][b] = 1;
	}
	int dp[H][W];
	dp[0][0] = 1;
	FORZ(i,H)
	{
	    FORZ(j,W)
	    {
		if(i == 0 && j == 0)
		    continue;
		dp[i][j] = 0;
		if(pos[i][j] == 1)
		    continue;
		//dbge(i);
	//	dbge(j);
		FORZ(x,8)
		{
		    int di = i + U[x][0];
		    int dj = j + U[x][1];
		    if(di >= 0 && di < H && dj >= 0 && dj < W)
		    {
			if(di < i && dj < j)
			{
			    //dbge(di);
			   // dbge(dj);
			    dp[i][j] += dp[di][dj], dp[i][j] %= mod;
			}
		    }
		}
		dp[i][j] %= mod;

	    }
	}
	printf("%d\n",dp[H-1][W-1]);

    }
}
