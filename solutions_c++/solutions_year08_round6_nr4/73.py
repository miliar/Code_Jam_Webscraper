#include<stdio.h>

int N,M;
int u[100],t[100];
int w1[100][100],w2[100][100];
int solve;

int CHECK()
{
	int ok=1;
	int i,j;

	for(i=1;i<=M;i++)
		for(j=1;j<=M;j++)
			if(w2[i][j]==1)
			{
				if(w1[ u[i] ][u[j]]==1);
				else return solve=0;
			}
			else
			{
				if(w1[ u[i] ][u[j]]==0);
				else return solve=0;
			}

	return solve=1;
}

void SOLVE(int at)
{
	if(solve) return;

	if(at==M+1)
	{
		CHECK();
		return;
	}

	int i;

	for(i=1;i<=N;i++)
		if(t[i]==0)
		{
			t[i]=1;
			u[at]=i;
			SOLVE(at+1);
			if(solve) return;
			t[i]=0;
		}
}

int main()
{
	int T,ks,a,b,i,j;

	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d",&N);
		for(i=1;i<=N;i++)
			for(j=1;j<=N;j++)
				w1[i][j]=0;

		for(i=1;i<N;i++)
		{
			scanf("%d%d",&a,&b);
			w1[a][b]=w1[b][a]=1;
		}

		scanf("%d",&M);
		for(i=1;i<=M;i++)
			for(j=1;j<=M;j++)
				w2[i][j]=0;

		for(i=1;i<M;i++)
		{
			scanf("%d%d",&a,&b);
			w2[a][b]=w2[b][a]=1;
		}

		solve=0;
		for(i=1;i<=N;i++) u[i]=0,t[i]=0;

		SOLVE(1);

		if(solve) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}