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
#define PA pair<double,int>
#define PA2 pair<double,double>
#define MAX_N 1005

using namespace std;

int tests;
int n,rev[MAX_N],xnow,ynow;
double w,l,r[MAX_N];
double x[MAX_N],y[MAX_N];
PA tmp[MAX_N];
set<PA2 > py;
set<PA2 >::iterator it;

inline bool isin(double tmpx, double tmpy) {
    return tmpx >= 0 and tmpx <= w and tmpy >= 0 and tmpy <= l;
}

inline bool inter(double x1, double x2, double y1, double y2) {
    return max(x1, y1) < min(x2, y2);
}

inline bool isok(double posx, double posy, int ind) {
    for (int i = 0 ; i < ind ; i ++) {
	if (inter(posx - tmp[ind].first, posx + tmp[ind].first, x[i] - tmp[i].first, x[i] + tmp[i].first) and inter(posy - tmp[ind].first, posy + tmp[ind].first, y[i] - tmp[i].first, y[i] + tmp[i].first)) return false;
    }
    return true;
}

inline void solve() {
    scanf("%d", &n);
    scanf("%lf %lf", &w, &l);
    for (int i = 0 ; i < n ; i ++) {
	scanf("%lf", &r[i]);
	tmp[i].first = -r[i];
	tmp[i].second = i;
    }
    /*
    printf("%d\n", n);
    printf("%lf %lf\n", w, l);
    for (int i = 0 ; i < n ; i ++ ) {
	printf("%lf ", r[i]);
    }
    printf("\n");
    */
    py.clear();
    sort(tmp, tmp + n);
    for (int i = 0 ; i < n ; i ++) {
	rev[tmp[i].second] = i;
	tmp[i].first = -tmp[i].first;
    }
    py.insert(PA2(0, 0));
    for (int i = 0 ; i < n ; i ++) {
	while (true) {
	    it = py.begin();
	    double posx, posy;
	    if (it -> first == 0 and it -> second == 0) {
		posx = 0;
		posy = 0;
	    } else if (it -> first == 0) {
		posx = 0;
		posy = it -> second + tmp[i].first;
	    } else if (it -> second == 0) {
		posx = it -> first + tmp[i].first;
		posy = 0;
	    } else {
		posx = it -> first + tmp[i].first;
		posy = it -> second + tmp[i].first;
	    }
	    //printf("%d : %lf : %lf %lf\n", i, tmp[i].first, posx, posy);
	    fflush(stdout);
	    if (isin(posx, posy) and isok(posx, posy,i)) {
		x[i] = posx;
		y[i] = posy;
		py.erase(it);
		py.insert(PA2(x[i] + tmp[i].first, y[i] + tmp[i].first));
		py.insert(PA2(x[i], y[i] + tmp[i].first));
		py.insert(PA2(x[i] + tmp[i].first, y[i]));
		break;
	    } else {
		py.erase(it);
	    }
	}
    }
    for (int i = 0 ; i < n ; i ++) {
	printf(" %lf %lf", x[rev[i]], y[rev[i]]);
    }
    //printf("\n");
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
