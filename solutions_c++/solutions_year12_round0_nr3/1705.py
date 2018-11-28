#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define sz(v) (int)(v).size()

int b[10];
int a[2000000 + 10];

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int test = 1; test <= tst; test++) {
		memset(a, -1, sizeof(a));
		int L, R;
		cin >> L >> R;
		int res = 0;
		for (int i = L; i < R; i++) {
			int k = 0;
			int t = i;
			while (t != 0) {
				b[k++] = t % 10;
				t /= 10;
			}
			reverse(b, b + k);
			//set <int> st;
			REP(j, k) {
				if (b[j] == 0) {
					continue;
				}
				int p = j;
				int x = 0;
				REP(q, k) {
					x *= 10;
					x += b[p];
					p++;
					if (p == k) {
						p = 0;
					}
				}
				if (i < x && x <= R) {
					if (a[x] != i) {
						++res;
						a[x] = i;
					}
					//++res;
					//cout << i << " " << x << endl;
					//st.insert(x);
				}
			}
			//res += sz(st);
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}