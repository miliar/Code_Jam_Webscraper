#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

#define MAXN 10240
#define MAXM 128
#define MAXS 32

int n, m, len[MAXN];
bool use[MAXN];
int _max, ans;
char words[MAXN][MAXS], lists[MAXM][MAXS];

void read_input() {
	scanf("%d %d", &n, &m);
	REP(i, n) {
		scanf("%s", words[i]);
		len[i] = strlen(words[i]);
	}
	REP(i, m)
		scanf("%s", lists[i]);
}

int cal(int w, int l) {
	int tmp[MAXN], count = 0;
	int _len = len[w];
	int out = 0;
	REP(i, n)
		if(len[i] == _len && i != w)
			tmp[count++] = i;
	REP(i, 26) {
		char ch = lists[l][i];
		int c = 0;
		bool f = false;
		bool wf = false;
		REP(k, _len)
			if(words[w][k] == ch)wf = true;
		REP(j, count) {
			bool match = true;
			REP(k, _len) {
				if(words[tmp[j]][k] == ch)f = true;
				if((words[w][k] == ch) ^ (words[tmp[j]][k] == ch))
					match = false;
			}
			if(match)tmp[c++] = tmp[j];
		}
		if(wf || f) {
			count = c;
			if(!wf)out++;
			if(count == 0)break;
		}
	}
	//printf("\ncal(%s, %d) = %d", words[w], l, out);
	return out;
}

void find_ans() {
	read_input();

	REP(i, m) {
		_max = -1;
		REP(j, n) {
			int p = cal(j, i);
			if(p > _max) {
				_max = p;
				ans = j;
			}
		}
		//printf("\n %s %d", words[ans], _max);
		printf(" %s", words[ans]);
	}
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
