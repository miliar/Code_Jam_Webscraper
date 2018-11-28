#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>

using std::vector;
using std::set;
using std::map;
using std::pair;
using std::string;

using std::fstream;
using std::istream;
using std::ostream;
using std::cin;
using std::cout;

using std::sort;
using std::max;
using std::min;
using std::reverse;

typedef long long int64;

int64 VectorToInt(const vector<int> &seq, int base)
{
	int64 ans = 0;
	for (int i = 0; i < seq.size(); ++i)
		ans = ans * base + seq[i];
	return ans;
}

vector<int> IntToVector(int64 n, int base)
{
	int64 tmp_n = n;

	vector<int> result;
	while (tmp_n >= base)
	{
		result.push_back(tmp_n % base);
		tmp_n /= base;
	}
	result.push_back(tmp_n);
	reverse(result.begin(), result.end());

	return result;	
}

int64 NextNumber(int64 number, int base)
{
	vector<int> vec = IntToVector(number, base);

	int64 nextNumber = 0;
	for (int i = 0; i < vec.size(); ++i)
		nextNumber += vec[i]*vec[i];

	return nextNumber;
}

bool IsHappy(int n, const vector<int> &bases)
{
	int64 tmpN = n;

	for (int i = 0; i < bases.size(); ++i)
	{
		tmpN = n;
		set<int64> numbers;
		while (numbers.find(tmpN) == numbers.end())
		{
			numbers.insert(tmpN);
			tmpN = NextNumber(tmpN, bases[i]);
		}
		if (tmpN != 1)
			return false;
	}
	return true;
}

vector<int> GetBases(const string &s)
{
	vector<int> result;

	int point = 0;
	
	while (point < s.size())
	{
		int tmp = 0;
		while ((s[point] != ' ') && (point < s.size()))
		{
			tmp = tmp * 10 + s[point++] - '0';
		}
		result.push_back(tmp);
		++point;
	}
	return result;
}

int main()
{
	fstream input("input.txt", std::ios::in);
	fstream output("output.txt", std::ios::out);
	
	int testsNumber;

	input >> testsNumber;
	char inputLine[100];
	input.getline(inputLine, 100);

	for (int i = 0; i < testsNumber; ++i)
	{
		input.getline(inputLine, 100);
		string s = inputLine;
		vector<int> bases = GetBases(s);

		int number = 2;
		while (!IsHappy(number, bases))
			++number;

		output << "Case #" << (i + 1) << ": " << number << std::endl;
	}

	return 0;
}