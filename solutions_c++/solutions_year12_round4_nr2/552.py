#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

struct unit
{
	double x, y;
	int index;
	int r;
	unit(int index, int r) : x(0), y(0), index(index), r(r) { }
};

bool operator < (const unit& l, const unit& r) {
	return l.r > r.r;
}

int gw;
int gl;

double sq_dist(double x1, double y1, double x2, double y2)
{
	return (x2-x1)*(x2-x1) + (y2-y1) * (y2-y1);
}

bool okay(vector<unit>& r, int n, double x, double y, int rad)
{
	for (int i = 0; i < n; i++) {
		if (sq_dist(r[i].x, r[i].y, x, y) < (ll)(r[i].r + rad) * (r[i].r + rad))
			return false;
	}

	r[n].x = x;
	r[n].y = y;
	return true;
}

double random_c(int max)
{
	return (double)rand() / RAND_MAX * max;
}

bool try_random(vector<unit>& gr, int c)
{
	if (c == gr.size())
		return true;
	
	for (int i = 0; i < 1000; i++) {
		if (okay(gr, c, random_c(gw), random_c(gl), gr[c].r) && try_random(gr, c+1))
			return true;
	}
	return false;
}

void solve(int W, int L, vector<unit>& r)
{
	gw = W;
	gl = L;
	int start = -1;

	sort(r.begin(), r.end());
	r[0].x = 0.0; r[0].y = 0.0;
	for (int i = 1; i < r.size(); i++) {
		if (okay(r, i, gw, 0, r[i].r))
			continue;
		if (okay(r, i, 0, gl, r[i].r))
			continue;
		if (okay(r, i, gw, gl, r[i].r))
			continue;
		start = i;
		break;
	}

	if (start < 0)
		return;

	assert(try_random(r, start));
}

int main(int argc, const char* argv[])
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int N, W, L;
		vector<unit> r;
		cin >> N >> W >> L;
		for (int i = 0; i < N; i++) {
			int t;
			cin >> t;
			r.push_back(unit(i, t));
		}
		cout << "Case #" << c << ": ";
		solve(W, L, r);
		cout.precision(12);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (r[j].index == i) {
					cout << r[j].x << ' ' << r[j].y << ' ';
					break;
				}
		cout << endl;
	}
    return 0;
}
