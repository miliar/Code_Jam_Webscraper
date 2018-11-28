#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

typedef long long i64;
i64 a[1004];

int main() {
  int cs, step = 0;
  scanf("%d", &cs);
  while(cs--) {
	step ++;
    int n;
    scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%I64d", &a[i]);
	}
	sort(a, a+n);
    i64 m = 0;
	for (int i = 1; i < n; ++i)
	{
		i64 b = a[i] - a[0];
		if (b==0)
		{
			continue;
		}
		if (m==0)
		{
			m = b;
		}
		if ((b % m))
		{
			i64 m2 = 1;
			for (i64 j = 2; j*j <= m; ++j)
			if ((m % j)==0)
			{
				if ((b % j)==0)
				{
					if (j > m2)
					{
						m2 = j;
					}
				}
				if ((b % (m/j))==0)
				{
					if (m/j > m2)
					{
						m2 = m/j;
					}
				}
			}
			m = m2;
		}
    }
	i64 add = a[0] % m;
	if (add)
	{
		add = m - add;
	}	
	printf("Case #%d: %I64d\n", step, add);
  }
  return 0;
}