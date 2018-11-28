#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <ctype.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int NMAX = 102;

struct Str
{
	vector <int> ind;
	string name;
};

Str str[NMAX*NMAX];

int main()
{
	int t;
	freopen("test.in", "a+", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;
	int n, m;
	string s, temp;
	for (int i = 0; i < t; ++i)
	{
		memset(str, 0, sizeof(str));

		cin >> n >> m;
		cout << "Case #" << i + 1 << ": ";
		int max_sub = 1;
		int cnt = 0;
		for (int i = 0; i < n; ++i) 
		{
			cin >> s;
			s += "/";
			int lvl = 0;
			for (int j = 1; j < s.size(); ++j)
			{
				if (s[j] != '/')
					temp += s[j];
				else
				{

					bool flag = false;
					for (int k = 0; k < str[lvl].ind.size(); ++k)
					{
						if (str[str[lvl].ind[k]].name == temp)
						{
							flag = true;
							lvl = str[lvl].ind[k];
							break;
						}
					}
					if (!flag)
					{
						str[max_sub].name = temp;
						str[lvl].ind.push_back(max_sub);
						lvl = max_sub;
						++max_sub;
						++cnt;
					}
					temp.clear();
				}
			}
		}

		cnt = 0;
		for (int i = 0; i < m; ++i) 
		{
			cin >> s;
			s += "/";
			int lvl = 0;
			for (int j = 1; j < s.size(); ++j)
			{
				if (s[j] != '/')
					temp += s[j];
				else
				{

					bool flag = false;
					for (int k = 0; k < str[lvl].ind.size(); ++k)
					{
						if (str[str[lvl].ind[k]].name == temp)
						{
							//cout << str[str[lvl].ind[k]].name;
							flag = true;
							lvl = str[lvl].ind[k];
							break;
						}
					}
					if (!flag)
					{
						str[max_sub].name = temp;
						str[lvl].ind.push_back(max_sub);
						lvl = max_sub;
						++max_sub;
						++cnt;
					}
					temp.clear();
				}
			}
		}


		cout << cnt << endl;
	}
	return 0;
}