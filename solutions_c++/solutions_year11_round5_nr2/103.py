#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

int n, a[1100];
vector <int> ans, nex;
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", a + i);
		sort(a, a + n);
		ans.clear();
		int an = 1992837465;
		int las = -1;
		for (int i = 0; i < n; i++) {
			int h = i;
			while (h < n && a[h] == a[i]) h++;
			int del = h - i;
			h--;
			if (las == a[i] - 1) {
				nex.clear();
				sort(ans.begin(), ans.end());
				for (int j = 0; j < ans.size(); j++) {
					if (del == 0) {
						an = min(an, ans[j]);
						break;
					}
					nex.PB(ans[j] + 1);
					del--;
				}
				while (del) del--, nex.PB(1);
				ans = nex;
			} else {
				for (int j = 0; j < ans.size(); j++)
					an = min(an, ans[j]);
				ans.clear();
				while (del) del--, ans.PB(1);
			}
			las = a[h];
			i = h;
		}
		for (int i = 0; i < ans.size(); i++)
			an = min(an, ans[i]);
		if (n == 0)
			an = 0;
		printf("Case #%d: %d\n", ++ca, an);
	}
}
