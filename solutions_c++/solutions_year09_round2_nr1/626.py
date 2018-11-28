#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;
const int N = 109;
const int M = 10009;
int n;
char s[M];
int a[M];
int l[M], r[M];
double p[M];
char f[1009][30];
int m, tp;

void init() {
	int L;
	scanf("%d\n", &L);
	tp = 0;
	m = 0;
	memset(l, -1, sizeof(l));
	string ss;
	for (int i=0; i<L; ++i) {
		string t;
		getline(cin, t);
		int j = 0;
		while (t[j]==' ') ++j;
		ss += t;
	}
	n = ss.size();
	strcpy(s, ss.c_str());
	for (int i=0; i<n;) {
		while (i<n && s[i]==' ') ++i;
		if (s[i]==')') {
			--tp;
			++i;
		}
		else {
			++i;
			int off;
			sscanf(s+i, "%lf %n", &p[++m], &off);
			a[++tp] = m;
//		for (int j=1; j<=tp; ++j) printf("%d ", a[j]);puts("");
			if (tp>1) {
				if (l[a[tp-1]]==-1) l[a[tp-1]] = a[tp];
				else r[a[tp-1]] = a[tp];
			}
			i += off;
			while (i<n && s[i]==' ') ++i;
			if (s[i]!=')') {
				sscanf(s+i, "%s %n", f[m], &off);
				i += off;
			}
		}			
	}
//	for (int i=1; i<=m; ++i) printf("%lf %s %d %d\n", p[i], f[i], l[i], r[i]);
}

void solve() {
	scanf("%d", &n);
	for (int i=0; i<n; ++i) {
		char name[30];
		scanf("%s", name);
		int nn;
		scanf("%d", &nn);
		double res = p[1];
		char ff[109][30];
		for (int j=0; j<nn; ++j) scanf("%s", ff[j]);
		int i = 1;
		while (l[i]>=0) {
			bool flag = false;
			for (int j=0; j<nn; ++j) if (strcmp(f[i], ff[j])==0) {
				flag = true;
				break;
			}
			if (flag) i = l[i];
			else i = r[i];
			res *= p[i];
		}
		printf("%.7lf\n", res);
	}
}
			
			
	

int main() {
	int cas, cass = 0;
	for (scanf("%d", &cas); cas--; ) {
		printf("Case #%d:\n", ++cass);
		init();
		solve();
	}
	return 0;
}

