#include <iostream>
#include <cstdio>
using namespace std;
int num[1005];
void solve()
{
	int n;
	scanf("%d",&n);
	for(int i = 1;i <= n;i++)
		scanf("%d",&num[i]);
	double ans = 0;
	for(int i = 1;i <= n;i++)
	{
		if(num[i] != i)
			ans++;
	}
	printf("%.10lf\n",ans);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
