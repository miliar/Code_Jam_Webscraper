#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

const int MOD = 10009;
const int MAXN = 100;
const int MAXK = 10;

string t;
int k;
vector<string> terms;
int n;
int num[MAXN][26];

void Load()
{
	cin >> t >> k;
	memset(num, 0, sizeof(num));
	string ct = "";
	int i;
	terms.clear();
	for (i = 0; i < t.length(); i++)
	{
		if (t[i] == '+')
		{
			terms.push_back(ct);
			ct = "";
		}
		else ct += t[i];
	}
	terms.push_back(ct);
	scanf("%d", &n);
	for (i = 0; i < n; i++) 
	{
		string cur;
		cin >> cur;
		int j;
		for (j = 0; j < cur.length(); j++)
		{
			num[i][cur[j] - 'a']++;
		}
	}
}

class State
{
public:
	int hv[4];
	void operator=(const State &b)
	{
		memcpy(hv, b.hv, sizeof(hv));
	}
};

int thave[4];
int tp[4];
int nt;

bool operator<(const State &a, const State &b)
{
	int i;
	for (i = 0; i < nt; i++)
	{
		if (a.hv[i] < b.hv[i]) return true;
		if (a.hv[i] > b.hv[i]) return false;
	}
	return false;
}

int res[MAXK];
map<State, int> tres[2];

void CountAdd()
{
	tres[0].clear();
	State bs;
	memset(bs.hv, 0, sizeof(bs.hv));
	tres[0][bs] = 1;
	int i, j, q;
	int t = 0;
	for (i = 0; i < k; i++)
	{
		tres[1 - t].clear();
		map<State, int>::iterator p;
		for (p = tres[t].begin(); p != tres[t].end(); p++)
		{
			for (j = 0; j < n; j++)
			{
				State ns = p->first;
				for (q = 0; q < nt; q++)
				{
					ns.hv[q] += num[j][thave[q]];
				}
				tres[1 - t][ns] += p->second;
			}
		}
		for (p = tres[1 - t].begin(); p != tres[1 - t].end(); p++)
		{
			p->second %= MOD;
			int cur = 1;
			for (q = 0; q < nt; q++)
			{
				int qq;
				for (qq = 0; qq < tp[q]; qq++)
				{
					cur *= p->first.hv[q];
					cur %= MOD;
				}
			}
			cur *= p->second;
			cur %= MOD;
			res[i] += cur;
			res[i] %= MOD;
		}
		t = 1 - t;
	}
}

void Solve()
{
	int i, j;
	memset(res, 0, sizeof(res));
	for (i = 0; i < terms.size(); i++)
	{
		nt = 1;
		thave[0] = terms[i][0] - 'a';
		tp[0] = 1;
		for (j  = 1; j < terms[i].length(); j++)
		{
			if (terms[i][j] - 'a' != thave[nt - 1])
			{
				thave[nt] = terms[i][j] - 'a';
				tp[nt] = 0;
				nt++;
			}
			tp[nt - 1]++;
		}
		//cerr << "Processing term: " << terms[i] << "\n";
		//cerr << "got: ";
		//for (j = 0; j < nt; j++) cerr << "(" << thave[j] << "," << tp[j] << ") ";
		CountAdd();
	}
	for (i = 0; i < k; i++) cout << res[i] << " ";
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		cerr << it << "\n";
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}