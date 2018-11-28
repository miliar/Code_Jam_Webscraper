#include <fstream>
#include <string>
#include <set>
#include <cstring>
using namespace std;

int t;
int n, m;
int i, j, k, p, q;
int ans;
set<string> ka;

ifstream cin("A-large.in");
ofstream cout("A-large.out");

int main()
{
	
	string c, nc;
	int len;
	cin >> t;
	for (k = 1; k <= t; k++)
	{
		ka.clear();
		ans = 0;
		cin >> n >> m;
		for (i = 0; i < n; i++)
		{
			cin >> c;
			ka.insert(c);
		}
		for (i = 0; i < m; i++)
		{
			cin >> c;
			len = c.length();
			j = 1;
			while (j < len)
			{
				for (p = j; p < len && c[p] != '/'; p++);
				nc = c.substr(0, p);
				if ( ka.find(nc) == ka.end() )
				{
					ans++;
					ka.insert(nc);
				}
				j = p + 1;
			}
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}