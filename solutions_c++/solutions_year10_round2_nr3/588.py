#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
int f[100][100];
int g[100];
int comb[100][100];
int combi(int n,int m)
{
	if(comb[n][m]!=-1)
		return comb[n][m];
	if(m==0)
		return comb[n][m]=comb[n][n-m]=1;
	return n*combi(n-1,m-1)/m;
}
int mymax(int a,int b)
{
	return (a>b?a:b);
}
void init(int n)
{
	int i,j;
	for(i=2;i<=n;i++)
		f[i][1]=1;
	for(i=3;i<=n;i++)
		for(j=2;j<i;j++)
		{
			int k=2*j-i;
			k=mymax(k,1);
			f[i][j]=0;
			for(;k<=j-1;k++){
				int q=j-k-1;
				int p=i-j-1;
				f[i][j]+=f[j][k]*combi(p,q);
			}
		}
	for(i=2;i<=n;i++)
	{
		g[i]=0;
		for(j=1;j<i;j++)
			g[i]+=f[i][j];
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	memset(comb,-1,sizeof(comb));
	init(100);
	for(int cas=1;cas<=t;cas++)
	{
		int n;
		scanf("%d",&n);
		printf("Case #%d: %d\n",cas,g[n]%100003);
	}
	return 0;
}

