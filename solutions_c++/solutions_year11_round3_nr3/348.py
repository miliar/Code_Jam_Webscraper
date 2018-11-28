// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		int n, l, h;
		cin >> n >> l >> h;
		int a[10000];
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		cout << "Case #" << test << ": ";
		int ans = -1;
		for (int i = l; i <= h; ++i) {
			int j;
			for (j = 0; j < n; ++j) {
				if (a[j] % i != 0 && i % a[j] != 0)
					break;
			}
			if (j == n) {
				ans = i;
				break;
			}
		}	
		if (ans != -1)
				cout << ans << endl;
			else
				cout << "NO\n";
	}

	return 0;
}

