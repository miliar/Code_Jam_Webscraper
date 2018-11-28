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


class Park
{
public:
	void execute()
	{
		int n;
		cin >> n;
		int times, people, groups;
		for(int i = 0; i < n; ++i)
		{
			cin >> times >> people >> groups;
			queue<int> numbers;
			int a;
			for(int j = 0; j < groups; ++j)
			{
				cin >> a;
				numbers.push(a);
			}
			long result = runCase(times, people, groups, numbers);
			for(int j = 0; j < groups; ++j)
			{
				numbers.pop();
			}
			cout << "Case #" << i+1 << ": " << result << endl;
		}
	}

	int runCase(int times, int people, int groups, queue<int>& numbers)
	{
	   int ret = 0;
	   for(int i = 0; i < times; ++i)
	   {
		   int cur = 0;
		   for(int j = 0; j < numbers.size(); ++j)
		   {
			   if(numbers.front() + cur <= people)
			   {
				   int a = numbers.front();
				   cur += a;
				   numbers.push(a);
				   numbers.pop();
			   }
			   else
			   {
				   break;
			   }
		   }
		   ret += cur;
	   }
	   return ret;
	}
};

int main()
{ 
    Park o;
	o.execute();
	int a;
	cin >> a;
}
