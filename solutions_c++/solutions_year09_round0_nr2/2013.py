#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <list>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define All(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef vector<vector<int> > vvi;

const int inf = 0x0ffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 10000;

vector<int> us, rank, color;

int w, h;

inline int GetLine(int i, int j)
{
	return i*w + j;
}

inline void MakeSet(int x)
{
	us[x] = x;
	rank[x] = 0;
}

inline int FindSet(int x)
{
	if(us[x] != x)
		us[x] = FindSet(us[x]);
	return us[x];
}

inline void Link(int x, int y)
{
	if(rank[x] > rank[y])
		us[y] = x;
	else
	{
		us[x] = y;
		if(rank[x] == rank[y])
			rank[y]++;
	}
}

inline void Union(int x, int y)
{
	Link(FindSet(x), FindSet(y));
}

vvi Map;

int size;

void DFSVisit(int ui, int uj)
{
	int u = GetLine(ui, uj);
	color[u] = gray;
	vector<pii> dest;
	dest.pb(mp(-1, 0));
	dest.pb(mp(0, -1));
	dest.pb(mp(0, 1));
	dest.pb(mp(	1, 0));
	int v = -1 , vm = Map[ui][uj];
	int vii, vjj;
	for(int k = 0; k < 4; k++)
	{
		int vi = dest[k].first+ui, vj = dest[k].second+uj;
		if(vi >= h || vj >= w || vi < 0 || vj < 0)
			continue;
		if(Map[vi][vj] < vm)
		{
			vm = Map[vi][vj];
			v = GetLine(vi, vj);
			vii = vi;
			vjj = vj;
		}
	}
	if(v != -1)
	{
		if(FindSet(u) != FindSet(v))
				Union(u, v);
		if(color[v] == white)
		{
			DFSVisit(vii, vjj);
		}
	}
	color[u] = black;
}

void DFS()
{
	us.clear();
	us.resize(size);
	rank.clear();
	rank.resize(size);
	color.clear();
	color.resize(size);
	for(int i = 0; i < size; i++)
		MakeSet(i);
	for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++)
			if(color[GetLine(i, j)] == white)
				DFSVisit(i, j);
}



int Solution(int nTest)
{
	Map.clear();
	scanf("%d%d", &h, &w);
	Map.resize(h, vector<int> (w));
	size = w * h;
	for(int i = 0; i < h; i++)
	{
		for(int j = 0; j < w; j++)
		{
			int t;
			scanf("%d", &t);
			Map[i][j] = t;
		}
	}
	DFS();

	vector<vector<char> > res;
	res.resize(h, vector<char> (w));

	char id = 'a';

	map<int, char> mp;

	for(int i = 0; i < h; i++)
	{
		for(int j = 0; j < w; j++)
		{
			int u = GetLine(i, j);
			if(mp.count(FindSet(u)))
				res[i][j] = mp[FindSet(u)];
			else
				res[i][j] = mp[FindSet(u)] = id++;
		}
	}
	printf("Case #%d:\n", nTest + 1);
	for(int i = 0; i < h; i++)
	{
		for(int j = 0; j < w-1; j++)
		{
			printf("%c ", res[i][j]);
		}
		printf("%c\n", res[i][w-1]);
	}

	
	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n = 0;

	scanf("%d", &n);

	for(int i = 0; i < n; i++) Solution(i);

//	while(Solution(n));

	return 0;
}

