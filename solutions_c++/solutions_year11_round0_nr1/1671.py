// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>

using namespace std;

vector<pair<char, int>> a;
vector<int> o, b;
int poso = 1, posb = 1, io = 0, ib = 0;

bool go(int k, int &pos) {
	if (pos > k)
		--pos;
	else if (pos < k)
		++pos;
	else
		return true;
	return false;
}

bool push(int k, int &pos) {
	return go(k, pos);
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	
	for (int test = 1; test <= t; ++test) {
		int n;
		cin >> n;
		int ans = 0;
		a.clear();
		o.clear();
		b.clear();
		poso = posb = 1;
		io = ib = 0;
		for (int i = 0; i < n; ++i) {
			a.push_back(make_pair('\0', 0));
			cin >> a[i].first >> a[i].second;
			if (a[i].first == 'O')
				o.push_back(a[i].second);
			else
				b.push_back(a[i].second);
		}
		for (int k = 0; k < n; ++k) {
			char r = a[k].first;
			int q = a[k].second;
			if (r == 'O') {
				if (ib < b.size())
					go(b[ib], posb);
				++ans;
				while (!push(q, poso)) {
					if (ib < b.size())
						go(b[ib], posb);
					++ans;
				}
				++io;
			} else {
				if (io < o.size())
					go(o[io], poso);
				++ans;
				while (!push(q, posb)) {
					if (io < o.size())
						go(o[io], poso);
					++ans;
				}
				++ib;
			}
		}
		
		cout << "Case #" << test << ": " << ans << '\n';
	}

	return 0;
}

