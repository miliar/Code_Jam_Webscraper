#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define X first
#define Y second
#define mp make_pair
typedef pair<int, int> pii;
typedef pair<pii, pii> ppp;
vector< pii > at, bt;
vector<bool> ua, ub;
int na, nb, t;
const int maxt = 24 * 60;

void dfs(int u, int q)
{
	if(q == 0) ua[u] = true;
	else	   ub[u] = true;
	if(q == 0) // from A to B
	{
		for(int v = 0; v < nb; ++v)
			if(!ub[v] && at[u].Y + t < maxt && at[u].Y + t <= bt[v].X)
			{
				dfs(v, 1);
				break;
			}
	} else // from B to A
	{
		for(int v = 0; v < na; ++v)
			if(!ua[v] && bt[u].Y + t < maxt && bt[u].Y + t <= at[v].X)
			{
				dfs(v, 0);
				break;
			}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt; cin >> tt;
	for(int z = 1; z <= tt; ++z)
	{
		cin >> t >> na >> nb;
		at.resize(na);
		bt.resize(nb);
		for(int i = 0; i < na; ++i)
		{
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			at[i].X = h1 * 60 + m1;
			at[i].Y = h2 * 60 + m2;
		}
		for(int i = 0; i < nb; ++i)
		{
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			bt[i].X = h1 * 60 + m1;
			bt[i].Y = h2 * 60 + m2;
		}	
		sort(at.begin(), at.end());
		sort(bt.begin(), bt.end());
		ua.clear();
		ub.clear();
		ua.resize(na, 0);
		ub.resize(nb, 0);
		vector< pair<pii, pair<int, int> > > p;
		for(int i = 0; i < na; ++i)
			p.push_back(mp(at[i], mp(0, i)));
		for(int i = 0; i < nb; ++i)
			p.push_back(mp(bt[i], mp(1, i)));
		sort(p.begin(), p.end());
		
		int ca = 0, cb = 0;
		for(int i = 0; i < na + nb; ++i) 
		{
			if(p[i].Y.X == 0 && ua[p[i].Y.Y]) continue;
			if(p[i].Y.X == 1 && ub[p[i].Y.Y]) continue;
			if(p[i].Y.X == 0) ca++;
			else cb++;
			dfs(p[i].Y.Y, p[i].Y.X);
//			dfs(p[i].Y.Y, p[i].Y.X);
		}
		cout << "Case #" << z << ": " << ca << " " << cb << endl;
	}
	return 0;
}


