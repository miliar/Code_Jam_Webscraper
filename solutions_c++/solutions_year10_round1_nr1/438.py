#include <iostream>
#define M 55
using namespace std;
int T,N,K;
char g[M][M],GG[M][M];
char G[M][M];
int X[8]={1,1,1,0,0,-1,-1,-1};
int Y[8]={1,0,-1,1,-1,1,0,-1};
void routate()
{
	int i,j,I,J;
	memset(GG,0,sizeof(GG));
	memset(G,0,sizeof(G));
	for (i=0,I=N-1;i<N;I--,i++)
		for (j=0,J=0;j<N;J++,j++)
		{
			GG[i][j]='.';
			G[J][I]=g[i][j];
		}
		for (j=0;j<N;j++)
		{
			J=j;I=N-1;
			for (i=N-1;i>=0;i--)
			{
				if (G[i][j]!='.') 
				{
					GG[I--][J]=G[i][j];
				}
			}
		}
		/*
		for (i=0;i<N;i++)
		{
			for (j=0;j<N;j++)
				printf("%c",G[i][j]);
			printf("\n");
		}
		for (i=0;i<N;i++)
		{
			for (j=0;j<N;j++)
				printf("%c",GG[i][j]);
			printf("\n");
		}
		*/
		return;
}
bool findans(int x,int y,char C)
{
	int i,j,cnt=0;
	for (i=x;i<x+K;i++)
	{
		if (i==N) break;
		if (GG[i][y]==C) cnt++;
		else break;
	}
	if (cnt>=K) return 1;
	cnt=0;
	for (i=y;i<y+K;i++)
	{
		if (i==N) break;
		if (GG[x][i]==C) cnt++;
		else break;
	}
	if (cnt>=K) return 1;
	cnt=0;
	for (i=x,j=y;i<N && j<N;i++,j++)
	{
		if (GG[i][j]==C) cnt++;
		else break;
	}
	if (cnt>=K) return 1;
	cnt=0;
	for (i=x,j=y;i>=0 && j<N;i--,j++)
	{
		if (GG[i][j]==C) cnt++;
		else break;
	}
	if (cnt>=K) return 1;
	return 0;
}
int check()
{
	int i,j;
	bool red=0,blue=0;
	for (i=0;i<N;i++)
		for (j=0;j<N;j++)
			if (GG[i][j]!='.')
			{
				if (GG[i][j]=='R') 
				{
					if	(findans(i,j,'R')) red=true;
				}
				else 
					if (findans(i,j,'B')) blue=true;
			}
	if (red && blue) return 3;
	if (red) return 2;
	if (blue) return 1;
	return 0;
}
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	int cases=0;
	scanf("%d",&T);
	while (T--)
	{
		int i,j;
		memset(g,0,sizeof(g));
		scanf("%d%d",&N,&K);
		for (i=0;i<N;i++)
			scanf("%s",g[i]);
		routate();
		int ans=check();
		if (ans==3) printf("Case #%d: Both\n",++cases);
		else if (ans==2) printf("Case #%d: Red\n",++cases);
		else if (ans==1) printf("Case #%d: Blue\n",++cases);
		else printf("Case #%d: Neither\n",++cases);
	}
	return 0;
}