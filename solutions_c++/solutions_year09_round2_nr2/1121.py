#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()	{
	int tnum;
	cin >> tnum;
	for (int t=1; t<=tnum; t++)	{
		string s;
		cin >> s;
		string c;
		c.push_back('0');
		for (int i=0; i<s.length(); i++)
			c.push_back(s[i]);
		next_permutation(c.begin(),c.end());
		cout << "Case #" << t << ": ";
		for (string::iterator i=c.begin(); i!=c.end(); i++)
			if (i==c.begin() && *i=='0')
				;
			else cout << *i;
		cout << endl;
	}
	return 0;
}