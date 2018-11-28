#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

inline LL min(LL a,LL b){return ((a)<(b)?(a):(b));}

#define N 14
#define M 10000
int n;
int m[M];
LL INF=LL(inf)*10000;
LL f[M][N];

LL F(int u,int d)
{
	LL &ans=f[u][d];
	if(ans>=0) return ans;
	if(u%2)
	{
		if(m[u]<n-d) return ans=INF;
		return ans=0;
	}
	int h=(u&-u)/2;
	return ans=min(F(u-h,d)+F(u+h,d),F(u-h,d+1)+F(u+h,d+1)+m[u]);
}

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		scanf("%d",&n);
		int i,j;
		for(j=0;j<=n;j++)
			for(i=0;i<bit(n-j);i++)
				scanf("%d",&m[bit(j)*(2*i+1)]);
		fill(f,255);
		LL ans=F(bit(n),0);
		printf("%I64d\n",ans);
	}
	return 0;
}
