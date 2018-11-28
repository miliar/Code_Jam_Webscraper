#include <stdio.h>
#include <time.h>
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

clock_t start=clock();

#define N 1000000
char apr[N]={1,1};
int pr[88888];
int plen=0;

int inv(int a_,int m)
{
	LL p=1;
	LL a=a_;
	int n=m-2;
	for(;n;)
	{
		if(n%2) p=p*a%m;
		if(n/=2) a=a*a%m;
	}
	return p;
}

int main()
{
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);
	int i,j;
	for(i=2;i<N;i++) if(!apr[i])
	{
		pr[plen++]=i;
		for(j=i+i;j<N;j+=i) apr[j]=1;
	}
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
		int d,k;
		scanf("%d %d",&d,&k);
		int maxs=0;
		int s[11];
		for(i=0;i<k;i++)
		{
			scanf("%d",&s[i]);
			MAX(maxs,s[i]);
		}
		//if(tst!=17) continue;
		if(k==1){puts("I don't know.");continue;}
		int pd=1;
		for(i=0;i<d;i++) pd*=10;
		int sk=-1;
		for(j=0;j<plen;j++)
		{
			int p=pr[j];
			if(p<=maxs) continue;
			if(p>pd) break;
			int a=-1;
			for(i=2;i<k;i++)
			{
				if(s[i-1]==s[0])
				{
					if(s[i]!=s[1]) a=-2;
				}
				else
				{
					int a1=LL(s[i]-s[1])*inv(s[i-1]-s[0],p)%p;
					if(a1<0) a1+=p;
					if(a==-1) a=a1; else
						if(a!=a1) a=-2;
				}
				if(a==-2) break;
			}
			if(a==-2) continue;
			if(s[k-1]==s[0] || a>=0)
			{
				int sk1=(LL(a)*(s[k-1]-s[0])+s[1])%p;
				if(sk1<0) sk1+=p;
				if(sk==-1) sk=sk1; else
					if(sk!=sk1) sk=-2;
			}
			else sk=-2;
			if(sk==-2) break;
		}
		if(sk<0) puts("I don't know."); else printf("%d\n",sk);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
