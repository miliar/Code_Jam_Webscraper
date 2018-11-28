#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define mp make_pair
#define fst first
#define sec second

class trains
{
	public:
		vector <int> optimize(int, int, vector <vector<int> >&);
};

int b[402][402];

vector <int> trains::optimize(int n, int m, vector <vector<int> > &a)
{
	int st = a.size(), ee = a.size() + 1;
	memset(b, 0, sizeof(b));
	vector <pair <int, int> > qu;
	for (int i = 0; i < n + m; i++)
	{
		for (int j = 0; j < a[i].size(); j++)
		{
			b[i][a[i][j]] = 1;
			b[a[i][j]][i] = -1;
		}
		b[st][i] = 1;
		b[i + n + m][ee] = 1;
		b[ee][i + n + m] = -1;
	}
	bool q[402];
	while (true)
	{
		qu.clear();
		memset(q, 0, sizeof(q));
		for (int i = 0; i < n + m; i++)
			if (b[st][i] == 1)
			{
				qu.push_back(mp(i, -1));
				q[i] = 1;
			}
		int k = 0;
		while (k < qu.size())
		{
			int x = qu[k].fst;
			if (b[x][ee] == 1)
				break;
			for (int i = 0; i < a[x].size(); i++)
				if (!q[a[x][i]] && b[x][a[x][i]] == 1)
				{
					q[a[x][i]] = true;
					qu.push_back(mp(a[x][i], k));
				}
			k++;
		}
		if (k < qu.size() && b[qu[k].fst][ee] == 1)
		{
			b[qu[k].fst][ee] = -1;
			int lnk = k;
			while (qu[lnk].sec != -1)
			{
				b[qu[lnk].fst][qu[qu[lnk].sec].fst] = 1;
				b[qu[qu[lnk].sec].fst][qu[lnk].fst] = -1;
				lnk = qu[lnk].sec;
			}
			b[st][qu[lnk].fst] = -1;
		}
		else
			break;
	}
	vector <int> ret;
	ret.clear();
	ret.push_back(n);
	ret.push_back(m);
	for (int i = 0; i < n + m; i++)
		if (b[st][i] == -1)
		{
			if (i < n)
				ret[1]--;
			else
				ret[0]--;
		}
	return ret;
}

vector <int> tmp;
int tt[200];
int t2[200];
vector <vector<int> > a;
vector <int> c;

int main()
{
	tmp.clear();
	int n;
	scanf("%d", &n);
	trains x;
	for (int i = 0; i < n; i++)
	{
		int t, na, nb;
		a.clear();
		scanf("%d%d%d", &t, &na, &nb);
		for (int j = 0; j < na; j++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			tt[j] = h * 60 + m;
			scanf("%d:%d", &h, &m);
			t2[j] = h * 60 + m;
			a.push_back(tmp);
			a.push_back(tmp);
		}
		for (int j = 0; j < nb; j++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			tt[na + j] = h * 60 + m;
			scanf("%d:%d", &h, &m);
			t2[na + j] = h * 60 + m;
			a.push_back(tmp);
			a.push_back(tmp);
		}
		for (int j = 0; j < na; j++)
			for (int k = na; k < na + nb; k++)
				if (t2[j] + t <= tt[k])
				{
					a[j].push_back(na + nb + k);
					a[na + nb + k].push_back(j);
				}
				else if (t2[k] + t <= tt[j])
				{
					a[k].push_back(na + nb + j);
					a[na + nb + j].push_back(k);
				}
		c = x.optimize(na, nb, a);
		printf("Case #%d: %d %d\n", i + 1, c[0], c[1]);
	}
	return 0;
}
