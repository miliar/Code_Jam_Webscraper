#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "A-small-attempt0.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

const int dir[4][2] = {
	{0, 1},
	{1, 0},
	{0, -1},
	{-1, 0}
};

// left_buttom
// [x, x + 1], [y, y + 1];
int h[256][256], v[256][256];
int area;
int d, np, p[65536][2];

void doit(char ch)
{
	switch (ch) {
	case 'L': --d; if (d == -1) d = 3; return;
	case 'R': ++d; if (d == 4) d = 0; return;
	default: break;
	}
	p[np][0] = p[np - 1][0] + dir[d][0];
	p[np][1] = p[np - 1][1] + dir[d][1];
	if (dir[d][0] == 0) {
		v[p[np][0]][min(p[np - 1][1], p[np][1])] = 1;
	}
	if (dir[d][1] == 0) {
		h[p[np][1]][min(p[np - 1][0], p[np][0])] = 1;
	}
	++np;
}

int Area(int n, int p[][2])
{
	int s1 = 0, s2 = 0;

	for (int i = 0; i < n; i++) {
		s1 += p[(i + 1) % n][1] * p[i][0];
		s2 += p[(i + 1) % n][1] * p[(i + 2) % n][0];
	}

	return abs(s1 - s2) / 2;
}

bool init(int x, int y)
{
	int c;

	c = 0;
	for (int i = 0; i <= x; i++) {
		if (v[i][y]) {
			++c;
			break;
		}
	}
	for (int i = x + 1; i <= 200; i++) {
		if (v[i][y]) {
			++c;
			break;
		}
	}
	if (c == 2) {
		//cerr << x << "," << y << endl;
		return true;
	}
	c = 0;
	for (int i = 0; i <= y; i++) {
		if (h[i][x]) {
			++c;
			break;
		}
	}
	for (int i = y + 1; i <= 200; i++) {
		if (h[i][x]) {
			++c;
			break;
		}
	}
	if (c == 2) {
		//cerr << x << "-" << y << endl;
		return true;
	}

	return false;
}

int main(void)
{
	int re;
	int l, r;
	string s;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		d = 0;
		p[0][0] = 100;
		p[0][1] = 100;
		np = 1;
		memset(h, 0, sizeof(h));
		memset(v, 0, sizeof(v));
		ifs >> l;
		for (int i = 0; i < l; i++) {
			ifs >> s >> r;
			while (r--) {
				for (unsigned int j = 0; j < s.length(); j++) {
					doit(s[j]);
				}
			}
		}
		// output
		area = Area(np - 1, p);
		cerr << "area = " << area << endl;
		for (int i = 0; i <= 200; i++) {
			for (int j = 0; j <= 200; j++) {
				if (init(i, j)) {
					//cerr << i << " " << j << endl;
					--area;
				}
			}
		}
		cerr << ri << endl;
		ofs << "Case #" << ri <<": " << -area << endl;
	}

	return 0;
}
