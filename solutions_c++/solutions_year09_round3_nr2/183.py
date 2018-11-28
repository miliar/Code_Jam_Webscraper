#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

typedef vector<int> vi; 
typedef pair<int,int> ii;
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 

const int maxn = 600;
double X[3][maxn];
double V[3][maxn];
double x[3], v[3];
int n;

inline double sqr(double x)
{
    return x * x;
}

void init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < 3; ++j) {
	    scanf("%lf", &X[j][i]);
	}
	for (int j = 0; j < 3; ++j) {
	    scanf("%lf", &V[j][i]);
	}
    }
    for (int i = 0; i < 3; ++i) {
	x[i] = 0;
	for (int j = 0; j < n; ++j) {
	    x[i] += X[i][j];
	}
	x[i] /= n;
	v[i] = 0;
	for (int j = 0; j < n; ++j) {
	    v[i] += V[i][j];
	}
	v[i] /= n;
    }
}

void run()
{
    double left = 0;
    double right = 0;
    double t;
    for (int i = 0; i < 3; ++i) {
	left += v[i] * v[i];
    }
    for (int i = 0; i < 3; ++i) {
	right += x[i] * v[i];
    }
    if (abs(left) < 1e-9) {
	t = 0;
    }
    else {
	t = -right / left;
	if (t < 0) {
	    t = 0;
	}
    }

    double ans = 0;
    for (int i = 0; i < 3; ++i) {
	ans += sqr(x[i] + v[i] * t);
    }
    ans = sqrt(ans);
    printf("%.8lf ", ans);
    if (abs(t) < 1e-9) {
	printf("0.00000000\n");
    }
    else {
	printf("%.8lf\n", t);
    }
}

int main(void)
{
    int c;
    scanf("%d", &c);
    for (int i = 1; i <= c; ++i) {
	printf("Case #%d: ", i);
	init();
	run();
    }
    return 0;
}

