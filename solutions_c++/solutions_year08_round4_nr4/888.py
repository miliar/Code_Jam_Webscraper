#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define EPS 1e-8

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int, int> PII;
typedef set<int> SI;
typedef map<int, int> MII;

const int maxn = 1024;

string s, t;
VI p;
int k, n;

string doit(string s) {
	string t = s;
	for (int i = 0; i < k; ++i) s[i] = t[p[i]];
	return s;		
}

int cost(string s) {
	int ret = 0;
	for (int i = 0; i < n; ) {
		int j = i + 1;
		while (j < n && s[i] == s[j]) ++j;
//		printf("i = %d j = %d\n", i, j);
		++ret;
		i = j;
	}
	return ret;
}

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		scanf("%d\n", &k);
		cin >> s;
//		cout << k << " " << s;
		n = s.length();
		p.clear();
		for (int i = 0; i < k; ++i) p.push_back(i);
				
		int ans = 2000000000;
		do {
	 		 t = s;
//	 		 for (int i = 0; i < k; ++i) printf("%d ", p[i]);
//	 		 printf("\n");
	 		 string ret = "";
	 		 for (int i = 0; i < n; i += k) {
	 		 	string r = doit(t.substr(i, k));
	 		 	ret += r;
//	 		 	cout << "r = " << r << "\n";
	 		 }
// 		 	 cout << ret << "\n";
 		 	 int tmp = cost(ret);
 		 	 ans <?= tmp;
		} while (next_permutation(p.begin(), p.end()));
		printf("%d\n", ans);
	}
	return 0;
}

