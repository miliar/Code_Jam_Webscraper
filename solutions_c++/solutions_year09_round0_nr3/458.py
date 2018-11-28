#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))
#define MOD 10000

char s[550];
int way[505][20];
char f[] = {"welcome to code jam"};

int calc(int i,int j)
{
	if (j < 0) return 1;
	if (i < 0) return 0;
	if (way[i][j]==-1)
	{
		int res = 0;
		if (s[i]==f[j]) res = calc(i-1,j-1);
		res += calc(i-1,j);
		way[i][j] = res % MOD;
	}
	return way[i][j];	
}

int main()
{
	int t;
	scanf("%d",&t);
	gets(s);
	REP(T,t)
	{
		gets(s);
		_m(way,-1);
		printf("Case #%d: %04d\n",T+1,calc(strlen(s)-1,strlen(f)-1));
	}
	return 0;	
}
