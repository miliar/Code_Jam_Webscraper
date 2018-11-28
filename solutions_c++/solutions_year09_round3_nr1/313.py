#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>
#include <map>

using namespace std;

#define int64 __int64
const int maxn = 100;
int t;
string s;
map<int, int> mp;
int64 a[maxn];

int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		mp.clear();
		cin >> s;
		for (int i = 0; i < s.length(); i++)
		{
			if (mp.find(s[i]) == mp.end())
				mp[s[i]] = mp.size();
			a[i] = mp[s[i]];
		}
		int64 base = mp.size();
		if (mp.size() == 1)
			base = 2;
		int64 out = 0;
		int64 pw = 1;
		for (int i = s.length() - 1; i >= 0; i--)
		{
			if (a[i] == 0)
				a[i] = 1;
			else
				if (a[i] == 1)
					a[i] = 0;
			out += pw * a[i];
			pw *= base;
		}
		printf("Case #%d: %I64d\n", k, out);
	}
	return 0;
}