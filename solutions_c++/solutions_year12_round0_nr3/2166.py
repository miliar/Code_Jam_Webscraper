#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

std::vector<int> v;

int digit_count(int a)
{
	if (a < 0)
	{
		std::cout << "Error!!!\n";
		return -1;
	}
	if (a < 10)
		return 1;
	if (a < 100)
		return 2;
	if (a < 1000)
		return 3;
	if (a < 10000)
		return 4;
	if (a < 100000)
		return 5;
	if (a < 1000000)
		return 6;
	if (a < 10000000)
		return 7;
	std::cout << "Error!!!\n";
	return -1;
}

int in10(int k)
{
	int res = 1;
	for (int i = 0; i < k; i++)
		res *= 10;
	return res;
}

int mega_func(int a, int b)
{
	int count = 0;
	int d = digit_count(a);
	if (d == 1) return 0;
	std::set<int> s;
	for (int i = a; i < b; ++i)
	{
		s.clear();
		for (int j = 1; j < d; ++j)
		{
			int m = (i % in10(j))*in10(d-j) + i/in10(j);
			if (m > i && m <= b)
			{
				//std::cout << i << " " << m << std::endl;
				s.insert(m);
			}
		}
		count += s.size();
	}
	return count;
}


int main()
{
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");
	int n;
	input >> n;
	int a, b;
	for (int i = 0; i < n; ++i)
	{
		input >> a >> b;
		output << "Case #" << i + 1 << ": " << mega_func(a, b) << std::endl;
	}
	input.close();
	output.close();
	return 0;
}