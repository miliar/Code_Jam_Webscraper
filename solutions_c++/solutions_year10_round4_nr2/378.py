#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int p[10000],m[1030];
int pow[14];
int f[10000][13];
int build_pow()
{
	pow[0]=1;
	for(int i=1;i<=11;i++)
		pow[i]=2*pow[i-1];
}
int solve(int pp)
{
	int n=pow[pp+1]-1;
	memset(f,-1,sizeof(f));
	int i,j,k;
	for(i=n;i>=1;i--)
	{
		if(i*2>n){
			for(j=pp-p[i];j<=pp;j++) f[i][j]=0;
			continue;
		}
		for(j=0;j<=pp;j++){
			if(f[i*2][j]!=-1 && f[i*2+1][j]!=-1){
				if(f[i][j]==-1 || f[i][j]>f[i*2][j]+f[i*2+1][j])
					f[i][j]=f[i*2][j]+f[i*2+1][j];
			}
			if(f[i*2][j+1]!=-1 && f[i*2+1][j+1]!=-1){
				if(f[i][j]==-1 || f[i][j]>f[i*2][j+1]+f[i*2+1][j+1]+p[i])
					f[i][j]=f[i*2][j+1]+f[i*2+1][j+1]+p[i];
			}
		}
	}
	return f[1][0];
}
int main()
{
	build_pow();
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int pp;
		scanf("%d",&pp);
		int i,j,k;
		for(i=pow[pp+1]-1;i>=1;i--)
			scanf("%d",&p[i]);
		int ans=solve(pp);
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

