#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>

using namespace std;

bool ring, fork, bridge;
int result;

struct Group
{
	int p;
	int rank;
	bool corner[6];
	bool edge[6];
};

int n;
vector<Group> gr(10001);
map<pair<int,int>, int> field;

int find(int x)
{
	if (gr[x].p == x)
	{
		return x;
	}
	else
	{
		gr[x].p = find(gr[x].p);
		return gr[x].p;
	}
}

void unite(int x, int y)
{
	int gx = find(x);
	int gy = find(y);
	if (gx != gy)
	{
		int g;
		if (gr[gx].rank >= gr[gy].rank)
		{
			g = gx;
		}
		else
		{
			g = gy;
		}
		gr[gx].p = g;
		gr[gy].p = g;
		gr[g].rank = gr[gx].rank + gr[gy].rank;
		int cnt = 0;
		for (int i = 0; i < 6; ++i) {
			if (gr[gx].corner[i] || gr[gy].corner[i]) {
				gr[g].corner[i] = true;
				++cnt; } }
		if (cnt > 1) bridge = true;
		cnt = 0;
		for (int i = 0; i < 6; ++i) {
			if (gr[gx].edge[i] || gr[gy].edge[i]) {
				gr[g].edge[i] = true;
				++cnt; } }
		if (cnt > 2) fork = true;
	}
}

int whichCorner(int x, int y)
{
	if (x == 1) {
		if (y == 1) {
			return 0;
		} else if (y == n/2) {
			return 1;
		}
	} else if (x == n/2) {
		if (y == 1) {
			return 2;
		} else if (y == n-1) {
			return 3;
		}
	} else if (x == n-1) {
		if (y == n/2) {
			return 4;
		} else if (y == n-1) {
			return 5;
		}
	}
	return -1;
}

int whichEdge(int x, int y)
{
	if (x == 1 && y != 1 && y != n/2) {
		return 0;
	} else if (y == 1 && x != 1 && x != n/2) {
		return 1;
	} else if (x-y+1 == n/2 && y != 1 && x != n-1) {
		return 2;
	} else if (y-x+1 == n/2 && x != 1 && y != n-1) {
		return 3;
	} else if (x == n-1 && y != n-1 && y != n/2) {
		return 4;
	} else if (y == n-1 && x != n-1 && x != n/2) {
		return 5;
	}
	return -1;
}

int neighbor(int x, int y, int i)
{
	pair<int,int> pr;
	map<pair<int,int>,int>::iterator it;
	switch (i)
	{
	case 0:
		pr = make_pair(x+1,y);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	case 1:
		pr = make_pair(x+1,y+1);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	case 2:
		pr = make_pair(x,y+1);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	case 3:
		pr = make_pair(x-1,y);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	case 4:
		pr = make_pair(x-1,y-1);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	case 5:
		pr = make_pair(x,y-1);
		if ((it = field.find(pr)) == field.end()) {
			return -1;
		} else {
			return it->second;
		}
	default:
		return -1;
	}
}

int neighs[6];

int main()
{
	ifstream fin("b2.txt");
	ofstream fout("b2_sol.txt");

	int t;
	fin >> t;
	for ( int tt = 1; tt <= t; ++tt )
	{
		int s,m,x,y;
		fin >> s >> m;
		n = s*2;

		for (int i = 0; i < m; ++i)
		{
			gr[i].p = i;
			gr[i].rank = 1;
			for (int j = 0; j < 6; ++j)
			{
				gr[i].corner[j] = false;
				gr[i].edge[j] = false;
			}
		}
		ring = fork = bridge = false;
		field.clear();

		for (int i = 0; i < m; ++i)
		{
			fin >> x >> y;
			field[make_pair(x,y)] = i;
			{
				int tmp = whichCorner(x,y);
				if (tmp != -1) gr[i].corner[tmp] = true;
				tmp = whichEdge(x,y);
				if (tmp != -1) gr[i].edge[tmp] = true;
			}

			for (int j = 0; j < 6; ++j) {
				neighs[j] = neighbor(x,y,j);
				if (neighs[j] != -1) neighs[j] = find(neighs[j]);
			}
			for (int j = 0; j < 6; ++j)  { if (neighs[j] != -1) {
				for (int k = j + 2; k < 6; ++k) { if (neighs[j] == neighs[k]) {
					bool ok = false;
					for (int kk = j+1; kk < k; ++kk) if (neighs[kk] == -1) ok = true;
					if (ok) {
						ok = false;
						for (int kk = k+1; kk < 6; ++kk) if (neighs[kk] == -1) ok = true;
						for (int kk = j-1; kk >=0; --kk) if (neighs[kk] == -1) ok = true;
						if (ok) ring = true;
					}
				} }
			} }

			for (int j = 0; j < 6; ++j) if (neighs[j] != -1) unite(i,neighs[j]);

			if (ring || bridge || fork)
			{
				for (int ii = i+1; ii < m; ++ii) fin >> x >> y;
				result = i + 1;
				break;
			}
		}

		fout <<"Case #" << tt << ": ";
		if (bridge) {
			if (fork) {
				if (ring) {
					fout << "bridge-fork-ring in move " << result;
				} else {
					fout << "bridge-fork in move " << result;
				}
			} else {
				if (ring) {
					fout << "bridge-ring in move " << result;
				} else {
					fout << "bridge in move " << result;
				}
			}
		} else {
			if (fork) {
				if (ring) {
					fout << "fork-ring in move " << result;
				} else {
					fout << "fork in move " << result;
				}
			} else {
				if (ring) {
					fout << "ring in move " << result;
				} else {
					fout << "none";
				}
			}
		}
		fout << "\n";
	}

	fin.close();
	fout.close();
}