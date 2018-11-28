#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <string>
#include <iterator>
#include <limits>
#include <sstream>
#include <iostream>
#include <stack>
#include <iomanip>

#include <boost/lexical_cast.hpp>
#include <boost/regex.hpp>
#define BOOST_REGEX_DYN_LIB

using namespace std;
using namespace boost;

vector<map<int, bool> > unhappy_nums(11);

int convert_num(int number, int base)
{
	vector<int> result;
	while(number > 0)
	{
		result.push_back(number % base);
		number /= base;
	}
	int res = 0;
	for(int i = result.size()-1; i >= 0; --i)
	{
		res += result[i] * (pow(10, double(i)));
	}
	return res;
}
bool is_happy(int number, int base, vector<int> current)
{
	if(base == 2 || base == 4)
		return true;

	if(unhappy_nums[base][number])
		return false;

	if(find(current.begin(), current.end(), number) != current.end())
	{
		for(int i = 0; i < current.size(); ++i)
		{
			unhappy_nums[base][current[i]] = true;
		}
		return false;
	}

	current.push_back(number);

	stringstream ss;
	ss << number;
	vector<int> digits;
	int sum = 0;
	while(ss.peek() != -1)
	{
		char c_digit;
		ss >> c_digit;
		int digit = lexical_cast<int>(c_digit);
		sum += digit*digit;
	}

	int result = sum;
	if(base != 10)
	{
		result = convert_num(result, base);
	}

	if(result != 1)
	{
		return is_happy(result, base, current);
	}
	return true;
}
int main()
{
	ifstream in("A.in");
	ofstream out("A.out");
	int cases = 0;
	in >> cases;
	in.ignore();

	for(int case_number = 0; case_number < cases; ++case_number)
	{
		vector<int> bases;
		string line;
		getline(in, line);
		stringstream ss;
		ss << line;
		while(ss.peek() != -1)
		{
			int base;
			ss >> base;
			bases.push_back(base);
		}
		for(unsigned int i = 2; i < 100000; ++i)
		{
			bool happy = true;
			for(int j = 0; j < bases.size(); ++j)
			{
				vector<int> current;
				int number = i;
				if(bases[j] != 10)
				{
					number = convert_num(number, bases[j]);
				}
				if(!is_happy(number, bases[j], current))
				{
					happy = false;
					break;
				}
			}
			if(happy)
			{
				out << "Case #" << case_number + 1 << ": " ;
				out << i;
				out << endl;
				break;
			}
		}
	}
}