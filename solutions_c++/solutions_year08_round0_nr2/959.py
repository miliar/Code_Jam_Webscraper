#include <iostream>
#include <sstream>
#include <string>
using namespace std;

const int maxn = 500;
int n;
int cnt[3], ans[3];

struct pnode
{
	int t, p;
} node[maxn];

void add(int _t, int _p)
{
	node[n].t = _t;
	node[n].p = _p;
	n ++;
}

int trans(string s)
{
	stringstream tmp; tmp.clear();
	tmp << s.substr(0, 2) << " " << s.substr(3, 2);
	int x, y;
	tmp >> x >> y;
	return x * 60 + y;
}

bool cpr(const pnode &a, const pnode &b)
{
	if (a.t != b.t) return a.t < b.t;
	else return a.p < b.p;
}

int main()
{
	int tCase;
	cin >> tCase;
	for (int nCase = 1; nCase <= tCase; nCase ++)
	{
		int T;
		cin >> T;
		int NA, NB;
		cin >> NA >> NB;
		n = 0;
		for (int i = 0; i < NA; i ++)
		{
			string s1, s2;
			cin >> s1 >> s2;
			add(trans(s1), 1);
			add(trans(s2) + T, -2);
		}
		for (int i = 0; i < NB; i ++)
		{
			string s1, s2;
			cin >> s1 >> s2;
			add(trans(s1), 2);
			add(trans(s2) + T, -1);
		}
		sort(node, node + n, cpr);
		cnt[1] = cnt[2] = ans[1] = ans[2] = 0;
		for (int i = 0; i < n; i ++)
		{
			int tp = node[i].p;
			if (tp > 0)
			{
				if (cnt[tp] == 0)
				{
					ans[tp] ++;
					cnt[tp] ++;
				}
				cnt[tp] --;
			}
			else
				cnt[-tp] ++;
		}
		cout << "Case #" << nCase << ": " << ans[1] << " " << ans[2] << endl;
	}
}
