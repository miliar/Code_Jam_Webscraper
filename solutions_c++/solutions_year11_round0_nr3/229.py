#include<iostream>
using namespace std;
int main()
{
	int t;
	int g = 1;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while(t -- )
	{
		int n;
		scanf("%d",&n);
		int mi = 100000000;
		int ans = 0;
		int sum = 0;
		while(n--)
		{
			int a;
			scanf("%d",&a);
			ans ^= a;
			sum += a;
			mi = mi < a? mi:a;
		}
		printf("Case #%d: ",g++);
		if(ans == 0)
			printf("%d\n",sum - mi);
		else
			printf("NO\n");
	}
}