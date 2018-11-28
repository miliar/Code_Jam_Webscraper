#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	long long mod = 210;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		string s;
		cin >> s;
		int n = s.length();
		vector<int> d(n);
		for (int j = 0; j < n; j++)
			d[j] = s[j] - '0';
		vector<vector<int> > val = vector<vector<int> >(n, vector<int>(n));
		for (int j = 0; j < n; j++)
			val[j][j] = d[j];
		for (int len = 2; len <= n; len++) {
			int l = 0, r = len-1;
			while (r<n) {
				val[l][r] = (val[l][r-1] * 10 + d[r]) % mod;
				l++;
				r++;
			}
		}
		vector<vector<long long> > a = vector<vector<long long> >(n, vector<long long>(mod));
		a[0][d[0]]++;
		for (int j = 1; j < n; j++) {
			a[j][val[0][j]]++;
			for (int k = 1; k <= j; k++) {                    
				int y = val[k][j];
				for (int x = 0; x < mod; x++) {
					a[j][(x + y) % mod] += a[k - 1][x];
					a[j][(x - y + mod) % mod] += a[k - 1][x];
				}                    
			}
		}
		long long res = 0;
		for (int j = 0; j < mod; j++)
			if (j % 2 == 0 || j % 3 == 0 || j % 5 == 0 || j % 7 == 0)
				res += a[n - 1][j];
		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}
