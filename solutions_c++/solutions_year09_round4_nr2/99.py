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
#include <cmath>
#include <cstdlib>
#include <assert.h>
#include <queue>
using namespace std;

const string diez = "#################################################################################";

int t,n,m,f;
string s[1000];

int d[100][100];
bool fr[100][100];
struct pp {
	int x,y,l;
};
bool operator < (const pp &a, const  pp &b) {
	return a.l > b.l;
}

priority_queue<pp> Q;

const int mm = 10;

typedef set< pair<int, int> > se;

se used[mm];

void addq(int x, int y, int l ) {
	if (fr[x][y] == true) return;
	if (d[x][y] <= l) return;
	d[x][y] = l;
	pp p; p.x= x; p.y = y; p.l = l;
	Q.push(p);
}

int ok(int x, int y) {
	return (x>=0 && y>=0 && x<n && y<m);
}

bool goodp(int x, int y, int v, int d) {
	int X = x-v;
	for (int i=0; i<=v+1; i++)
		if (!ok(X, y+d*i) || s[X][ y+d*i]=='#') return false;
	for (int i=1; i<=v+1; i++)
		for (int j=0; j<=v+2-i; j++)
			if (!ok(X+i, y+d*i) || s[X+i][y+d*i]!='#') return false;
	return true;
}

bool good(int x, int y, int v) {
	return goodp(x, y, v, 1) || goodp(x, y, v, -1);
}
int Ans = 100000;

int kk[60][60][61*61/2];
const int mcnt = 10;
void find(int x, int y, int d, int pr) {
	if (kk[x][y][d] > mcnt) return;
	if (d >= Ans) return;
	if (x == n-1) {
		if (d < Ans) Ans = d;
		return;
	}
	if (s[x+1][y]=='.') {
		int fall = 0;
		while (s[x+1][y]=='.') {
			fall++;
			x++;
		}
		if (fall > f) return;
		find(x, y, d, 0);
		return;
	}
	if (ok(x, y+1) && s[x][y+1] == '.' && pr!=1)
		find(x, y+1, d, 2);
	if (ok(x, y-1) && s[x][y-1] == '.' && pr!=2)
		find(x, y-1, d, 1);
	if (ok(x, y-1) && s[x][y-1] == '.')
		if (ok(x+1, y-1) && s[x+1][y-1] == '#') {
			s[x+1][y-1]='.';
			find(x, y, d+1, 0);
			s[x+1][y-1]='#';
		}
	if (ok(x, y+1) && s[x][y+1] == '.')
		if (ok(x+1, y+1) && s[x+1][y+1] == '#') {
			s[x+1][y+1]='.';
			find(x, y, d+1, 0);
			s[x+1][y+1]='#';
		}
}

int main()
{
	ifstream cin("data.in");
	ofstream cout("data.out");
	cin >> t;
	for (int T=1; T<=t; T++) {
		cerr << T << endl;
		cin >> n >> m >> f;
		for (int i=0; i<n; i++)
			cin >> s[i];
		s[n] = diez;
		/*memset(fr, 0, sizeof fr);
		memset(d, 10, sizeof d);
		used.clear();
		addq(0, 0, 0);
		while (!Q.empty()) {
			pp p = Q.top();
			Q.pop();
			if (d[p.x][p.y] < p.l) continue;
			if (fr[p.x][p.y] == true) continue;
			fr[p.x][p.y] = true;
			if (s[p.x+1][p.y] == '.') {
				int fall = 0;
				if (s[p.x][p.y] == '#') fall++;
				while (s[p.x+1][p.y] == '.') { p.x++; fall++; }
				if (fall > f) continue;
				addq(p.x, p.y, p.l);
				continue;
			}
			if (ok(p.x, p.y+1) && s[p.x][p.y+1] == '.')
				addq(p.x, p.y+1, p.l);
			if (ok(p.x, p.y-1) && s[p.x][p.y-1] == '.')
				addq(p.x, p.y-1, p.l);
			int X = p.x, v = 0;
			while (ok(X, p.y) && s[X][p.y] == '#') { X--; v++; }
			if (good(p.x, p.y, v)) 
				addq(p.x+1, p.y, p.l+(v+1));
		}
		int ans = 100000000;
		for (int i=0; i<m; i++)
			if (fr[n-1][i] == true && d[n-1][i] < ans) ans = d[n-1][i];*/
		Ans = 100000000;
		memset(kk, 0, sizeof kk);
		find(0, 0, 0, 0);
		if (Ans >= 100000000)
			cout << "Case #" << T << ": " << "No" << endl;
		else
			cout << "Case #" << T << ": " << "Yes " << Ans << endl;
	}

	return 0;
}