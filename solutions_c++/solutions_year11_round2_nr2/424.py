#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long double INFTY = 1e30;
const long double EPS = 1e-7;

ifstream fin("input");
ofstream fout("output");

bool can(long double t, const vector<int> &a, int d)
{
	long double prev = -INFTY;
	int n = a.size();
	for (int i = 0; i < n; i++) {
		if (prev + d <= a[i]) {
			prev = max(a[i] - t, prev + d);
		}
		else {
			if (a[i] + t < prev + d) {
				return false;
			}
			prev = prev + d;
		}
	}
	return true;
}

void solve()
{
	int c, d;
	fin >> c >> d;
	vector<int> a;
	for (int i = 0; i < c; i++) {
		int x;
		fin >> x;
		int qnt;
		fin >> qnt;
		for (int j = 0; j < qnt; j++) {
			a.push_back(x);
		}
	}
	long double l = 0, r = INFTY;
	while (r - l > EPS) {
		long double t = (l + r) / 2;
		if (can(t, a, d)) {
			r = t;
		}
		else {
			l = t;
		}
	}
	fout << (l + r) / 2 << endl;
}

int main()
{
	int t;
	fin >> t;
	fout.setf(ios::fixed);
	fout.precision(10);
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
