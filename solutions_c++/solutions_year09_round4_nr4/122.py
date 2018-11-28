#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cctype>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)

const int maxn = 11111;
const double eps = 1e-8;

int dcmp(double x) {
    return x < -eps ? -1 : x > eps;
}

double sqr(double x) {
    return x * x;
}

class tnode {
public:
    double x, y;

    tnode () {}
    tnode (double nx, double ny): x(nx), y(ny) {}

    double len() {
        return sqrt(sqr(x) + sqr(y));
    }
};

tnode operator+(const tnode &a, const tnode &b) {
    return tnode(a.x + b.x, a.y + b.y);
}

tnode operator-(const tnode &a, const tnode &b) {
    return tnode(a.x - b.x, a.y - b.y);
}

tnode operator*(const tnode &a, double d) {
    return tnode(a.x * d, a.y * d);
}

tnode operator/(const tnode &a, double d) {
    return tnode(a.x / d, a.y / d);
}

bool operator<(const tnode &a, const tnode &b) {
    return dcmp(a.x - b.x) ? dcmp(a.x - b.x) < 0 : dcmp(a.y - b.y) < 0;
}

bool operator==(const tnode &a, const tnode &b) {
    return dcmp(a.x - b.x) == 0 && dcmp(a.y - b.y) == 0;
}

double dis(const tnode &a, const tnode &b) {
    return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}


class circle {
public:
    tnode o;
	double r;

	bool inside(tnode a) {
	    return sqr(a.x - o.x) + sqr(a.y - o.y) <= r;
	}

	void calc(tnode a, tnode b) {
	    o.x = (a.x + b.x) / 2;
	    o.y = (a.y + b.y) / 2;
	    r = sqr(a.x - o.x) + sqr(a.y - o.y);
	}

	void calc(tnode a, tnode b, tnode c) {
		double a1 = 2 * (a.x - b.x);
		double b1 = 2 * (a.y - b.y);
		double c1 = sqr(a.x) - sqr(b.x) + sqr(a.y) - sqr(b.y);
		double a2 = 2 * (a.x - c.x);
		double b2 = 2 * (a.y - c.y);
		double c2 = sqr(a.x) - sqr(c.x) + sqr(a.y) - sqr(c.y);
		o.x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1);
		o.y = (c1 * a2 - c2 * a1) / (a2 * b1 - a1 * b2);
		r = sqr(a.x - o.x) + sqr(a.y - o.y);
	}
};


tnode p[maxn], info[maxn], p1[maxn], p2[maxn];
double r[maxn], r1[maxn], r2[maxn];
circle cc;
int n, n1, n2;
double res;
int id[maxn];

double get(int n, tnode p[maxn], double r[maxn]) {
    if (n == 1) return r[0] * r[0];
    if (n == 0) return 0;

    int m = n;
    for (int i = 0; i < n; i++) info[i] = p[i];
    tnode t;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) if (i < j) {
            t = p[j] - p[i];
            t = t / t.len();
            info[m++] = p[j] + t * r[j];
            info[m++] = p[i] - t * r[i];
        }
    sort(info, info + m);
    m = unique(info, info + m) - info;
    n = m;
//    printf("n = %d\n", n);
    //for (int i = 0; i< n; i++) printf("%lf %lf\n", info[i].x, info[i].y);
    //printf("===\n");
	cc.calc(info[0], info[1]);
	for (int i = 2; i < n; i++) {
		if (cc.inside(info[i])) continue;
		cc.calc(info[0], info[i]);
		for (int j = 1; j < i; j++) {
			if (cc.inside(info[j])) continue;
			cc.calc(info[i], info[j]);
			for (int k = 0; k < j; k++) {
				if (cc.inside(info[k])) continue;
				cc.calc(info[k], info[j], info[i]);
			}
		}
	}
	return cc.r;
}

void solve() {
    res = 9e20;
    for (int rt = 0; rt < 10000; rt++) {
        for (int i = 0; i < n; i++) id[i] = i;
        for (int i = 0; i < n; i++) id[i] = rand() % 2;
        n1 = n2 = 0;
        for (int i = 0; i < n; i++) if (id[i]) {
            p1[n1] = p[i];
            r1[n1++] = r[i];
        } else {
            p2[n2] = p[i];
            r2[n2++] = r[i];
        }

        double tmp1 =get(n1, p1, r1), tmp2 = get(n2, p2, r2);
        res = min(res, max(tmp1, tmp2));
    }

}

int main(){
    srand(12345);
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%lf%lf%lf", &p[i].x,&p[i].y,&r[i]);
        solve();
        printf("Case #%d: %.8lf\n", tt + 1, sqrt(res));
    }
}
