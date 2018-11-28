#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

set <string> S;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i,j,n,m,l;
	int T,tt;
	int ans=0;
	string s,t;
	cin >> T;
	for (tt=0; tt<T; ++tt)
	{
		S.clear();
		cin >> n >> m;
		for (i=0; i<n; ++i)
		{
			cin >> s;
			S.insert(s);
		}
		ans=0;
		for (j=0; j<m; ++j)
		{
			cin >> s;
			t="/";
			l=s.length();
			for (i=1; i<=l; ++i)
			{
				if ((i==l || s[i]=='/') && S.find(t)==S.end() )
				{
					ans++;
					S.insert(t);
				}
				if (i<l) t+=s[i];
			}
		}
		cout << "Case #" << tt+1 << ": " << ans <<endl;
	}
	return 0;
}