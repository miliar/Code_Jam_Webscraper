#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;


int n, m;


void Load()
{
	cin >> n >> m;

}

string s;


int nv;

map <string, int> trie[10000];


void Solve()
{
	int ans = 0;
	nv = 0;
	int i, j, v;

	trie[0].clear();


	for (i = 0; i < n+m; i++)
	{
		cin >> s;
		s += "/";
		string cur;
		v = 0;


		cur = "";
		for (j = 1; j < (signed)s.size(); j++)
		{
			if (s[j] != '/')
			{
				cur += s[j];
			}
			else {
				if (trie[v].find(cur) == trie[v].end())
				{
					trie[v][cur] = (++nv);
					trie[nv].clear();
					if (i >= n) ans++;
				}
				v = trie[v][cur];
				cur = "";
			}
		}
	}
	cout << ans << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
