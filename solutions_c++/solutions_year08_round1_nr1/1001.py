// SubRoundA.cpp : Defines the entry point for the console application.
//

#include <string>
#include <vector>

#include <iostream>
#include <sstream>

#include <vector>

#include <algorithm>

using std::string;

using std::cin;
using std::cout;

using std::vector;

class vec
{
public:
	std::vector<long> m_arr;

public:

	long dot(const vec& other) const
	{
		long dot_product = 0;
		vector<long>::const_iterator it;
		vector<long>::const_iterator it2;
		it  = m_arr.begin();
		it2 = other.m_arr.begin();
		for(;it != m_arr.end(); it++,it2++)
		{
			long lval = *it;
			long lval2 = *it2;
			dot_product += lval*lval2;
		}
		return dot_product;
	}


};

class sort_asc
{
public:
	bool operator ()(long a, long b)
	{
		return a < b;
	}
};

class sort_desc
{
public:
	bool operator ()(long a, long b)
	{
		return a > b;
	}
};

int main(int argc, char* argv[])
{
	 long total_cases;

	 long variable_a;// Input A
	 long variable_b;// Input B

	 long degree;// Other

	
	string str_variable_a;       
	string str_variable_b;	

	vec x;
	vec y;

	cin >> total_cases;

	cin.ignore();
	cin.clear();

	for( long i = 1; i <= total_cases; i++)
	{
		x.m_arr.clear();
		y.m_arr.clear();

		cin >> degree;
		cin.ignore();
		cin.clear();

		for( long j = 0; j < degree - 1; j++)
		{
			std::getline(cin,str_variable_a,' ');
			std::istringstream(str_variable_a) >> variable_a;
			x.m_arr.push_back(variable_a);
		}
		
		std::getline(cin,str_variable_b);
		std::istringstream(str_variable_b) >> variable_b;

		x.m_arr.push_back(variable_b);

		for( long k = 0; k < degree - 1; k++)
		{
			std::getline(cin,str_variable_a,' ');
			std::istringstream(str_variable_a) >> variable_a;
			y.m_arr.push_back(variable_a);

		}

		std::getline(cin,str_variable_b);
		std::istringstream(str_variable_b) >> variable_b;

		y.m_arr.push_back(variable_b);

		long dot;

		sort(y.m_arr.begin(),y.m_arr.end(),sort_asc());
		sort(x.m_arr.begin(),x.m_arr.end(),sort_desc());

		dot = y.dot(x);

		cout << "Case #" << i <<": " << (dot) << " " << std::endl;
	}
	return 0;
}


