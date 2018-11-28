#include <stdio.h>
#include <algorithm>

using namespace std;


const long long bound = 10000000000000000;


long long num[10001];

long long gcd(long long a, long long b)
{
	if( 0 == a % b )
	{
		return b;
	}
	else
	{
		return gcd(b, a%b);
	}
}

long long lcm(long long a, long long b)
{
	return (a*b)/gcd(a,b);
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int testNum = 0;
	scanf("%d", &testNum);
	for(int tc = 1; tc <= testNum; tc++)
	{
		long long N, L, H;
		scanf("%lld%lld%lld", &N, &L, &H);
		
		for(int i = 0; i < N; i++)
		{
			scanf("%lld", &num[i]);
		}

		sort(&num[0], &num[N]);

		


		int ans = -1;
		for(int k = L; k <= H; k++)
		{
			bool isH = true;
			for(int i = 0; i < N; i++)
			{
				if( 0 == num[i] % k || 0 == k % num[i] )
				{

				}
				else
				{
					isH = false;
					break;
				}
			}
			
			if(isH)
			{
				ans = k;
				break;
			}
			
		}

		printf("Case #%d: ", tc);
		if( -1 != ans )
		{
			printf("%d\n", ans);
		}
		else
		{
			printf("NO\n");
		}
		
	}
	return 0;
}