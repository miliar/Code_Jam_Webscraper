 #include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

char a[51][51], ch;

void Do(int case_number)
{
	int i, j, n, k, l;
	bool was[260]; memset(was, false, sizeof(was));
	cin >> n >> l;
	for (i = n; i >= 1; i--)
		for (j = 1; j <= n; j++)
			cin >> a[j][i];

	for (i = 1; i <= n; i++) {
		k = n;
		for (j = n; j >= 1; j--) if (a[j][i] != '.') a[k--][i] = a[j][i];
		while (k) a[k--][i] = '.';
	}

	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++) {
			ch = a[i][j];
			if (ch != '.' && !was[ch]) {
				//vertically:
				if (i >= l) {
					for (k = 0; k < l; k++) if (a[i-k][j] != ch) goto horizontal;
					was[ch] = true;
				}
				horizontal:
				if (j >= l) {
					for (k = 0; k < l; k++) if (a[i][j-k] != ch) goto diag1;
					was[ch] = true;
				}
				diag1:
				if (i >= l && j >= l) {
					for (k = 0; k < l; k++) if (a[i-k][j-k] != ch) goto diag2;
					was[ch] = true;
				}
				diag2:
				if (i >= l && j + l - 1 <= n) {
					for (k = 0; k < l; k++) if (a[i-k][j+k] != ch) goto breaked;
					was[ch] = true;
				}
				breaked:;
			}
		}
	cout << "Case #" << case_number << ": ";
	if (was['R'] && was['B']) cout << "Both\n"; else
	if (!was['R'] && !was['B']) cout << "Neither\n"; else
	if (was['R']) cout << "Red\n"; else
	cout << "Blue\n";
}

int main()
{
	freopen("a.in", "r", stdin);
   	freopen("a.out", "w", stdout);
   	int m; cin >> m;
   	for (int k = 1; k <= m; k++)
   		Do(k);
}
