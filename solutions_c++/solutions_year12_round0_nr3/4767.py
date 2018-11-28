#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
main()
{
	int test, a, b, i, x, j, num = 0, num_dig, next, cas = 1;
	int arr[2000001];
	long long int pows[9];
	long long ans;
	pows[0] = 1;
	for ( i = 1; i < 9;i++)
		pows[i] = pows[i-1] * 10;
	scanf("%d",&test);
	while (test--)
	{
		memset(&arr,0,sizeof(arr));
		scanf("%d %d",&a,&b);
		ans = 0;
		num_dig = 0;
		x = a;
		while (x)
		{
			num_dig++;
			x/=10;
		}
		for (i = a;i <=b ; i++)
		{
			if (i == pows[num_dig])
			{
				num_dig++;
			}
			if (arr[i] == 1)
				continue;
			arr[i] = 1;
			num = 1;
			for (j=1;j<=num_dig;j++)
			{
				next = (i%pows[j]) * pows[num_dig - j] + (i/pows[j]);
				if (next > b)
					continue;
				if (arr[next] == 1)
					continue;
				if ((next/pows[num_dig - 1]) == 0)
					continue;
				if (next >=a && next <=b)
				{
					arr[next] = 1;
					num++;
					//printf ("%d\n",next);
				}
			}
			ans = ans + (long long)(num*(num - 1))/2;
			//printf("%d\n",i);
		}
		printf("Case #%d: %lld\n",cas,ans);
		cas ++;
	}
}
				
