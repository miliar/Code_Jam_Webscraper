#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <math.h>
#include <map>

using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	#endif
	
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
	string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
	
	map<char, char> m;
	
	for (unsigned int i = 0; i < s1.length(); i++)
	{
		m[s1[i]] = s2[i];
	}
	
	int n;
	char s[111];
	cin >> n;
	gets(s);
	
	for (int i = 0; i < n; i++)
	{
		gets(s);
		cout << "Case #" << i+1 << ": ";
		int mm = strlen(s);
		for (int j = 0; j < mm; j++)
		{
			cout << m[s[j]];
		}
		cout << endl;
	}
	
	return 0;
}