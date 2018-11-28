// C.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

int T, r, k, n;
std::vector< long long > nums;
std::vector< std::pair< long long, long long > > mas;
long long res = 0;
std::vector< long long > temp;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		nums.clear();
		mas.clear();
		temp.clear();
		res = 0;
		scanf("%d %d %d", &r, &k, &n);
		nums.resize(n);
		mas.resize(n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &nums[i]);
		}
		for (int i = 0; i < n; i++)
		{
			int j = (i + 1) % n;
			mas[i].second = nums[i];
			while (j != i && (mas[i].second + nums[j] <= k))
			{
				mas[i].second += nums[j];
				j++;
				j %= n;
			}
			mas[i].first = j;
		}
		temp.assign(n, -1);
		int index = 0, newindex = 0, rr = 0, rf = 0;
		long long value = 0, firstvalue = 0;
		while (temp[index] == -1)
		{
			temp[index] = value;
			value += mas[index].second;
			newindex = mas[index].first;
			index = newindex;
			rr++;
		}
		value -= temp[index];
		firstvalue = temp[index];
		int j = 0;
		while (j != index)
		{
			newindex = mas[j].first;
			j = newindex;
			rf++;
		}
		rr -= rf;
		j = 0;
		while (rf && r)
		{
			res += mas[j].second;
			newindex = mas[j].first;
			j = newindex;
			r--;
			rf--;
		}
		res += (r / rr) * value;
		r %= rr;
		j = index;
		while (r)
		{
			res += mas[j].second;
			newindex = mas[j].first;
			j = newindex;
			r--;
		}
		std::cout << "Case #" << t + 1 << ": " << res << std::endl;
	}
	return 0;
}

