#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int v,i,j,t,k;
string s,c;

int main()
{
	freopen("b.in","rt",stdin);
	freopen("b.out","wt",stdout);
	cin >> t;
	for (v = 1;v<=t;v++)
	{
		cin >> s;
		if (next_permutation(s.begin(),s.end()))
		{
			cout << "Case #" << v << ": " << s << endl;	
			continue;
		}
		k = 0;
		c = "";
		sort(s.begin(),s.end());
		for (i = 0;i<s.length();i++)
			if (s[i] == '0') k++;
		k++;
		for (i = 0;i<s.length();i++)
			if (s[i] != '0')
			{
				if (c == "") 
				{
					c = c+s[i];
					while (k>0)
					{
						c = c+'0';
						k--;
					}
				}
				else c = c+s[i];
			}   		
		cout << "Case #" << v << ": " << c << endl;
	}
	return 0;
}



