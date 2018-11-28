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
using namespace std;
#define MAX 1000


class Snapper
{
public:
	void execute()
	{
		int n;
		cin >> n;
		int snappers, times;
		for(int i = 0; i < n; ++i)
		{
			cin >> snappers >> times;		
			string ret = runCase(snappers, times);
			cout << "Case #" << i+1 << ": " << ret << endl;
		}
	}

	string runCase(int snappers, int times)
	{
	   int n = 1 << snappers;
	   if((times+1)%n == 0)
	   {
		   return "ON";
	   }
	   else
	   {
		   return "OFF";
	   }
	}
};

int main()
{ 
    Snapper o;
	o.execute();
	int a;
	cin >> a;
}
