#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <assert.h>
#include <queue>
using namespace std;

int t,n,m,f,k;

int y[1000][1000];

bool g[20][20];

bool inter(int a, int b) {
	for (int i=0; i<k-1; i++) {
		if (y[a][i] == y[b][i]) return true;
		if (y[a][i+1] == y[b][i+1]) return true;
		if (y[a][i] < y[b][i] && y[a][i+1] > y[b][i+1]) return true;
		if (y[a][i] > y[b][i] && y[a][i+1] < y[b][i+1]) return true;
	}
	return false;
}

int c[1000];
bool u[20];

void color(int v) {
	memset(u, 0, sizeof u);
	for (int i=0; i<n; i++)
		if (g[v][i]) u[ c[i] ] = true;
	c[v] = 1;
	while (u[ c[v] ] == true) c[v]++;
}

bool ca = false;

void paint(int pos, int ma) {
	if (pos == n || ca == true) {
		ca = true;
		return;
	}
	for (c[pos] = 1; c[pos]<=min(pos+1, ma); c[pos]++) {
		bool goo = true;
		for (int i=0; i<n; i++)
			if (g[pos][i] && c[pos] == c[i]) {
				goo=false;
				break;
			}
		if (goo)
			paint(pos+1, ma);
	}
}

bool can(int ma) {
	memset(c, 0, sizeof c);
	ca  = false;
	paint(0, ma);
	return ca;
}

int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("data.out");
	cin >> t;
	for (int T=1; T<=t; T++) {
		cerr << T << endl;
		cin >> n >> k;
		for (int i=0; i<n; i++)
			for (int j=0; j<k; j++)
				cin >> y[i][j];
		memset(g, 0, sizeof g);
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (inter(i,j))
					g[i][j] = g[j][i] = true;

		memset(c, 0, sizeof c);
		for (int i=0; i<n; i++)
			color(i);

		int ma = 0;
		for (int i=0; i<n; i++)
			ma = max(ma, c[i]);

		int l=1, r = ma;
		while (r>l) {
			int m = (l+r)/2;
			if (can(m)) r = m;
			else l = m+1;
		}

		cout << fixed << "Case #" << T << ": " << l << endl;
	}

	return 0;
}