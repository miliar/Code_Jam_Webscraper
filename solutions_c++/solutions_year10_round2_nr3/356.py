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
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

#define MOD 100003

#define N 501

int bin[N][N];
int f[N][N];

int main()
{
	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);
	int n,k,i;
	for(n=0;n<N;n++) bin[n][0]=bin[n][n]=1;
	for(n=2;n<N;n++)
		for(k=1;k<n;k++) bin[n][k]=(bin[n-1][k-1]+bin[n-1][k])%MOD;
	for(n=2;n<N;n++)
	{
		f[n][1]=1;
		for(k=2;k<n;k++)
		{
			for(i=1;i<k;i++)
				f[n][k]=(f[n][k]+LL(f[k][i])*bin[n-k-1][k-i-1])%MOD;
			//printf("f[%d][%d]=%d\n",n,k,f[n][k]);
		}
	};
	int T,t=0;
	for(scanf("%d",&T);T--;)
	{
		scanf("%d",&n);
		int ans=0;
		for(k=1;k<n;k++)
			ans=(ans+f[n][k])%MOD;
		printf("Case #%d: %d\n",++t,ans);
	}
	return 0;
}
