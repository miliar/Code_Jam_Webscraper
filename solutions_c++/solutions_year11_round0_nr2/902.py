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
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

string comb[50], op[50];
string s;
vector <char> t;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, tt;
	scanf("%d", &T);
	for (tt=0; tt<T; ++tt)
	{
		int c, d, n;
		int i, j, u;
		scanf("%d", &c);
		for (i=0; i<c; ++i)
			cin >> comb[i];
		scanf("%d", &d);
		for (i=0; i<d; ++i)
			cin >> op[i];
		scanf("%d", &n);
		cin >> s;
		t.clear();
		for (i=0; i<n; ++i)
		{
			for (j=0; j<c; ++j)
				if ((s[i]==comb[j][0] && t.size()>0 && t.back()==comb[j][1]) ||
					(s[i]==comb[j][1] && t.size()>0 && t.back()==comb[j][0]))
				{
					t.pop_back();
					t.push_back(comb[j][2]);
					break;
				}
			if (j<c)
				continue;
			if (t.size()==0)
			{
				t.push_back(s[i]);
				continue;
			}
			for (j=0; j<t.size(); ++j)
			{
				for (u=0; u<d; ++u)
					if ((op[u][0]==t[j] && op[u][1]==s[i]) ||
						(op[u][1]==t[j] && op[u][0]==s[i]))
					{
						t.clear();
						break;
					}
				if (u<d)
					break;
			}
			if (t.size()!=0)
				t.push_back(s[i]);
		}
		printf("Case #%d: ", tt+1);
		if (t.size()>0)
		{
			printf("[%c", t[0]);
			for (i=1; i<t.size(); ++i)
				printf(", %c", t[i]);
			printf("]\n");
		}
		else
		{
			printf("[]\n");
		}
	}
	return 0;
}