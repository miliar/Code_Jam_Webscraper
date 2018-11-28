#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<set>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<vector>
#include<iostream>
#define PINF 2000000000
#define NINF -2000000000
using namespace std;
int n,m,t,c;
int chk[1001];
vector<int> x[1001];
int search(int idx)
{
	chk[idx]++;
	if(chk[idx]>=2)
		return 1;
	for(int i=0;i<x[idx].size();i++)
	{
		if(search(x[idx][i]))
			return 1;
	}
	return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		int ans=0;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			x[i].clear();
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&m);
			for(int j=0;j<m;j++)
			{
				int ty;
				scanf("%d",&ty);
				x[i].push_back(ty);
			}
		}
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
				chk[j]=0;	
			if(search(i))
			{
				ans=1;
				break;
			}
		}
		printf("Case #%d: ",c);
		if(ans)
			printf("Yes\n");
		else
			printf("No\n");
	}
    scanf(" ");
}
