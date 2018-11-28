#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF = 1000000000;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cerr << test << endl;
		int best = INF;
		int k, n;
		cin >> k;
		string s;
		cin >> s;
		n = s.length();
		vi a(k);
		for (int i = 0; i < k; ++i) a[i] = i;
		do
		{
			string s1 = s;
			for (int i = 0; i < n; i += k)
			{
				for (int j = 0; j < k; ++j)
					s1[i + j] = s[i + a[j]];
			}
			
			int cur = 1;
			for (int i = 1; i < n; ++i)
				if (s1[i - 1] != s1[i])
					cur++;
			best = min(best, cur);
		} while (next_permutation(all(a)));

		printf("Case #%d: %d\n", test, best);
	}

}