#include <iostream>
#include <set>
#include <vector>
#include <string>


using namespace std;


set<string> dirs;
string s;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; test++)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		dirs.clear();
		for(int i = 0; i < n; i++)
		{
			cin >> s;
			s = s + '/';
			for(int j = 0; j < s.length(); j++)
			{
				if(s[j] == '/')
					dirs.insert(s.substr(0, j));
			}
		}
		int ans = 0;
		for(int j = 0; j < m; j++)
		{
			cin >> s;
			s = s + '/';
			int x = 0;
			int max = -1;
			for(int j = 0; j < s.length(); j++)
			{
				if(s[j] == '/')
				{
					if(dirs.count(s.substr(0, j)) != 0)
					{
						max = x;
					}
					x++;
					dirs.insert(s.substr(0, j));
				}
			}
			if(max == -1)
				ans += x - 1;
			else
				ans += x - max - 1;
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}
}