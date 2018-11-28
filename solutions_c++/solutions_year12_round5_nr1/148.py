#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int n;
vector<int> l, p;

vector<pair<long double, int> > a;

void Load()
{
	cin >> n;
	int i;
	l.resize(n); p.resize(n);
	for (i = 0; i < n; i++)
		cin >> l[i];
	for (i = 0; i < n; i++)
		cin >> p[i];
	a.clear();
}

void Solve()
{
	int i;
	for (i = 0; i < n; i++) {
		long double r;
		if (p[i] == 0) {
			r = 1e60;
		} else r = l[i]*100.0 / p[i];
		a.push_back(make_pair(r, i));
	}
	sort(a.begin(), a.end());
	for (i = 0; i < n; i++)
		cout << a[i].second << ' ';
	cout << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
