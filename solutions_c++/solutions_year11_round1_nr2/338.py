#include <iostream>
#include <vector>
#include <list>
#include <cstring>

using namespace std;

static const int maxn = 100;
static const int maxm = 10;
static const int maxd = 10;
static const int maxl = 26;

int n, m;
char d[maxn][maxd + 1];
int dl[maxn];
char l[maxm][maxl + 1];
list<int> cad[maxn];
int score[maxn];

void showscore()
{
	return;
	cerr << endl;
	for (int k = 0; k < n; ++k)
		cerr << d[k] << ' ' << score[k] << endl;
	cerr << endl;
}

void showcad()
{
	return;
	cerr << endl;
	for (int k = 0; k < n; ++k)
	{
		cerr << "cad[" << k << "] = ";
		for (list<int>::iterator iter = cad[k].begin(); iter != cad[k].end(); ++iter)
			cerr << d[*iter] << ", ";
		cerr << " score = " << score[k] << endl;
	}
	cerr << endl;
}

void init()
{
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
	{
		cin >> d[i];
		dl[i] = strlen(d[i]);
	}
	for (int i = 0; i < m; ++i)
		cin >> l[i];
}

bool has(int idx, char c)
{
	for (int i = 0; i < dl[idx]; ++i)
		if (d[idx][i] == c)	return true;
	return false;
}

void solve()
{
	for (int i = 0; i < m; ++i)
	{
		for (int k = 0; k < n; ++k)	score[k] = 0;
		for (int k = 0; k < n; ++k)
		{
			cad[k].clear();
			for (int v = 0; v < n; ++v)
				if (dl[k] == dl[v])
					cad[k].push_back(v);
		}
		for (int j = 0; j < maxl; ++j)
		{
			showcad();
			for (int k = 0; k < n; ++k)
			{
				bool skip = true;
				for (list<int>::iterator iter = cad[k].begin(); iter != cad[k].end(); ++iter)
					if (has(*iter, l[i][j]))
					{
						skip = false;
						break;
					}
				if (skip)	continue;
				if (!has(k, l[i][j]))
				{
					++score[k];
					for (list<int>::iterator iter = cad[k].begin(); iter != cad[k].end(); )
					{
						if (has(*iter, l[i][j]))
							iter = cad[k].erase(iter);
						else
							++iter;
					}
				}
				else
					for (list<int>::iterator iter = cad[k].begin(); iter != cad[k].end(); )
					{
						bool bad = false;
						for (int v = 0; v < dl[k]; ++v)
						{
							if (d[k][v] == l[i][j] && d[k][v] != d[*iter][v])
							{
								bad = true;
								break;
							}
							if (d[*iter][v] == l[i][j] && d[k][v] != d[*iter][v])
							{
								bad = true;
								break;
							}
						}
						if (bad)
							iter = cad[k].erase(iter);
						else
							++iter;
					}
			}
		}
		showscore();
		int best = -1, bestk = 0;
		for (int k = 0; k < n; ++k)
			if (score[k] > best)
			{
				best = score[k];
				bestk = k;
			}
		cout << ' ' << d[bestk];
	}
	cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ":";
		init();
		solve();
	}
	return 0;
}

