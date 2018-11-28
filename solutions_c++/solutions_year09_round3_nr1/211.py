#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iostream>
#include <sstream>
using namespace std;

char next (char c )
{
	if ( c== '1')
		return '0';
	if ( c== '0')
		return '2';
	if ( c >='2' && c <= '8')
		return (char)(c+1);
	if ( c == '9')
		return 'a';
	return (char)(c+1);
}
long long toDecimal(string s, int base)
{
    long long v, i, result = 0;
    for(i = 0 ; i < s.size() ; i++)
    {
          if(s[i]>='0' && s[i] <= '9')  v = s[i] - '0';
          else v = s[i]-'A'+10;
          result = result*base+v;
    }
    return result;
}
int main ()
{
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small-attempt1.out","wt",stdout);
	int tt;
	cin >> tt;
	string s;
	for ( int t = 1 ; t<=tt ; t++ )
	{
		cin >> s;

		set<char> st;
		for ( int i = 0 ; i < s.size(); i ++)
			st.insert(s[i]);

		int base = st.size();
		if (base <2) base = 2;
		//cout << base << endl;
		map<char,char> mp;
		string nw;
		char c = '1';
		for ( int i = 0; i <s.size() ; i ++)
			if ( mp.find(s[i]) != mp.end())
				nw += mp[s[i]];
			else
			{
				nw += c;
				mp[s[i]] = c;
				c = next (c);
			}

		//cout << nw << endl;
		long long d = toDecimal(nw,base);
		printf("Case #%d: ",t);
		cout << d << endl;
	}
	return 0;
}
