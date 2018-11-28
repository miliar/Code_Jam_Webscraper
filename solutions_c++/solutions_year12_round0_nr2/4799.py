#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <ctime>
#include <set>
#include <map>
     
using namespace std;

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("goat1.in", "r", stdin); freopen("goat1.out", "w", stdout);
	
	int n, s, y, x, p, t, ans;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		cin >> n >> s >> p;
		ans = 0;
		for (int j = 0; j < n; ++j) {
			cin >> x;
			y = x / 3;
			if (x % 3 != 0) {
				++y;
			}
			if (y >= p) {
				++ans;
			} else if (y + 1 >= p && x % 3 != 1 && x >= 2 && s > 0) {
				--s;
				++ans;
			}
		}
		cout << ans << endl;
	}
		
    return 0;
}
