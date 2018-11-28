#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;


int A, B;
int num[10];

int count(int n)
{
	int len = 0;
	int t = n;
	while(t)
	{
		num[len++] = t % 10;
		t /= 10;
	}
	int i;
	for(i = 0; i < len / 2; i++)
	{
		int tt = num[i];
		num[i] = num[len - 1 - i];
		num[len - i - 1] = tt;
	}
	int m;
	int ret = 0;
	for(i = 1; i < len; i++)
	{
		m = 0;
		int j = i;
		int cnt = 0;
		while(cnt < len)
		{
			if(j == len)
				j = 0;
			m += num[j] * pow(10, len - 1 - cnt);
			cnt++;
			j++;
		}
        if(m > n && m <= B)
		{
			ret++;
		}
	}
	return ret;
}


	

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T, cnt;
	int ans;
	cnt = 1;
	scanf("%d", &T);

	while(T--)
	{
		scanf("%d%d", &A, &B);

		ans = 0;

		for(int i = A; i <= B; i++)
		{
			ans += count(i);
		}

		printf("Case #%d: %d\n", cnt++, ans);

	}

	return 0;
}
			


