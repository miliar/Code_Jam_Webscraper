// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

std::ifstream in("a.in");
std::ofstream out("a.out");

int T;
std::string text;
std::vector< int > letters; 
std::vector< int > nums;
std::vector< int > number;
long long solve(std::string str)
{
	long long res = 0;
	int osn = 0;
	letters.clear();
	letters.resize(255);
	nums.clear();
	nums.resize(255);
	number.clear();
	for (int i = 0; i < (int)str.size(); i++)
	{
		if (!letters[str[i]])
		{
			letters[str[i]] = 1;
			nums[str[i]] = osn++;
		}
	}
	for (int i = 0; i < (int)str.size(); i++)
	{
		int x = nums[str[i]];
		if (x == 1)
		{
			x = 0;
		}
		else
		{
			if (x == 0)
			{
				x = 1;
			}
		}
		number.push_back(x);
	}
	int n = (int)number.size();
	if (osn < 2)
	{
		osn = 2;
	}
	for (int i = 0; i < n; i++)
	{
		res += number[n - i - 1] * (long long)pow((double)osn, (double)i);
	}
	return res;
}

int main()
{
	in >> T;
	for (int t = 0; t < T; t++)
	{
		in >> text;
		out << "Case #" << t + 1 << ": " << solve(text)<< std::endl;
	}
	return 0;
}

