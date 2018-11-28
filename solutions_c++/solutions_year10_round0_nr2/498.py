#include "stdafx.h"
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <map>
#include <list>
#include <set>
#include <queue>
using namespace std;
#define MAX 1000


class Warning
{
public:
	void execute()
	{
		int n;
		cin >> n;
		int events, people, groups;
		for(int i = 0; i < n; ++i)
		{
			cin >> events;
			vector<long long> numbers;
			for(int j = 0; j < events; ++j)
			{
			   long long a;
			   cin >> a;
			   numbers.push_back(a);		
			}			
			long long result = runCase(numbers);
			numbers.clear();
			cout << "Case #" << i+1 << ": " << result << endl;			
		}
	}

	long long runCase(vector<long long>& numbers)
	{
	   vector<long long> dis;
	   for(int i = 0; i < numbers.size(); ++i)
	   {
		   for(int j = i+1; j < numbers.size(); ++j)
		   {
			   long long r = numbers[i] - numbers[j];
			   if(r < 0)
			   {
				   r = 0-r;
			   }
			   if(r == 0)
			   {
				   continue;
			   }
			   dis.push_back(r);
		   }
	   }

	   long long n;
	   n = dis[0];
	   for(int i = 1; i < dis.size(); ++i)
	   { 
		   n = gcd(n, dis[i]);
	   }

	   long long result = 0;
	   long long max = 0;
	   for(int i = 0; i < numbers.size(); ++i)
	   {
		   if(result < (numbers[i] / n)*n)
		   {
		      max = numbers[i];
			  result = (max / n)*n;
		      if(max % n != 0)
			  {
				  result += n;
			  }
		   }
	   }
	   return result%max;
	}

	long long gcd(long long a, long long b)
	{
		if(a == 0)
		{
			return b;
		}
		else
		{
			long long s =  b < a ? b : a;
			long long l =  b < a ? a : b;
			b = l % s;
			a = s;
			return gcd(b, a);
		}
	}
};

int main()
{ 
    Warning o;
	o.execute();
	int a;
	cin >> a;
}