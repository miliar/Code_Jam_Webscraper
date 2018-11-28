#include <iostream>
#include <string>
#include <set>

using namespace std;


string s;
set<string> S;


int add(string & s)
{
	int res = 0;
	int len = s.size();
	for(int k = 1; k <= len; k++)
	{
		if(k == len || s[k] == '/')
		{
			string s1 = s.substr(0,k);
			if(S.count(s1) == 0)
			{
				res++;
				S.insert(s1);
			}
		}
	}
	return res;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
		S.clear();
		int n, m;
		cin >> n >> m;
		printf("Case #%d: ", i + 1);
		int res = 0;
		for(int j = 0; j < n; j++)
		{
			cin >> s;
			add(s);
		}
		for(int j = 0; j < m; j++)
		{
			cin >> s;
			res += add(s);
		}
		printf("%d", res);
		printf("\n");
	}
	return 0;
}