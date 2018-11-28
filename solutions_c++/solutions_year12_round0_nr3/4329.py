#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <climits>
#include <cstdlib>
 
const double Pi=acos(-1.0);
typedef long long LL;
 
#define Set(a, s) memset(a, s, sizeof (a))
#define Rd(r) freopen(r, "r", stdin)
#define Wt(w) freopen(w, "w", stdout)
 
using namespace std;

int tcount[2000100];

int main (int argc, char ** argv)
{
	int linen;
	cin >> linen;
	for (int i = 1; i <= linen; i++) {
		cout << "Case #" << i << ": ";
		int low, high;
		cin >> low >> high;
		int ans = 0;
		for (int j = low; j <= high; j++) {
			int len = 0;
			int t = j;
			while (t) {
				len++;
				t /= 10;
			}
			if (len <= 1) continue;
			int pow10 = 1;
			for (int k = 0; k < len - 1; k++) {
				pow10 *= 10;
			}
			t = j;
			for (int k = 0; k < len; k++) {
				t = t / 10 + t % 10 * pow10;
				if (t > j && t <= high) {
					if (!tcount[t]) {
					ans++;
					tcount[t] = true;
					}
				}
			}
			t = j;
			for (int k = 0; k < len; k++) {
				t = t / 10 + t % 10 * pow10;
				if (t > j && t <= high) {
					tcount[t] = false;
				}
			}
		}
		cout << ans;
		cout << '\n';
	}
	return 0;
}





