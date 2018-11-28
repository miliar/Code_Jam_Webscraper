#include <set>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

string getStrLine()
{
	string dummy;
	getline(cin, dummy);
	return dummy;
}

int getIntLine()
{
	int v;
	cin >> v;
	string dummy;
	getline(cin, dummy);
	return v;
}

int getBase(string str)
{
	sort(str.begin(), str.end());
	int b = 1;
	char prev = str[0];
	for (int i=1; i < str.length(); ++i)
	{
		if (str[i] != prev)
		{
			++b;
			prev = str[i];
		}
	}
	if (b == 1) return 2;
	return b;
}
vector<int> assignVal(string str)
{
	vector<int> ret;
	int vals[256];
	for(int i=0; i < 256;++i) vals[i] = -1;
	int mv = 0;
	vals[ str[0] ] = 1;

	for (int i=0; i < str.length(); ++i)
	{
		char v = str[i];
		if (vals[v] != -1)
		{
			ret.push_back( vals[v] );
			continue;
		}
		vals[v] = mv;
		ret.push_back( mv );
		if (mv == 0) mv = 2;
		else ++mv;
	}
	return ret;

}
double getMin(string str)
{
	int b = getBase(str);
	vector<int> vals = assignVal(str);
	double v = 0;
	for (int i=0; i < vals.size(); ++i)
	{
		v = v * b + vals[i];
	}
	return v;
}

int main()
{
	int T = getIntLine();
	for (int i=0; i < T; ++i)
	{
		double res = getMin(getStrLine());
		printf("Case #%d: %.0f\n", i+1, res);
	}
}
