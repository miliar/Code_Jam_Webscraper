#include <fstream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <memory.h>
using namespace std;


string col[30];
int a[30];
int b[30];

int n;

void Load()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> col[i] >> a[i] >> b[i];
	}
}


int was[30];

vector <string> cols;



vector <pair <int, int> > ev;

void Solve()
{
	int m;
	int i, j, k, f, cnt;
	int bst = -1;
	for (m = 0; m < (1 << n); m++)
	{
		cnt = 0;
		for (j = 0; j < n; j++)
			if ((m & (1 << j)) == 0) was[j] = 0; else { was[j] = 1; cnt++;}
		cols.clear();
		for (i = 0; i < n; i++)
			if (was[i] == 1) cols.push_back(col[i]);
		if (cols.size() == 0) continue;
		sort(cols.begin(), cols.end());
		cols.erase(unique(cols.begin(), cols.end()), cols.end());
		if (cols.size() > 3) continue;
		ev.clear();
		for (i = 0; i < n; i++)
			if (was[i] == 1)
			{
				ev.push_back(make_pair(a[i],-1)), ev.push_back(make_pair(b[i]+1,1));
			}
		sort(ev.begin(), ev.end());
		f = 1;
		if (ev[0].first > 1 || ev.back().first < 10001) f = 0;
		j = 0;
		for (i = 0; i < ev.size(); i++)
		{
			j += ev[i].second;
			if (j == 0 && i+1 < ev.size())
				f = 0;	
		}
		if (f)
		{
			if (bst == -1 || bst > cnt) bst = cnt;
		}
		    
	}
	if (bst == -1) cout << "IMPOSSIBLE\n";
	else cout << bst << "\n";

}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int tt = 0;
	int nt;
	cin >> nt;
    for (tt = 1; tt <= nt; tt++)
    {
		Load();
		cout << "Case #" << tt << ": ";
    	Solve();
    }
	return 0;
}

