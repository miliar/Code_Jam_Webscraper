// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

int T, n, k;
std::vector< long long > nums;
std::ifstream in("A.in");
std::ofstream out("A.out");

int main()
{

	in >> T;
	nums.resize(35);
	nums[1] = 1;
	for (int i = 2; i <= 30; i++)
	{
		nums[i] = 2 * nums[i - 1]  +1;
	}
	for (int t = 0; t < T; t++)
	{
		in >> n >> k;
		if (k % (nums[n] + 1) == nums[n])
		{
			out << "Case #" << t + 1 << ": ON" << std::endl;
		}
		else
		{
			out << "Case #" << t + 1 << ": OFF" << std::endl;
		}
	}
	return 0;
}

