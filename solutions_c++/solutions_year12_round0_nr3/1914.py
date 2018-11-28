#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vint;

int d[2012030], m[30];

int main() {
	int a = 1, b = 9;
	for (int i = 1; i <= 6; i ++) {
		for (int j = a; j <= b; j ++) d[j] = i;
		m[i-1] = a;
		a *= 10; b = b * 10 + 9;
	}	
	m[6] = 1000000; m[7] = 10000000;
	for (int i = 1000000; i <= 2000000; i ++) d[i] = 7;

	int T; scanf("%d", &T);
	for (int Case = 1; Case <= T; Case ++) {
		int x, y; scanf("%d%d", &x, &y);

		vint v;
		int n[10], l;
		int ans = 0;
		for (int i = x; i <= y; i ++) {
			v.clear(); v.push_back(i);
			int cur = i; 
			l = d[i];

			for (int j = 0; j < l; j ++) n[j] = cur % m[j+1] / m[j];
			for (int j = 0; j < l - 1; j ++) {
				for (int k = 0; k < l - 1; k ++) {
					int t = n[k]; n[k] = n[k+1]; n[k+1] = t;
				}

				cur = 0;
				for (int k = l - 1; k >= 0; k --) cur = cur * 10 + n[k];
				if (cur >= x && cur <= y && d[cur] == l) v.push_back(cur);
			}

			sort(v.begin(), v.end());

			if (i > v[0]) continue;
			
			int cat = 1;
			for (int i = 0; i < v.size() - 1; i ++)
				if (v[i] != v[i+1]) cat ++;
			ans += cat * (cat - 1) / 2;
		}
		printf("Case #%d: %d\n", Case, ans);
	}

	return 0;
}
