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

#define LINT long long

using namespace std;

#define MAX 1024

void find_ans() {
	LINT r, k, n;
	LINT g[MAX], use[MAX];

	REP(i, MAX)
		use[i] = 0;

	scanf("%lld %lld %lld", &r, &k, &n);

	//LINT tmp = 0;
	REP(i, n) {
		scanf("%lld", &g[i]);
		//tmp += g[i];
	}
	/*if(tmp <= k) {
		printf("%lld", r * tmp);
		return;
	}*/

	bool found = false, uflag = false;
	LINT ans = 0, rcount = 0, rstep = 0;
	LINT pos = 0, spos = 0;
	REP(round, r) {
		if(found && spos == pos && !uflag) {
			uflag = true;

			LINT next = ((r - round) / rstep);
			ans += rcount * next;
			round += next * rstep;
			if(round >= r)break;
		}
		if(use[pos] && !found) {
			found = true;
			spos = pos;
		}
		use[pos] = 1;

		LINT tmp = pos;
		LINT sum = 0;
		while(sum + g[pos] <= k) {
			sum += g[pos];
			pos = (pos + 1) % n;
			if(pos == tmp)break;
		}
		ans += sum;
		if(found) {
			rcount += sum;
			rstep++;
		}
	}
	printf("%lld", ans);
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
