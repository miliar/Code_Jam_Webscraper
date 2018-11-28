#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int A, B;
string subStr;
set< pair<string,string> > setString;

void reCalc(string a, int inA)
{
	string twoString = a + a;
	int length = a.size();
	stringstream ss;
	int temp;
	for(int i=1; i<a.size(); ++i)
	{
		subStr = twoString.substr(i, length);
		ss << subStr;
		ss >> temp;
		ss.clear();
		if( subStr == a)
			continue;
		if(A<=temp && temp<=B)
		{
			if( inA <= temp )
				setString.insert( make_pair(a, subStr) );
			else
				setString.insert( make_pair(subStr, a) );
		}
	}
}
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int testCase = 0;
	cin >> testCase;

	
	int solve = 0;
	for(int t=1; t<=testCase; ++t)
	{
		cin >> A >> B;
		for( int a=A; a<=B; ++a)
		{
			stringstream ss;
			ss << a;
			reCalc(ss.str(), a);
		}
		printf("Case #%d: %d\n", t, setString.size());
		setString.clear();
	}
	return 0;
}