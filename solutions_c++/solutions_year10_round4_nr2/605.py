#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int team[2000];
int number[100];
int compete[10][1054];
int main() {
	int test,t,answer,i,j,k,temp,n;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	number[0]=1;
	for (i=1;i<32; ++i) {
		number[i]=number[i-1]*2;
	}
	scanf("%d",&test);
	for (t=1;t<=test;t++)
	{
		scanf("%d",&n);
		for (i=0;i<number[n];++i)
			scanf("%d",team+i);
		for (i=0;i<n;++i)
			for (j=0;j<number[n-1-i]; ++j)
				scanf("%d",&compete[i][j]);
		answer=0;
		for (i=0;i<n;++i)
		{
			for (j=0;j<number[n-i];j+=2)
			{
				if (team[j]==0||team[j+1]==0)
					++answer;
				else
				{
					--team[j];
					--team[j+1];
				}
			}
			for (j=0;j<number[n-i-1];++j)
				team[j]=min(team[2*j],team[2*j+1]);
		}
		printf("Case #%d: ",t);
		printf("%d\n",answer);
	}
	return 0;
}
