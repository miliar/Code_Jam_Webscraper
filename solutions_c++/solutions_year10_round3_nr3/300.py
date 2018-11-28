#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>
using namespace std;
int g[33][33]={{0}};
int b[33]={0}, n, m;
bool u[33][33]={{0}};
void us(int i, int j, int p )
{
	int k, t;
	for(k=i; k<=i+p-1; k++)
		for(t=j; t<=j+p-1; t++)
			u[k][t]=1;
}
bool find(int k, int l, int p)
{
	int i, j;
	if(k+p-1>m||l+p-1>n)
		return 0;

	for(i=k; i<=p+k-1; i++)
		for(j=l; j<=p+l-1; j++)
		{
			if(i!=k)
			{
				if(g[i][j]==g[i-1][j]||u[i][j])
					return 0;
			}
			if(j!=l)
			{
				if(g[i][j]==g[i][j-1]||u[i][j])
					return 0;
			}
		}
	return 1;
}
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int tt, ii,cnt, i, j, k, mx;
	bool f;
	char a[77][6]={{0}}, c;
	strcpy(a[48],"0000");
	strcpy(a[49],"0001");
	strcpy(a[50],"0010");
	strcpy(a[51],"0011");
	strcpy(a[52],"0100");
	strcpy(a[53],"0101");
	strcpy(a[54],"0110");
	strcpy(a[55],"0111");
	strcpy(a[56],"1000");
	strcpy(a[57],"1001");
	strcpy(a[65],"1010");
	strcpy(a[66],"1011");
	strcpy(a[67],"1100");
	strcpy(a[68],"1101");
	strcpy(a[69],"1110");
	strcpy(a[70],"1111");

	
	scanf("%d\n", &tt);
	for(ii=1; ii<=tt; ii++)
	{
		scanf("%d %d\n", &m, &n);
		for(i=1; i<=m; i++)
		{
			for(j=1; j<=n/4; j++)
			{
				scanf("%c", &c);
				for(k=0; k<4; k++)
					g[i][(j-1)*4+k+1]=a[c][k]-48;
			}
			scanf("\n");
		}
		/*
		for(i=1; i<=m; i++)
		{
			cout<<'\n';
			for(j=1; j<=n; j++)
				cout<<g[i][j]<<' ';
		}
		cout<<'\n';*/
		mx=min(n, m);
		
		while(mx>=1)
		{
			for(i=1; i<=m; i++)
				for(j=1; j<=n; j++)
					if (!u[i][j]&&find(i, j, mx))
					{
						b[mx]++;
						us(i, j, mx);
					}
			mx--;
		}
		cnt=0;
		for(i=1; i<=32; i++)
			if(b[i]>0)
				cnt++;
		printf("Case #%d: %d\n", ii, cnt);
		for(i=32; i>=1; i--)
		{
			if(b[i])
				printf("%d %d\n", i, b[i]);
			b[i]=0;
		}
		for(i=1; i<=32; i++)
			for(j=1; j<=32; j++)
				u[i][j]=g[i][j]=0;		
	}
	return 0;
}