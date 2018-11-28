#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
    int ones[30];
		int smallest = 10000000;
		int sum = 0;
		
		//init
		for (int i = 0; i < 30; i++)
			ones[i] = 0;
		
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			int x;
			scanf("%d", &x);
			
			smallest = min(smallest, x);
			sum += x;
			
			for (int j = 0; j < 30; j++)
			{
				ones[j] += x % 2;
				x /= 2;
			}
		}
		
		//check
		bool ok = true;
		for (int i = 0; i < 30; i++)
			if (ones[i] % 2 == 1)
			{
				ok = false;
				break;
			}
			
	  //output
		printf("Case #%d: ", Ti);
	  if (!ok)
			printf("NO\n");
		else
			printf("%d\n", sum - smallest);
	}
	return 0;
}