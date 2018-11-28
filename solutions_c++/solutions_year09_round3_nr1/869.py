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

vector<int> calc_permutations(vector<char> unique_symbol, vector<char> symbol, int base, bool flag)
{
	vector<int> perms;
	do
	{
		vector<char> temp = symbol;
		int k = 0;
		for(; k < base; ++k)
		{
			for(int i = 0; i < symbol.size(); ++i)
			{
				if(symbol[i] == unique_symbol[k])
				{
					temp[i] = lexical_cast<char>(k);
					if(flag)
					{
						temp[i] = lexical_cast<char>(k+1);
					}
				}
			}
			//replace(temp.begin(), temp.end(), unique_symbol[k], lexical_cast<char>(k));
		}
		if(temp[0] == '0')
			continue;
		int number;
		stringstream ss;
		for(int i = 0; i < temp.size(); ++i)
		{
			ss << temp[i];
		}
		ss >> number; 
		perms.push_back(number);
	} while(next_permutation(unique_symbol.begin(), unique_symbol.end()));
	return perms;
}
int change_base(int number, int base)
{
	stringstream ss;
	ss << number;
	string s;
	ss >> s;

	int result = 0;
	for(int i = 0; i < s.size(); ++i)
	{
		result += lexical_cast<int>(s[i]) * (pow(double(base), double(s.size() - i - 1)));
	}
	return result;
}
int main()
{
	ifstream in("A.in");
	ofstream out("A2.out");
	int cases = 0;
	in >> cases;

	for(int case_number = 0; case_number < cases; ++case_number)
	{
		string number;
		in >> number;
		stringstream ss;
		ss << number;

		vector<char> symbol(number.size());
		int count = 0;
		while(ss.peek() != -1)
		{
			ss >> symbol[count++];
		}

		vector<char> unique_chars = symbol;
		sort(unique_chars.begin(), unique_chars.end());
		vector<char>::iterator it = unique(unique_chars.begin(), unique_chars.end());
		unique_chars.resize(it - unique_chars.begin());
		int base = unique_chars.size();
		bool flag= false;
		if(base == 1)
		{
			flag = true;
			base = 2;
			unique_chars.push_back('%');
		}

		vector<int> permutations = calc_permutations(unique_chars, symbol, base, flag);
		sort(permutations.begin(), permutations.end());
		int result = 1;
		if(permutations.size())
		{
			result = change_base(permutations[0], base);
		}

		out << "Case #" << case_number + 1 << ": " << result << endl ;
	}
}