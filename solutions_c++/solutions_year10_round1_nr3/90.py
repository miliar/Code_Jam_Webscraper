#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

long n, m, t;
long a[2], b[2];

void swap(long &p1, long &p2)
{
	long tmp = p1;
	p1 = p2;
	p2 = tmp;
}

long cal(long x, long y)
{
	if (x%y == 0)
	{
		if (x/y == 1) return 0;
		return 1;
	}
	
	long flag = cal(y, x%y);
	
	if (flag == 0) return 1;	
	if (x/y == 1) return 0;
	return 1;
}

int main()
{
	freopen("CS.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		scanf("%ld%ld%ld%ld", &a[0], &a[1], &b[0], &b[1]);
		
		long ans = 0;
//		bool flag;
		for (long i = a[0]; i <= a[1]; ++i)
		{
//			flag = 1;
			for (long j = b[0]; j <= b[1]; ++j)
			{
				long p1 = i, p2 = j;
				if (p1 < p2) swap(p1, p2);
				if (cal(p1, p2)) 
				{
					++ans;
//					if (flag) flag = 0; else continue;
//					if (i < j)
//					printf("%ld %ld\n", i, j);
				}
			}
		}
		
		printf("Case #%ld: %ld\n", l, ans);
	}
		
	return 0;
}

