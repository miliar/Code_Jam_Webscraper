#include <iostream>
#include <string>
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
int dp[1 << 11][11];
bool arr[11][11];
int M, N;
int solve(int prev, int row)
{
    if(row == M)
	return 0;
    int cur = 0;
    int& ref = dp[prev][row];
    if(ref != -1)
	return ref;
    FORZ(i,N)
    {
	if((i - 1 < 0 || !(prev & (1 << (i - 1)))) && (i + 1 > N || !(prev & (1 << (i + 1)))) && arr[row][i] == 1)
	    cur |= (1 << i);
    }
    ref = 0;
    int x = __builtin_popcount(cur);

    FORZ(yy, (1 << x))
    {
	int st = 0;
	int t = cur;
	FORZ(i,N)
	{
	    if(cur & (1 << i))
	    {
		if(!(yy & (1 << st)))
		    t &= ~(1 << i);
		st++;
	    }
	}
	bool f = 1;
	FOR(i,1,N)
	{
	    if(t & (1 << i))
		if(t & (1 << (i - 1)))
		{
		    f = 0;
		    break;
		}
	}
	if(f)
	    ref >?= solve(t, row + 1) + __builtin_popcount(t);
    }
    return ref;
}
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	printf("Case #%d: ",nc);
	M = GI, N = GI;
	arr[M][N];
	int ret = 0;
	FORZ(i,M)	
	{
	    string s;
	    cin >> s;
	    FORZ(j,N)
		arr[i][j] = s[j] == '.';
	}
	memset(dp, -1, sizeof dp);
/*	for(int st = 0; st < (1 << N); ++st)
	{
	    bool f = 1;
	    FORZ(i,N)
		if(st & (1 << i))
		    if(!arr[0][i])
		    {
			f = 0;
			break;
		    }
	    if(f)
		ret >?= solve(st, 1) + __builtin_popcount(st);
	}
    */
	printf("%d\n", solve(0,0));
    }
}
