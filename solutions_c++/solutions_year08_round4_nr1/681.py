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
const int mx = 10000+2;
int M;
bool arr[mx];
bool isch[mx];
int dp[mx][2];
int ret;
int solve(int a, int val)
{
    if(a >= M)
	return INT_MAX;
    if(a >= (M - 1)/2)
	return arr[a] == val ? 0: INT_MAX;
    int& ref = dp[a][val];
    if(ref != -1)
	return ref;
    ref = INT_MAX;
    FORZ(i,2)
    {
	int x =	solve(2*a+1, i);
	FORZ(j,2)
	{
	    int y = solve(2*a + 2, j);
	    if(x == INT_MAX || y == INT_MAX)
		continue;
	    if(arr[a] == 1)
	    {
		int f = i && j;
		if(f == val)
		{
		    ref <?= x + y;
		}
		if(isch[a] == 1)
		{
		    int f = i || j;
		    if(f == val)
		    {
			ref <?= x + y + 1;
		    }
		}
	    }
	    else
	    {
		int f = i || j;
		if(f == val)
		{
		    ref <?= x + y;
		}
		if(isch[a] == 1)
		{
		    int f = i && j;
		    if(f == val)
		    {
			ref <?= x + y + 1;
		    }
		}
	    }
	}
    }
    return ref;
}
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	printf("Case #%d: ",nc);
	memset(arr, 0, sizeof arr);	
	memset(isch, 0, sizeof isch);
	memset(dp, -1, sizeof dp);
	M = GI;
	ret = GI;
	int f = M - 1;
	f /= 2;
	int x;
	for(x = 0; x < f; ++x)
	{
	    int a = GI, b = GI;
	    isch[x] = b;
	    arr[x] = a;
	}
	f = (M +1 )/2;
	FORZ(i,f)
	{
	    arr[x] = GI;
	    isch[x] = -1;
	    x++;
	}
	int val = solve(0, ret);

	if(val == INT_MAX)
	    printf("IMPOSSIBLE\n");
	else
	    printf("%d\n",val);
    }
}
