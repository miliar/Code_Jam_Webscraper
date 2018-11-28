// B.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>

std::ifstream in("B.in");
std::ofstream out("B.out");

int C, n;
std::vector< long long > nums;

int main()
{
	in >> C;
	for (int c = 0; c < C; c++)
	{
		in >> n;
		long long max = -1;
		nums.resize(n);
		for (int i = 0; i < n; i++)
		{
			in >> nums[i];
		}
		std::sort(nums.begin(), nums.end());
		long long d = 0;
		if (n == 2)
		{
			d = nums[1] - nums[0];
		}
		else
		{
			d = nums[2] - nums[1];
			long long d2 = nums[1] - nums[0];
			if (d == 0 || d2 < d && d2 != 0)
			{
				d = d2;
			}
		}
		long long res = -1;
		std::vector< long long > temp;
		temp.resize(n);

		for (int i = 1; i <= sqrt((double)d); i++)
		{
			if (d % i == 0)
			{
				int x = i, y = d / i;
				for (int j = 0; j < n; j++)
				{
					temp[j] = nums[j] % x;
				}
				bool f = true;
				for (int j = 1; j < n; j++)
				{
					if (temp[j - 1] != temp[j])
						f = false;
				}
				if (f && x > res)
				{
					res = x;
				}
				for (int j = 0; j < n; j++)
				{
					temp[j] = nums[j] % y;
				}
				f = true;
				for (int j = 1; j < n; j++)
				{
					if (temp[j - 1] != temp[j])
						f = false;
				}
				if (f && y > res)
				{
					res = y;
				}
			}
		}
		if (res > 1 && nums[0] % res != 0)
		{
			out << "Case #" << c + 1 << ": " << res - (nums[0] % res) << std::endl;
		}
		else
		{
			out << "Case #" << c + 1 << ": 0" << std::endl;
		}
	}
	return 0;
}

