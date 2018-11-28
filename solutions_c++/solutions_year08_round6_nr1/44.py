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

string input = "A-large.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

const int inf = 1000000;

set<int> h1, w1;
bool f1;
vector<pair<int, int> > vp;
int hmin, hmax, wmin, wmax;

bool judge(pair<int, int> p)
{
	if (!f1) {
		for (int i = 0; i < vp.size(); i++) {
			if (vp[i] == p) {
				return true;
			}
		}
		return false;
	}
	int hh = p.first, ww = p.second;
	for (int i = 0; i < vp.size(); i++) {
		int h = vp[i].first, w = vp[i].second;
		if (h < hmin) {
			if (w < wmin) {
				if (hh <= h && ww <= w) return true; 
			}
			else if (w <= wmax) {
				if (hh <= h) return true;
			}
			else {
				if (hh <= h && ww >= w) return true;
			}
		}
		else if (h <= hmax) {
			if (w < wmin) {
				if (ww <= w) return true;
			}
			else if (w <= wmax) {
				cerr << "@@" << endl;
			}
			else {
				if (ww >= w) return true;
			}
		}
		else {
			if (w < wmin) {
				if (hh >= h && ww <= w) return true;
			}
			else if (w <= wmax) {
				if (hh >= h) return true;
			}
			else {
				if (hh >= h && ww >= w) return true;
			}
		}
	}
	return false;
}

int main(void)
{
	int re;
	int n, m, h, w;
	string str;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		h1.clear();
		w1.clear();
		vp.clear();

		ifs >> n;
		for (int i = 0; i < n; i++) {
			ifs >> h >> w >> str;
			if (str == "BIRD") {
				h1.insert(h);
				w1.insert(w);
			}
			else {
				ifs >> str;
				vp.push_back(make_pair(h, w));
			}
		}

		// output
		cerr << ri << endl;
		ofs << "Case #" << ri <<": ";
		ofs << endl;

		

		if (h1.empty()) {
			f1 = false;			
		}
		else {
			f1 = true;
			hmin = *h1.begin();
			hmax = *h1.rbegin();
			wmin = *w1.begin();
			wmax = *w1.rbegin();
			/*
			if (h2.empty()) {
				f2 = false;
			}
			else {
				f2 = true;
				set<int>::const_iterator it;

				h2l = w2l = -inf;
				h2r = w2r = inf;
				it = h2.lower_bound(h1min);
				if (it != h2.begin() && *--it < h1min) {
					h2l = *it;
				}
				it = h2.lower_bound(h1max);
				if (it != h2.end() && *it > h1max) {
					h2r = *it;
				}
				it = w2.lower_bound(w1min);
				if (it != w2.begin() && *--it < w1min) {
					w2l = *it;
				}
				it = w2.lower_bound(w1max);
				if (it != w2.end() && *it > w1max) {
					w2r = *it;
				}
			}
			cerr << h1min << "\t" << h1max << "\t" << w1min << "\t" << w1max << endl;
			cerr << h2l << "\t" << h2r << "\t" << w2l << "\t" << w2r << endl;
			*/
		}

		ifs >> m;
		for (int i = 0; i < m; i++) {
			ifs >> h >> w;
			if (f1) {
				if (h >= hmin && h <= hmax && w >= wmin && w <= wmax) {
					ofs << "BIRD\n";
				}
				else if (judge(make_pair(h, w))) {
					ofs << "NOT BIRD\n";
				}
				else {
					ofs << "UNKNOWN\n";
				}
			}
			else {
				if (judge(make_pair(h, w))) {
					ofs << "NOT BIRD\n";
				}
				else {
					ofs << "UNKNOWN\n";
				}
			}
			/*if (f1) {
				if (h >= h1min && h <= h1max && w >= w1min && w <= w1max) {
					ofs << "BIRD\n";
				}
				else if (f2 && (h <= h2l || h >= h2r || w <= w2l || w >= w2r)) {
					ofs << "NOT BIRD\n";
				}
				else {
					ofs << "UNKNOWN\n";
				}
			}
			else {
				if (f2 && (h2.count(h) > 0 && w2.count(w) > 0)) {
					ofs << "NOT BIRD\n";
				}
				else {
					ofs << "UNKNOWN\n";
				}
			}*/
		}

	}

	return 0;
}

