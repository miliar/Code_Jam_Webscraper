#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn;
	string s;
//	const string mp = "abcdefghijklmnopqrstuvwxyz";
	const string mp = "yhesocvxduiglbkrztnwjpfmaq";
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
	scanf("%d", &tcn);
	getline(cin, s);
	for (int tc = 1; tc <= tcn; tc++)
	{
		getline(cin, s);
		for (int i = 0; i < int(s.size()); ++i)
		{
			if ('a' <= s[i] && s[i] <= 'z')
				s[i] = mp[s[i] - 'a'];
		}
		printf("Case #%d: %s\n", tc, s.c_str());
	}

	return 0;
}
