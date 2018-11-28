#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

double p[1001],pp[1001],ans[1001];
double work(double a,int k)
{
	for(int i=2;i<=k;i++)a/=i;
	return a;
}
int num[2001],tnum[2001];
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	p[0] = p[1] = 0;
	p[2] = 0.5;
	pp[2] = 0.5;
	ans[0] = 0.0;ans[1] = 0.0;ans[2] = 2.0;
	for(int i = 3; i <= 1000; i++)
	{
		pp[i] = (-1)*pp[i-1]/i;
		p[i] = p[i-1]+pp[i];
	}
	for(int i=3;i<=1000;i++)
	{
		ans[i] = 0.0;
		for(int k = 1;k<=i-2;k++)
		{
			ans[i] += work(p[i-k],k)*(ans[i-k]+1);
		}
		ans[i] += work(1.0,i)+p[i];
		ans[i]/=(1.0-p[i]);
	}
	int T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		int cnt = 0,x;
		int N;
		scanf("%d",&N);
		for(int i = 1;i <= N; i++)
		{
			scanf("%d",&num[i]);
			tnum[i] = num[i];
		}
		sort(num+1,num+1+N);
		for(int i=1;i<=N;i++)if(tnum[i]!=num[i])cnt++;
		printf("Case #%d: %.6f\n",++cas,ans[cnt]);
	}
	return 0;
}
