#include<stdio.h>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>
using namespace std;
#define MAX 110

int n;
int a[1010], b[1010];

void readin()
{
	scanf("%d\n", &n);

	for(int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
		scanf("%d", &b[i]);
	}

}

void solve()
{
	int ans=0;

	for(int i = 1; i <n; i++)
		for(int j = 0; j < i; j++)
		{
			if((a[j]-a[i])*(b[j]-b[i]) < 0) ans++;
		}
	printf("%d\n", ans);

}
int main()
{
#ifndef ONLINE_JUDGE
	//freopen("data.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif

	int cases;
	scanf("%d\n", &cases);

	for(int i = 1; i <= cases; i++)
	{
		printf("Case #%d: ", i);
		readin();
		solve();
	}

	return 0;

}
