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

	int test;
	cin >> test;
	int sc[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384 };
	for (int tt = 0; tt < test; ++tt) {
		int k;
		cin >> k;
		string s;
		cin >> s;
		vector<int> v;
		for (int i = 0; i < k; ++i)
			v.push_back(i);
		int ans = 1000000000;
		do {
			string t = s.substr(0, k), tt;
			for (int j = 0; j < s.length() / k; ++j) {
				for (int l = 0; l < k; ++l) {
					t[l] = s[k * j + v[l]];
				}
				tt += t;
			}
			int tek = 1;
			for (int i = 1; i < tt.length(); ++i) {
				if (tt[i] != tt[i - 1])
					++tek;
			}
			ans = min(ans, tek);
		} while (next_permutation(v.begin(), v.end()));
		/*int m, n;
		cin >> m >> n;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				for (int k = 0; k < 
			}*/
		/*cin >> m >> v;
		int i;
		for (i = 0; sc[i] < m; ++i);
		n = sc[i];
		int ch[100], val[100] ty[100];
		for (int i = 0; i < m; ++i) {
			cin << ty[i] << ch[i];
		}
		for (int i = 0; i < n - m; ++i) {
			cin << val[i];
		}
		for (int i = 0; i < 1 << m; ++i) {
			bool f = true;
			for (int j = 0; j < m; ++j) {
				if ((1 << j) & i) {
					if (!ch[j]) {
						f = false;
						break;
					}
				}
			}
			if (!f)
				continue;

		}*/
		
		cout << "Case #" << tt+1 << ": " << ans << endl;
	}

	return 0;
}
