/*
 TASK: A. Bot Trust
 LANG: C++
 by pasin30055
 */
#include <iostream>
#include <cstdio>
#include <algorithm>

#define MAX_T 105
#define MAX_N 105
#define MAX_P 105
#define INF 1000000000

using namespace std;

int t,iii;
int n,i,j,k,l,o;
int p[MAX_N];
int mic[MAX_N][MAX_P+5][MAX_P+5];
int tmp2[MAX_N][MAX_P+5][MAX_P+5];
int answer;
char in[MAX_N];

bool isin(int tmpx)
{
	if(tmpx>=0&&tmpx<MAX_P)
		return 1;
	else
		return 0;
}

int abso(int tmpx)
{
	if(tmpx>0)
		return tmpx;
	else
		return -tmpx;
}

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large-out.txt","w",stdout);
	scanf("%d",&t);
	for(iii=0;iii<t;iii++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf(" %c %d",&in[i],&p[i]);
		}
		for(i=0;i<=n;i++)
		{
			for(j=0;j<MAX_P;j++)
			{
				for(k=0;k<MAX_P;k++)
				{
					mic[i][j][k]=INF;
				}
			}
		}
		for(j=1;j<=100;j++)
		{
			for(k=1;k<=100;k++)
			{
				mic[0][j][k]=max(abso(j-1),abso(k-1));
			}
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=100;j++)
			{
				for(k=1;k<=100;k++)
				{
					if(in[i]=='O'&&j==p[i])
					{
						mic[i][j][k]=mic[i-1][j][k]+1;
						tmp2[i][j][k]=mic[i][j][k];
					}
					if(in[i]=='B'&&k==p[i])
					{
						mic[i][j][k]=mic[i-1][j][k]+1;
						tmp2[i][j][k]=mic[i][j][k];
					}
				}
			}
			for(j=1;j<=100;j++)
			{
				for(k=1;k<=100;k++)
				{
					for(l=1;l<=100;l++)
					{
						if(in[i]=='B'&&(k!=p[i]))
						{
							mic[i][j][k]=min(mic[i][j][k],mic[i][l][p[i]]+max(abso(j-l)-1,abso(k-p[i])));
						}
						if(in[i]=='O'&&(j!=p[i]))
						{
							mic[i][j][k]=min(mic[i][j][k],mic[i][p[i]][l]+max(abso(j-p[i]),abso(k-l)-1));
						}
					}
				}
			}
			for(j=1;j<=100;j++)
			{
				for(k=1;k<=100;k++)
				{
					for(l=1;l<=100;l++)
					{
						if(in[i]=='B'&&(k==p[i]))
						{
							tmp2[i][j][k]=min(tmp2[i][j][k],mic[i][l][p[i]]+max(abso(j-l)-1,abso(k-p[i])));
						}
						if(in[i]=='O'&&(j==p[i]))
						{
							tmp2[i][j][k]=min(tmp2[i][j][k],mic[i][p[i]][l]+max(abso(j-p[i]),abso(k-l)-1));
						}
					}
				}
			}
			for(j=1;j<=100;j++)
			{
				for(k=1;k<=100;k++)
				{
					if(in[i]=='B'&&(k==p[i]))
					{
						mic[i][j][k]=tmp2[i][j][k];
					}
					if(in[i]=='O'&&(j==p[i]))
					{
						mic[i][j][k]=tmp2[i][j][k];
					}
				}
			}
		}
		answer=INF;
		for(j=0;j<MAX_P;j++)
		{
			for(k=0;k<MAX_P;k++)
			{
				answer=min(answer,mic[n][j][k]);
			}
		}
		printf("Case #%d: %d\n",iii+1,answer);
	}
	return 0;
}