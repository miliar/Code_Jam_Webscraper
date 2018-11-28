#include <algorithm>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
const int MAXN = 50;
char buf[MAXN];

const int INF = 1000000000;

bool check(const vector<int>& v) {
	for (int i=0; i<v.size(); i++)
		if (v[i] > i) return false;
	return true;
}

vector<int> tab;
/*
int solve(int l, int r) {
	int res = INF;
	for (int i=l+1; i<r; i++)
		if (tab[i-1] > i-1) {
			res = min(res, 
		}
	return res;
}*/

int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int n;
		scanf("%d\n", &n);
		vector<string> v(n);
		for (int i=0; i<n; i++) {
			gets(buf);
			v[i] = string(buf);
		}
		tab.resize(n);
		for (int i=0; i<n; i++) {
			int j;
			for (j=n-1; j>=0 && v[i][j] != '1'; j--);
			tab[i] = j;
		}

		int res = 0;
		for (int i=0; i<n; i++) {
			int j;
			for (j=0; j<n && tab[j] <= j; j++);
			if (j==n) break;
			int k;
			for (k=j+1; k<n && tab[k] > j; k++);
			assert(k<n);
			res += k-j;
			int tj = tab[j];
			int tk = tab[k];
			tab.erase(tab.begin()+k);
			tab.insert(tab.begin()+j, tk);
		}

		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}