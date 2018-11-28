#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN=109;
char g[MAXN][MAXN];
int t,n,p[MAXN][MAXN];
double wp[MAXN],o[MAXN],oo[MAXN];

void init()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
		scanf("%s",g[i]+1);
}

void calcwp()
{
	memset(p,0,sizeof(p));
	memset(wp,0,sizeof(wp));
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (g[i][j]=='1')
			{
				p[i][0]++;	p[j][0]++;
				p[i][j]=p[j][i]=1;	wp[i]+=1;
			}
			else if(g[i][j]=='0')
			{
				p[i][0]++;	p[j][0]++;
				p[i][j]=p[j][i]=1;	wp[j]+=1;
			}
	for (int i=1;i<=n;i++) 
		wp[i]/=p[i][0];
}

void calco()
{
	memset(o,0,sizeof(o));
	for (int i=1;i<=n;i++)
	{
		int k=0;
		for (int j=1;j<=n;j++)
			if (p[i][j]) 
			{ 
				k++;	
				double tmp=wp[j]*p[j][0];	int tmp0=p[j][0];
				if (g[i][j]=='0') { tmp-=1; tmp0--; } else if(g[i][j]=='1') tmp0--;
				if (g[j][i]=='1') { tmp-=1; tmp0--; } else if(g[j][i]=='0') tmp0--;
				o[i]+=tmp/tmp0;
			}
		o[i]/=k;
	}
}

void calcoo()
{
	memset(oo,0,sizeof(oo));
	for (int i=1;i<=n;i++)
	{
		int k=0;
		for (int j=1;j<=n;j++)
			if (p[i][j]) { k++;	oo[i]+=o[j]; }
		oo[i]/=k;
	}
}		
			
void out()
{
	for (int i=1;i<=n;i++)
		printf("%.12lf\n",wp[i]*0.25+o[i]*0.5+oo[i]*0.25);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int test=1;test<=t;test++)
	{
		init();
		calcwp();
		calco();
		calcoo();
		printf("Case #%d:\n",test);
		out();
	}
	return 0;
}
		
	