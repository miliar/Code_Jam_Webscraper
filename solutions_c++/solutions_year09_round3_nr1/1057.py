#include <iostream>
#include <string>
#include <string.h>
using namespace std;


string t = "0123456789ABCDEF";
int baseKtoDec(string str,int base)
{
	int a = 0;
	for(int i=0;i<str.size();i++)
	{
		for(int j=0;j<t.size();j++)
		{
			if(str[i] == t[j])
			a = a*base + j;
		}
	}
	return a;
}

int main()
{
			char at[123];
	int t;
	cin >> t;
	int z = 1;
	while (z <= t) {
			for (int i = 48 ; i < 123 ; ++i) {
				at[i] = 'X';
			}
		string s;
		cin >> s;
		char ch = s[0];
		at[s[0]] = '1';
		s[0] = '1';
		int i;
		for (i = 1 ; i < s.size() ; ++i) {
			if(at[s[i]] != 'X') {
				s[i] = at[s[i]];
				continue;
			}
			else {
				at[s[i]] = '0';
				s[i] = '0';
				break;
			}
		}
		char j = '2';
		for (int k =  i+1 ; k < s.size() ; ++k) {
			if (at[s[k]] == 'X') {
				at[s[k]] = j;
				s[k] = j;
				j++;
			}
			else {
				s[k] = at[s[k]];
			}
		}
//		cout << s << endl;
	
		int ibase = j-'0';
		cout << "Case #" << z<<": " <<  baseKtoDec(s, ibase) << endl;
		z++;
	}
	
	return 0;
}

			

