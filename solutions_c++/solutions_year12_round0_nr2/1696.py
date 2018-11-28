#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(a,b,c) for(int a=b;a<=(c);a++)
#define FORD(a,b,c) for (int a=b;a>=(c);a--)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)

using namespace std;

typedef long long LL;  

int prog,niespod,ile,suma,result,t;

int main()
{
	scanf("%d",&t);
	FOR(j,1,t)
	{
		scanf("%d%d%d",&ile,&niespod,&prog);
		result = 0;
		prog = max(3*prog-2,0);
		REP(i,ile)
		{
			scanf("%d",&suma);
			if (suma >= prog) ++result;
				else if (niespod && suma >= max(1,prog-2)) {++result; --niespod;}
		}	
		printf("Case #%d: %d\n",j,result);
	}
	return 0;
}
