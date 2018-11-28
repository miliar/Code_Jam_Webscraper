#include<iostream>
using namespace std;

int main()
{
//	freopen("C.in","r",stdin);
//	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i++)
	{
		int n,k,mm = 2100000000,sum = 0,xor = 0;
		scanf("%d",&n);
		for (int j = 0; j < n; j++)
		{
			scanf("%d",&k);
			if (k < mm) mm = k;
			xor ^= k;
			sum += k;
		}
		printf("Case #%d: ",i);
		if (xor != 0) printf("NO\n");
		  else printf("%d\n",sum - mm);
	}
	return 0;
}