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

#pragma comment(linker, "/stack:10000000")

using namespace std;

long long s[1000000], time[1000001];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		int L, N, C;
		long long t;
		long long a[1000];
		cin >> L >> t >> N >> C;
		for (int i = 0; i < C; ++i)
			cin >> a[i];

		for (int i = 0; i < N; ++i)
			s[i] = a[i % C] * 2;

		time[0] = 0;

		for (int i = 1; i <= N; ++i)
			time[i] = time[i - 1] + s[i - 1];

		multiset<long long> se;

		long long ans = time[N], sum = 0, appr = 0;

		for (int i = N - 1; L > 0 && i >= 0; --i) {
			long long tt = 0;
			if (t - time[i] > 0)
				tt = t - time[i];
			long long ttime = time[i] + min(tt, s[i]) + (s[i] - tt) / 2 + (sum - appr) + appr / 2;
			se.insert(s[i]);
			appr += s[i];
			sum += s[i];
			if (!se.empty() && se.size() >= L) {
				long long dd = *se.begin();
				se.erase(se.begin());
				appr -= dd;
			}
			if (time[i] + s[i] >= t)
				ans = min(ans, ttime);
		}
	
		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}

