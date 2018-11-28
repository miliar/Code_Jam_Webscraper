#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))

int main() {
	#ifndef ONLINE_JUDGE
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	#endif
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		string s;
		getline(cin, s);
		if (!next_permutation(s.begin(), s.end())) {
			int b[10];
			memset(b, 0, sizeof(b));
			int n = s.length();
			for (int i = 0; i < n; i++) b[(int)(s[i] - '0')]++;
			int mn = -1;
			for (int i = 1; i < 10; i++) if (b[i]) { mn = i; break; }
			stringstream ss;
			ss << mn;
			b[mn]--;
			b[0]++;
			for (int i = 0; i < 10; i++) {
				while (b[i]) {
					ss << i;
					b[i]--;
				}
			}
			s = ss.str();
		}
		printf("Case #%d: ", test);
		cout << s << endl;
	}
	return 0;
}
