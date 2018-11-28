#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;

using namespace std;

string to_st(int a) {
	string ans = "";
	while (a > 0) {
		ans += a % 10 + '0';
		a /= 10;
	}
	reverse(ans.begin(), ans.end());
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int A, B;
	for (int I = 1; I <= T; ++I) {
		cin >> A >> B;
		int ans = 0;
		for (int n = A; n < B; ++n) {
			for (int m = n + 1; m <= B; ++m) {
				string s = to_st(m);
				string s2 = to_st(n);
				s2 += s2;
				int len = SZ(s);
				for (int i = 0; i < len; ++i) {
					if (s == s2.substr(i, len)) {
						++ans;
						break;
					}
				}
			}
		}
		cout << "Case #"<< I << ": " << ans << endl;
	}
	return 0;
}