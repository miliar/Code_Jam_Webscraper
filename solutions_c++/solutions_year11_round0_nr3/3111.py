#include <iostream>
using namespace std;

int N;
int *a;


int main()
{
int T;
	
	scanf("%d", &T);
	
	
	for(int test = 1; test <= T; test ++)
	{
		scanf("%d", &N);
		
		a = new int[N];
		
		int x = 0, sum = 0, minElement = INT_MAX;
		
		for(int i = 0; i < N; i++)
		{
			scanf("%d", & a[i]);
			
			x ^= a[i];
			sum += a[i];
			minElement = min(minElement, a[i]);
		}
		
		printf("Case #%d: ", test);
		
		if(x)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", sum - minElement);
		}
	}
	
	//system("pause");
	
	return 0;
}
