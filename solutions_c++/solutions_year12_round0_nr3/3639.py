#include <iostream>
#include <algorithm>
#include <string.h>
#include <cstdlib>
#include <sstream>
using namespace std;

bool rec(int x, int y)
{
	ostringstream one;
	one << x;
	string a = one.str();
	
	ostringstream two;
	two << y;
	string b = two.str();
	
	// cout << "HERE " << a << " " << b << endl;
	
	if(a.size() != b.size())
		return false;
		
	for(int i = 0; i < a.size(); i ++)
	{
		string tmp = a.substr(i) + a.substr(0, i);
		if(tmp == b)
			return true;
	}
	return false;
}

int t, a, b;

int main()
{
	cin >> t;
	for(int cas = 1; cas <= t; cas ++)
	{
		int res = 0;
		cin >> a >> b;
		for(int i = a; i <= b; i ++)
		{
			for(int j = i+1; j <= b; j ++)
			{
				if(rec(i, j))
					res ++;
			}
		}
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}