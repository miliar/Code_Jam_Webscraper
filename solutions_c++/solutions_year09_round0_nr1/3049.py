#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef set<string> SS;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef set<char> SC;
#define si(n) scanf("%d", &n)
#define ss(s) scanf("%s", s)

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int l, d, n;
	si(l);
	si(d);
	si(n);
	VS words;
	char s[10000];
	for(int i=0; i<d; i++)
	{
		ss(s);
		words.push_back(s);
	}
	for(int t=0; t<n; t++)
	{
		VB ok(words.size(), true);
		ss(s);
		int p = 0;
		for(int i=0; i<l; i++)
		{
			SC chars;
			if (s[p] == '(')
			{
				p++;
				while(s[p]!=')')
				{
					if (s[p]!=')')
					{
						//cout << s[p];
						chars.insert(s[p]);
					}
					p++;
				}
				p++;
				//cout << endl;
			}
			else
			{
				chars.insert(s[p]);
				//cout << s[p] << endl;
				p++;
			}
			for(int j=0; j<d; j++)
				if (chars.find(words[j][i]) == chars.end())
					ok[j] = false;
		}
		int count = 0;
		for(int i=0; i<ok.size(); i++)
			if (ok[i])
				count++;
		printf("Case #%d: %d\n", t+1, count);
	}
	return 0;
}