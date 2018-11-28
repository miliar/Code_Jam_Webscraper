#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxC = 1010;

struct Point{
	int val, cnt;
	Point(): val(0), cnt(0){}
	Point(int _val, int _cnt):val(_val), cnt(_cnt){}

	bool operator<(const Point & point)const
	{
		return val < point.val;
	}
};

int w, n, c, l;
long long t, ar[maxC], sum;
long long ans;
long long diff[20010];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &w);
	for (int q = 0; q < w; q++)
	{
		ans = sum = 0;
		memset(diff, 0, sizeof(diff));
		scanf("%d%lld%d%d", &l, &t, &n, &c);
		for (int i = 0; i < c; i++)
		{
			scanf("%lld", &ar[i]);
			sum += ar[i];
		}
		long long k = t / (sum * 2);
		if (n > c * k)
		{
			n -= c * k;
			ans += k * sum * 2;
			t -= k * sum * 2;
		}
		if (n > c)
		{
			for (int i = 0; i < c; i++)
			{
				diff[ar[i]] += (n - c) / c;
				if ((n - c) % c > i)
				{
					diff[ar[i]]++;
				}
			}
		}
		long long cur = 0;
		for (int i = 0; i < c; i++)
		{
			cur += ar[i] * 2;
			if (cur >= t)
			{
				ans += (ar[i] * 2 - (cur - t));
				if ((cur - t) % 2 == 1)
				{
					ans += (cur - t);
				}
				else
				{
					diff[(cur - t) / 2]++;
				}
				for (int j = i + 1; j < c; j++)
				{
					diff[ar[j]]++;
				}
				break;
			}
			else
			{
				ans += ar[i] * 2;
			}
		}
		for (int i = 10000; i > 0; i--)
		{
			if (diff[i] > 0)
			{
				if (diff[i] <= l)
				{
					ans += diff[i] * i;
					l -= diff[i];
					diff[i] = 0;
				}
				else
				{
					ans += l * i;
					diff[i] -= l;
					l = 0;
					ans += diff[i] * i * 2;
				}
			}
		}
		printf("Case #%d: %lld\n", q + 1, ans);
	}
	return 0;
}