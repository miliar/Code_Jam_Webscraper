/*
 * recycle.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: labrus
 */

#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>


using namespace std;

bool less_than(const string& x, int cut, int num_digits) // tests if x < xcut
{
	for(int i = 0; i < num_digits; i++)
	{
		int cut_pos = (i+cut) % num_digits;
		if(x[i] < x[cut_pos])
		{
			return true;
		}
		else if(x[i] > x[cut_pos])
		{
			return false;
		}
	}
	return false;
}

bool greater_than(const string& y, const string& x, int cut, int num_digits) // tests if y > xcut
{
	for(int i = 0; i < num_digits; i++)
	{
		int cut_pos = (i+cut) % num_digits;
		if(y[i] > x[cut_pos])
		{
			return true;
		}
		else if(y[i] < x[cut_pos])
		{
			return false;
		}
	}
	return true;
}

int compute_period(const string& x, int num_digits)
{
	int periods[] = {2,3};
	for(int k = 0; k < 2; k++)
	{
		int p = periods[k];
		if(num_digits % p != 0)
		{
			break;
		}
		bool is_periodic = true;
		for(int i = 0; i < p; i++)
		{
			for(int j = 0; j < num_digits/p - 1; j++)
			{
				if(x[j*p+i] != x[(j+1)*p+i])
				{
					is_periodic = false;
					break;
				}
			}
			if(!is_periodic)
			{
				break;
			}
		}
		if(is_periodic)
		{
			return p;
		}
	}
	return num_digits;
}


int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		string num1, num2;
		int n1, n2;
		cin >> num1;
		cin >> num2;
		int num_digits = num1.length();
		bool check_periodic = num_digits == 4 || num_digits == 6;
		n1 = atoi(num1.c_str());
		n2 = atoi(num2.c_str());
		int count = 0;
		for(int j = n1; j <= n2; j++)
		{
			stringstream ss;
			ss << j;
			string num;
			ss >> num;
			//cout << num << "(";
			int period = num.length();
			if(check_periodic)
			{
				period = compute_period(num, num_digits);
				//cout << "period = " << period << endl;
			}
			for(int cut = 1; cut < period; cut++)
			{
				if(less_than(num, cut, num_digits) && greater_than(num2, num, cut, num_digits)) // the original is less than the cut one.
				{
				//	cout << cut << " ";
					count++;
				}
			}
			//cout << ") ";
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
