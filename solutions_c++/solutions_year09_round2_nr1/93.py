#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define pb push_back
#define mp make_pair

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? (-(x)) : (x))

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

char s[10000000];

struct TT {
	int l, r;
	int feature;
	double weight;
} t[100000];
int tc;
map<string, int> features;
int fc;
char w[100];
int u[100000];

int parse(char *s, int &i) {
	while (s[i] != '(') {
		++i;
	}
	++i;
	int k = tc++;
	sscanf(s + i, "%lf", &t[k].weight);
	while (isdigit(s[i]) || (s[i] == '.')) {
		++i;
	}
	while (!isalpha(s[i]) && (s[i] != ')')) {
		++i;
	}
	if (s[i] != ')') {
		int j = 0;
		while (isalpha(s[i])) {
			w[j++] = s[i];
			++i;
		}
		w[j] = 0;
		if (features.find(w) == features.end()) {
			features[w] = fc++;
		}
		t[k].feature = features[w];
		t[k].l = parse(s, i);
		t[k].r = parse(s, i);
	} else {
		t[k].l = t[k].r = -1;
	}
	return k;
}

int main() {
	int T; scanf("%d", &T);
	int e = 1;
	for (int tt = 0; tt < T; ++tt) {
		features.clear();
		tc = 0;
		int l;
		scanf("%d\n", &l);
		char *ss = s;
		for (int i = 0; i < l; ++i) {
			gets(ss);
			int m = strlen(ss);
			ss[m++] = ' ';
			ss[m] = 0;
			ss += m;
		}
		int j = 0;
//		printf("%s\n", s);
		parse(s, j);
/*		for (int i = 0; i < tc; ++i) {
			printf("%d %d %d %d %lf\n", i, t[i].l, t[i].r, t[i].feature, t[i].weight);
		}*/
		int n; scanf("%d", &n);
		printf("Case #%d:\n", tt + 1);
		for (int i = 0; i < n; ++i) {
			int k;
			scanf("%*s %d", &k);
			for (int j = 0; j < k; ++j) {
				scanf("%s", w);
				int x = -1;
				if (features.find(w) != features.end()) {
					x = features[w];
				}
				if (x != -1) {
					u[x] = e;
				}
			}
			int v = 0;
			long double result = 1.0;
			while (v != -1) {
				result *= t[v].weight;
				if (u[t[v].feature] == e) {
					v = t[v].l;
				} else {
					v = t[v].r;
				}
			}
			printf("%.9Lf\n", result);
			++e;
		}
	}
	return 0;
}
