#include<iostream>
#include<cstdio>
using namespace std;

const int MAX = 205;
int G[MAX][MAX];
int T,N;
void init()
{
	char str[MAX];
	scanf("%d",&N);
	memset(G,0,sizeof(G));
	for(int i = 1;i <= N;++i)
	{
		scanf("%s",str);
		int len = strlen(str);
		for(int j = 0;j < len;++j)
		{
			if(str[j] == '0')	G[i][j+1] = -1;
			else if(str[j] == '1')	G[i][j+1] = 1;
			else G[i][j+1] = 0;
		}
	}
}
double WP[MAX][MAX],OWP[MAX],OOWP[MAX],RPI[MAX];
int op[MAX][MAX];
void calWP()
{
	memset(op,0,sizeof(op));
	memset(WP,0,sizeof(WP));
	for(int i = 1;i <= N;++i)
	{
		int cnt = 0,tot = 0;
		for(int j = 1;j <= N;++j)
		{
			if(G[i][j] != 0)	
			{
				++tot;
				op[i][++op[i][0]] = j;
				if(G[i][j] == 1)	++cnt;
			}
		}
		for(int j = 1;j <= op[i][0];++j)
		{
			if(tot-1 == 0)	continue;
			if(G[i][op[i][j]] == 1)
				WP[i][op[i][j]] = (cnt-1)*1.0 / (tot-1);
			else if(G[i][op[i][j]] == -1)
				WP[i][op[i][j]] = cnt * 1.0 / (tot-1);
		}
		WP[i][0] = cnt*1.0 / tot;
	}
}
void calOWP()
{
	for(int i = 1;i <= N;++i)
	{
		double owp = 0;
		int tot = 0;
		for(int j = 1;j <= N;++j)
		{
			if(G[i][j] == 0)	continue;
			owp += WP[j][i];
		}
		OWP[i] = owp * 1.0 / op[i][0];
	}
}
void calOOWP()
{
	for(int i = 1;i <= N;++i)
	{
		double oowp = 0;
		int tot = 0;
		for(int j = 1;j <= N;++j)
		{
			if(j == i)	continue;
			if(G[i][j] == 0)	continue;
			++tot;
			oowp += OWP[j];
		}
		OOWP[i] = oowp / tot;
	}
}
void calRPI()
{
	for(int i = 1;i <= N;++i)
	{
		RPI[i] = 0.25 * WP[i][0] + 0.50 * OWP[i] + 0.25 * OOWP[i];
	}
}
int Case;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		init();
		calWP();
		calOWP();
		calOOWP();
		calRPI();
		printf("Case #%d:\n",++Case);
		for(int i = 1;i <= N;++i)
		{
			printf("%lf\n",RPI[i]);
		}

	}
}