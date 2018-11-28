#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

char* by_len[11][10010];
int by_size[11];
int n, m;

int hused;
int used[10010];

char source_data[10010][12];
char lens[10010];

void input() {
	GI2(n, m);
	FIR(11) by_size[i] = 0;

	FI {
		scanf("%s", source_data[i]);
		lens[i] = strlen(source_data[i]);
		by_len[lens[i]][by_size[lens[i]]++] =source_data[i];
	}
}

char order[30];

inline bool contains(char* s, char c) {
	for(; *s; ++s) if (*s == c) return true;
	return false;
}

int contain_mask(char* s, char c) {
	int res = 0;
	for(int ind = 0; *s; ++s, ++ind) if (*s == c) res |= 1 << ind;
	return res;
}

int score(int pos) {
	char* self = source_data[pos];
	++hused;

	int cnt = by_size[lens[pos]];
	char** c= by_len[lens[pos]];
	int l = lens[pos];

	int res = 0;

	REP(kkk,26) {
		char cand=order[kkk];
		bool ok = false;

		FIR(cnt) if (used[i] != hused) {
			if (contains(c[i], cand)) {
				ok = true;
				break;
			}
		}

		if (ok) {
			if(contains(self, cand)) {
				int mask = contain_mask(self, cand);
				FIR(cnt) if (used[i] != hused)
					if(contain_mask(c[i], cand) != mask)
						used[i] = hused;

			} else {
				++res;
				FIR(cnt) if (used[i] != hused)
					if (contains(c[i], cand)) 
						used[i] = hused;
			}
		} 
	}

	return res;
}

int main() {
freopen("B-small-attempt0.in", "rt", stdin);
freopen("B-small-attempt0.out", "w", stdout);

	int ntc; GI(ntc);
	
	hused = 0;
	memset(used, 0, sizeof used);

	FORE(tc, 1, ntc) {
		input();

		printf("Case #%d:", tc);

		FIR(m) {
			scanf("%s", order);
			int scor = -1;
			char* res = 0;

			FJ {
				int cs = score(j);
				if (cs>scor) scor = cs, res = source_data[j];
			}
			printf(" %s", res);
		}

		puts("");
	}

}
