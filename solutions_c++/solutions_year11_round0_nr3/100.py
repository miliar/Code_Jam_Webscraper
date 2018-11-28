#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		int n;
		int minvalue = 0x3fffffff;
		int sumvalue = 0;
		int bit = 0;
		int x;
		int i;
		scanf("%d" , &n);
		for(i = 0;i < n;i++)
		{
			scanf("%d" , &x);
			minvalue = min(minvalue , x);
			sumvalue += x;
			bit ^= x;
		}
		printf("Case #%d: " , ++ii);
		if(bit != 0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n" , sumvalue - minvalue);
		}
	}
	return 0;
}