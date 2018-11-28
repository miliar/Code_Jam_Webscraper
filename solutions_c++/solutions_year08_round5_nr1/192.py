#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

vector<pair<int, int> > points;

void nextf(int&x, int&y, int dir)
{
	if (dir == 0) { y++; }
	else if (dir == 1) { x++; }
	else if (dir == 2) { y--; }
	else { x--; }
}

bool valid(int x, int y)
{
	int left = 0;
	int right = 0;
	int bottom = 0;
	int top = 0;

	for (int i=0; i<points.size()-1; ++i) {
		int sx = points[i].first;
		int sy = points[i].second;
		int ex = points[i+1].first;
		int ey = points[i+1].second;

		if (sx == ex) {
			if (y>min(sy,ey) && y<max(sy,ey)) {
				if (x > sx) left++;
				else right++;
			}
		} else {
			if (x>min(sx,ex) && x<max(sx,ex)) {
				if (y > sy) bottom++;
				else top++;
			}
		}
	}

	bool ans = (right&1)==0 && (left&&right || bottom&&top);

	/*
	if (ans) {
		cout << x << ' ' << y << ":" << endl;
		cout << left << ' ' << right << ' ' << top << ' ' << bottom << endl;
	}
	*/

	return ans;
}

int calc()
{
	int mx = 1000000;
	int my = 1000000;
	int Mx = -1000000;
	int My = -1000000;

	int i, j;

	for (i=0; i<points.size(); ++i) {
		if (points[i].first < mx) mx = points[i].first;
		if (points[i].second < my) my = points[i].second;
		if (points[i].first > Mx) Mx = points[i].first;
		if (points[i].second > My) My = points[i].second;
	}

	for (i=0; i<points.size(); ++i) {
		points[i].first -= mx;
		points[i].second -= my;

		points[i].first *= 2;
		points[i].second *= 2;
	}

	/*
	for (i=0; i<points.size(); ++i) {
		cout << points[i].first << ' ' << points[i].second << endl;
	}
	cout << endl;
	*/


	Mx -= mx;
	My -= my;

	Mx *= 2;
	My *= 2;

	int ans = 0;

	//cout << Mx << ' ' << My << endl;

	for (i=1; i<Mx; i+=2) for (j=1; j<My; j+=2) {
		if (valid(i, j)) ans++;
	}

	return ans;
}

int main(void)
{
	int N;
	cin >> N;
	for (int i=1; i<=N; ++i) {
		points.clear();
		int L;
		cin >> L;

		int x = 0;
		int y = 0;
		int dir = 0;
		points.push_back(make_pair(0,0));

		for (int j=0; j<L; ++j) {
			string s;
			int t;
			cin >> s >> t;

			for (int k=0; k<t; ++k) {
				for (int kk=0; kk<s.length(); ++kk) {
					char ch = s[kk];
					if (ch == 'F')  {
						nextf(x, y, dir);
					} else if (ch == 'L') {
						points.push_back(make_pair(x,y));
						dir = (dir+3) % 4;
					} else {
						points.push_back(make_pair(x,y));
						dir = (dir+1) % 4;
					}
				}
			}
		}


		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}
