#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

void test(int num)
{
	int n;
	scanf("%d",&n);
	int tmp;
	int sum=0;
	int mn=1000000000;
	int add=0;
	for(int i=0; i<n; ++i)
	{
		scanf("%d",&tmp);
		sum^=tmp;
		mn=min(mn,tmp);
		add+=tmp;
	}
	printf("Case #%d: ",num);
	if(sum!=0)
	{
		printf("NO\n");
		return;
	}
	printf("%d\n",add-mn);
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}