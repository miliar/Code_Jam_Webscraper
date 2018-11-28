#include <stdio.h>
#include <string.h>
#include <math.h>

bool is_debug = false;
int cas = 0;
int	T;
long long L, P, C;


long long getNext(long long a, long long b)
{
	if (a * C >= b)
	{
		return a;
	}
	else
	{
		a *= C;
		double dou_b = ((double)b);
		double dou_C = C;
		b = ceil(dou_b / C);
		return getNext(a, b);
	}
}

long long run_left()
{
	long long left = L;
	long long right = P;

	int cnt = 0;
	while (left * C < right)	
	{
		cnt++;
		long long next = getNext(left, right);
		right = next;
	}
	return cnt;
}

long long run_right()
{
	long long left = L;
	long long right = P;

	int cnt = 0;
	while (left * C < right)	
	{
		cnt++;
		long long next = getNext(left, right);
		left = next;
	}
	return cnt;
}

int main()
{
	if (!is_debug)
	{
		freopen("in.in", "r", stdin);
		freopen("out.out", "w", stdout);
	}

	int i, j, k;

	scanf("%d", &T);	
	while (T--)
	{		
		scanf("%lld %lld %lld", &L, &P, &C);
		//printf("%d %d %d\n", L, P, C);

		int left = 0;
		int right = 0;
		
		left = run_left();
		right = run_right();
		int cnt = left > right ? left : right;		
		printf("Case #%d: %d\n", ++cas, cnt);		
	}
	return 0;
}