#include <iostream>
using namespace std;

double solve(const int * a, const int & n)
{
bool used[n];
double ret = 0.0;
	
	for(int i = 0; i < n ; i ++)
		used[i] = false;
	
	for(int i = 0; i < n ; i ++)
	{
		if(used[i] == false)
		{
			int idx = i;
			int len = 1;
			
			while(a[idx] != i)
			{
				idx = a[idx];
				used[idx] = true;
				
				len ++;
			}
			
			if(len > 1) ret += len;
		}
	}
	
	return ret;
}

int main()
{
int T;
int N;
int *a;

	scanf("%d", &T);
	
	
	for(int test = 1; test <= T; test ++)
	{
		scanf("%d", &N);
		
		a = new int[N];
		
		for(int i = 0; i < N; i++)
		{
			scanf("%d", & a[i]);
			
			a[i] --;
		}
		
		printf("Case #%d: ", test);
		
		printf("%.9lf\n", solve(a, N));
	}
	
	return 0;
}
