#include <iostream>
#include <string>
#include <map>
using namespace std;
map<string, bool> created;
int addDir(string s)
{
	int cnt = 0;
	while (s.length() > 0 && !created[s])
	{
		created[s] = true;
		++cnt;
		while (s[s.length()-1] != '/')
			s.erase(s.length()-1);
		s.erase(s.length()-1);
	}
	return cnt;
}
int main()
{
	int testCnt;
	cin >> testCnt;
	for (int T = 1; T <= testCnt; ++T)
	{
		int n, m;
		cin >> n >> m;
		created.clear();
		for (int i = 0; i < n; ++i)
		{
			string s;
			cin >> s;
			addDir(s);
		}
		int res = 0;
		for (int i = 0; i < m; ++i)
		{
			string s;
			cin >> s;
			res += addDir(s);
		}
		cout << "Case #" << T << ": " << res << endl;
	}
	return 0;
}