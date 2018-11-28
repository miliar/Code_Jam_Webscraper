#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool is_possible(int num, int& s, int p)
{
	if (num == 0)
		return p == 0;
	if (num % 3 == 0)
	{
		int k = num / 3;
		if (k >= p)
			return true;
		if ( k == p - 1 && s > 0)
		{
			--s;
			return true;
		}
		return false;
	} else if (num % 3 == 1)
	{
		int k = num / 3 + 1;
		if (k >= p)
			return true;
		return false;
	} else if (num % 3 == 2)
	{
		int k = num / 3 + 1;
		if (k >= p)
			return true;
		if ( k == p - 1 && s > 0)
		{
			--s;
			return true;
		}
		return false;
	}
	std::cout << "Error!!!" << std::endl;
	return false;
}

int googlers(vector<int>& v, int s, int p)
{
	int n = v.size();
	int res = 0;
	for (int i = 0; i < v.size(); ++i)
		if (is_possible(v[i], s, p))
			res++;
	return res;
}


int main()
{
	int t;
	ifstream input("input_b.txt");
	ofstream output("output_b.txt");
	input >> t;
	for (int i = 0; i < t; ++i)
	{
		int n, s, p;
		input >> n >> s >> p;
		vector<int> v;
		for (int j = 0; j < n; ++j)
		{
			int tmp;
			input >> tmp;
			v.push_back(tmp);
		}
		output << "Case #" << i + 1 << ": " << googlers(v, s, p) << std::endl;
	}
	input.close();
	output.close();
	return 0;
}