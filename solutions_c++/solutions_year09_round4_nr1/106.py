#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))
#define FOR(a,b,c) for(int a=(b); a<(c); ++a)

char a[50][50];

int Swap(int i, int j)
{
	//FOR(t,i,j)
	for (int t = j-1; t >= i; --t)
	{
		FOR(k,0,50) swap(a[t][k], a[t+1][k]);
	}
	return j - i;
}

int ok(int n, char *s, int i)
{
	FOR(t,i+1,n) if (s[t] == '1') return false;
	return true;
}

int main()
{
    int T;

	scanf("%d", &T);
	FOR(cas,1,T+1)
	{
		int n;
		scanf("%d", &n);
		FOR(i,0,n) scanf("%s", a[i]);
		int res = 0;
		FOR(i,0,n)
		{
			FOR(j,i,n)
				if (ok(n, a[j], i))
				{
					res += Swap(i, j);
					break;
				}
		}
		printf("Case #%d: %d\n", cas, res);
	}	

    return 0;
}
