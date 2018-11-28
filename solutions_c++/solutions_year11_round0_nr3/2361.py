#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
void test();
void read_test()
{
	int T,i = 0;
	for(scanf("%d", &T); i < T; i++)
	{
		printf("Case #%d: ", i+1);
		test();
	}
}

void test()
{
	int N, xord = 0, temp, min;
        long long sum = 0;
	scanf("%d",&N);

	scanf("%d", &temp);
	xord = temp;
	sum = temp;
	min = temp;
	for(int i = 1; i < N; i++)
	{
		scanf("%d", &temp);
		xord ^= temp;
		sum += (long long)temp;

		if(temp < min)
			min = temp;
	}
	sum -= (long long)min;
	if(xord)
	{
		printf("NO\n");
	}
	else
	{
		printf("%lld\n", sum);
	}
		
/*	
	for(int i = N - num_taken; i < N; i++)
	{
		scanf("%d", &temp);
		xord ^= temp;
		arr.push_back(temp)
	//	sum += (long)temp;		
	}
		
	if(xord)
	{
		printf("NO\n");
	}
	else
	{
		sort(arr.begin(),arr.end());
		for(int i = 0; i < num_taken  ; i++)
		{
			printf(" %d ", arr[N-i-1]);
			sum += (long)arr[N - i - 1];	
		}
		printf("%ld\n",sum);
	}
*/	
}

int main()
{
	read_test();
    	return 0;
}
