#include <stdio.h>
#include <stdarg.h>
#include <cassert>

#define IS_DEBUG 0

void dgb(const char * fmt, ...)
{
	#if IS_DEBUG
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
	#endif
}

int dp[20000];
int changeable[20000], value[20000], type[20000];
const int _and = 1;
const int _or = 0;
const int infty = 10000000;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a < b ? b : a;
}


int test(int flag, int i)
{
	int ans = infty;
	for(int j = 0; j < 8; j++)
	{
		if ((j & 1) && !changeable[i])
			continue;
		int cost = 0;
		int a1,a2;
		a1 = value[2*i];
		a2 = value[2*i+1];
		if (j & 1) 
			cost += 1;
		if (j & 2)
		{
			cost += dp[2*i];
			a1 = 1 - a1;
		}
		if (j & 4)
		{
			cost += dp[2*i+1];
			a2 = 1 - a2;
		}
		int result;
		if ((j & 1) ^ (flag == _and ? 0 : 1))
			result = a1 | a2;
		else
			result = a1 & a2;
		if (result != value[i])
		{
			ans = min(ans, cost);
			if (result + value[i] != 1)
				assert(false);
			//assert(result + value[i] == 1);
			
		}	
		
	}		
	return ans;
}


void solve(int test_case)
{
	int m,v;
	scanf("%d%d", &m,&v);
	int interior_count = (m-1)/2;

	
	for(int i = 1; i <= interior_count; i++)
		scanf("%d%d", &type[i], &changeable[i]);
	for(int i = interior_count + 1; i <= m; i++)
	{
		scanf("%d", &value[i]);
		dp[i] = infty;
	}
	for(int i = interior_count; i >= 1; i--)
	{
		if (type[i] == _and)
			value[i] = value[2*i] & value[2*i+1];		
		else		
			value[i] = value[2*i] | value[2*i+1];
		dp[i] = test(type[i], i);
	}


	printf ("Case #%d: ", test_case);
	if (value[1] == v)
		printf("0");
	else if (dp[1] == infty)
		printf("IMPOSSIBLE");
	else
		printf("%d", dp[1]);
	printf("\n");
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}