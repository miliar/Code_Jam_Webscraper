#include <cstdio>
#include <vector>
#include <string>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)

const int M = 1010000;
vector<string> ch[2036];
vector<int> id[2036];
int t, n, m, k, all;
int ans, nn;
string s[M];
char tt[M];
char b[M];

void ins(int p, int k, int add) {
	if (k == nn)
		return;
	int ne = -1;
	for (int i = 0; i < ch[p].size() && ne == -1; i++) {
		if (ch[p][i] == s[k]) {
			ne = id[p][i];
		}
	}
	if (ne == -1) {
		ch[p].push_back( s[k] );
		id[p].push_back( all );
		ne = all++;
		ans += add;
	}
	ins(ne, k + 1, add);
}

void doit(int n, int a) {
	int add, cnt;
	while (n--) {
		scanf("%s", b);
		for (int i = 0; b[i]; ++i)
			if (b[i] == '/')
				b[i] = ' ';
		nn = 0, add = 0, cnt;
		while (sscanf(b + add, "%s%n", tt, &cnt) != EOF) {
			s[nn ++] = tt;
			add += cnt;
		}
		ins(0, 0, a);
	}
}

int main() {
	scanf("%d", &t);
	FOR(zz,1,t+1) {
		scanf("%d%d", &n, &m);
		FOR(i,0,2036) ch[i].clear(), id[i].clear();
		all = 1;
		ans = 0;
		doit(n, 0);
		doit(m, 1);
		printf("Case #%d: %d\n", zz, ans);
	}
}
