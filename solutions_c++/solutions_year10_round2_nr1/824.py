#include <iostream>
#include <string>
#include <vector>
using namespace std;
int res;
vector<string> directory;
void work(string& dir)
{
	int i, j;
	int n = dir.length();
	for (i = 1; i <= n; i++)
	{
		if (dir[i] == '/' || i == n)
		{
			string s = dir.substr(0, i);
			bool find = false;
			for (j = 0; j < directory.size(); j++)
			{
				int pos = directory[j].find(s, 0);
				if (pos == 0 && (s.length() == directory[j].length() || directory[j][s.length()] == '/'))
				{
					find = true;
					break;
				}
			}
			if (!find)
			{
				res ++;
			}
		}
	}
	directory.push_back(dir);
}
int main()
{
	int i, j, n, m, t, c = 0;
	string dir;
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		res = 0;
		directory.clear();
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; i++)
		{
			cin>>dir;
			directory.push_back(dir);
		}
		for (i = 0; i < m; i++)
		{
			cin>>dir;
			work(dir);
		}
		printf("Case #%d: %d\n", ++c, res);
	}

	return 0;
}
