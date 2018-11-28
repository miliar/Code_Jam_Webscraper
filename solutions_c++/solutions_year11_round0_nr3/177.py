#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		int n;
		scanf("%d",&n);
		int min_value=0x7FFFFFFF;
		int sum=0;
		int flag=0;
		while (n--)
		{
			int a;
			scanf("%d",&a);
			flag^=a;
			sum+=a;
			min_value=min(min_value,a);
		}
		printf("Case #%d: ",caseI);
		if (flag!=0)
			puts("NO");
		else
			printf("%d\n",sum-min_value);
	}
	return 0;
}
