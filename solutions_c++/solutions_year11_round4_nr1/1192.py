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

#define MAX 1024

struct W {
	double b, e, w;
}w[MAX];

int sort_function(const void *a, const void *b) {
	if(((W *)a)->w < ((W *)b)->w)return -1;
	if(((W *)a)->w > ((W *)b)->w)return 1;
	return 0;
}

double x, s, r, t;
int n;

void find_ans() {
	double ans = 0;
	double sum = 0;
	scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
	REP(i, n) {
		scanf("%lf %lf %lf", &w[i].b, &w[i].e, &w[i].w);
		w[i].w += s;
		sum += (w[i].e - w[i].b);
	}
	w[n].b = 0;
	w[n].e = x - sum;
	w[n].w = s;
	n++;
	qsort((void *)w, n, sizeof(w[0]), sort_function);
	REP(i, n) {
		if(t > 0) {
			double tmp = (w[i].e - w[i].b) / (w[i].w + r - s);
			if(tmp > t)
				tmp = t;
			w[i].e -= (w[i].w + r - s) * tmp;
			ans += tmp;
			t -= tmp;
		}
		ans += (w[i].e - w[i].b) / w[i].w;
	}
	printf("%.6lf", ans);
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
