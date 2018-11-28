#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int r; scanf("%d", &r);
		map<pii, int> a;
		for(int i = 0; i < r; ++i)
		{
			int lx, ly, ux, uy; scanf("%d%d%d%d", &lx, &ly, &ux, &uy);
			for(int x = lx; x <= ux; ++x)
				for(int y = ly; y <= uy; ++y)
					a[mp(x, y)] = 1;
		}
		int time = 0;
		while(a.size())
		{
			time++;
			map<pii, int> b;
			for(map<pii, int> :: iterator it = a.begin(); it != a.end(); ++it)
			{
				pii w = it->first;
				if(a.count(mp(w.X, w.Y - 1)) || a.count(mp(w.X - 1, w.Y)))
				{
					b[w] = 1;
				}
				if(a.count(mp(w.X - 1, w.Y + 1)))
					b[mp(w.X, w.Y + 1)] = 1;
				if(a.count(mp(w.X + 1, w.Y - 1)))
					b[mp(w.X + 1, w.Y)] = 1;
			}
			/*
			vector<string> e(20, string(20, '.'));
			for(map<pii, int> :: iterator it = b.begin(); it != b.end(); ++it)
				e[it->first.X][it->first.Y] = '#';
			cout << endl;
			for(int i = 0; i < e.size(); ++i)
				cout << e[i] << endl;
			*/
			a = b;
		}
		printf("Case #%d: %d\n", z + 1, time);
	}

	return 0;
}
#endif