#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <stack>
#include <queue>
#include <valarray>
#include <cmath>
#include <ctime>
using namespace std;


long long int getNumber(const vector<char>& number, int base)
{
	long long int result = 0;
	int b = 0;
	for(long int i = number.size() -1  ; i >= 0 ; --i)
	{
		result += std::pow((double)base, b) * (number.at(i) - 48);
		b++;
	}
	return result;
}

std::vector<char> generateDictionary(const string& number)
{
	map<char, int> dictionary;
	std::vector<char> result;
	result.resize(number.size());
	int base = 0;
	bool isZeroUsed = false;
	for (int i = 0 ;  i < number.size() ; ++i)
	{
		map<char, int>::iterator found =  dictionary.find(number.at(i));
		if (found != dictionary.end())
		{
			result[i] = found->second;
		}
		else
		{
			if (i == 0 && base == 0)
			{
				result[i] = '1';
				dictionary.insert(make_pair(number.at(i), '1'));
			}
			if (i > 0 && base == 0)
			{
				result[i] = '0';
				dictionary.insert(make_pair(number.at(i), '0'));
				base += 2;
			}
			else
			if (i > 0 && base > 0)
			{
				result[i] = base + 48;
				dictionary.insert(make_pair(number.at(i), base + 48));
				base++;
			}
		}
	}

	return result;
}

int main()
{
	ifstream input("C:\\CodeJam\\in.txt");
	ofstream output("C:\\CodeJam\\out.txt");

	int T;
	input >> T;

	int testCase = 1;
	while(T--)
	{


		std::string number;

		input >> number;

		std::vector<char> result = generateDictionary(number);
		std::valarray<char> valArray(&result[0], result.size());
		int max =  valArray.max() - 47;

		if (max < 2)
		{
			max = 2;
		}

		output << "Case #" << testCase++ << ": " << getNumber(result, max) << std::endl;
	}

	return 0;
}