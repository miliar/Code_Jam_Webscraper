#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <ctime>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

#define INF 1000000000
#define PA pair<int,int>
#define PA2 pair<int,PA >
#define MAX_N 10005

using namespace std;

int tests,n,d[MAX_N],l[MAX_N],now,entmp,nowtmp,D;
int maxx[MAX_N];
PA tmp[MAX_N],tmp2[MAX_N];

inline int abso(int tmpx) {
    if (tmpx > 0) return tmpx;
    else return -tmpx;
}

inline void solve() {
    scanf("%d", &n);
    for (int i = 0 ; i < n ; i ++) {
	scanf("%d %d", &d[i], &l[i]);
	tmp[i].first = d[i];
	tmp[i].second = l[i];
	maxx[i] = -1;
    }
    scanf("%d", &D);
    maxx[0] = min(l[0], d[0]);
    for (int i = 0 ; i < n ; i ++) {
	if (maxx[i] != -1) {
	    for (int j = 0 ; j < n ; j ++) {
		if (d[j] > d[i] + maxx[i]) break;
		maxx[j] = max(maxx[j], min(abso(d[i] - d[j]), l[j]));
	    }
	    //printf("%d %d\n", d[i], maxx[i]);
	}
    }
    now = -1;
    for (int i = 0 ; i < n ; i ++) {
	if (maxx[i] != -1) now = max(now, d[i] + maxx[i]);
    }
    /*now = d[0];
    sort(tmp, tmp + n);
    entmp = 0;
    nowtmp = tmp[0].first;
    for (int i = 0 ; i < n ; i ++) {
	if (nowtmp < tmp[i].first + tmp[i].second) {
	    tmp2[entmp] = tmp[i];
	    entmp ++;
	    nowtmp = tmp[i].first + tmp[i].second;
	}
	}
    */
    if (now >= D) printf("YES");
    else printf("NO");
    return ;
}

int main() {
    //freopen("template.in", "r", stdin);
    //freopen("template.out", "w", stdout);
    scanf("%d", &tests);
    for (int test = 1 ; test <= tests ; test ++) {
	printf("Case #%d: ", test);
	solve();
	printf("\n");
    }
    return 0;
}
