#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int testq;
int test;

#define MAX 1010

int n;
int l[MAX];
double p[MAX];

void Read() {
	int i;
	scanf("%d", &n);
	fi(0, n - 1) {
		scanf("%d", &l[i]);
	}
	fi(0, n - 1) {
		scanf("%lf", &p[i]);
		p[i] /= 100;
		p[i] = 1 - p[i];
	}
}

double d[MAX];

vector <int> g;	

double eps = 1e-9;

double ans;
vector <int> ansv;

double matr[10][10];
double b[10];
double M[10];

int k;

void Swap(int l1, int l2) {
	int i;
	fi(0, k) {
		swap(matr[l1][i], matr[l2][i]);
	}
	swap(b[l1], b[l2]);
}

void Gauss() {
	int i, j, o;
	int f;
	double g;
	double bst;
	fi(0, k) {
		f = -1;
		bst = -1;
		fj(i, k) {
			if (fabs(matr[j][i]) > bst) {
				bst = fabs(matr[j][i]);
				f = j;
			}
		}

		Swap(i, f);

		fj(0, k) {
			if (j == i) continue;
			g = -matr[j][i] / matr[i][i];
			fo(1, k) {
				matr[j][o] += matr[i][o] * g;
			}
			b[j] += b[i] * g;
		}
	}

	fi(0, k) {
		M[i] = b[i] / matr[i][i];
	}
}

double Check(int g0, int g1) {
	int i;
	k = 1;
	ZERO(matr);
	ZERO(b);
	
	matr[1][0] += 1 - p[g1];
	b[1] += -l[g1];
	matr[1][1]--;
	
	matr[0][0] += 1 - p[g0];
	matr[0][1] += p[g0];
	b[0] += -l[g0];
	matr[0][0]--;
	
	Gauss();
	return M[0];
}

void Solve() {
	int i;
	g.clear();
	fi(0, n - 1) {
		g.pb(i);
	}
	ans = 1e18;
	ansv.clear();
	do {
		ZERO(d);
		//Check();
		if (M[0] < ans - eps) {
			ans = M[0];
			ansv = g;
		}
	} while (next_permutation(g.begin(), g.end()));
	fi(0, SIZE(g) - 1) {
		printf("%d ", ansv[i]);
	}
	printf("\n");

}

void Solve2() {
	int i, j;
	double v1, v2;
	g.clear();
	fi(0, n - 1) {
		g.pb(i);
	}
	
	ansv.clear();
	fj(0, n) {
		fdi(n - 2, 0) {
			v1 = Check(g[i], g[i + 1]);
			v2 = Check(g[i + 1], g[i]);
			if (v2 < v1 - eps) {
				swap(g[i], g[i + 1]);
			}
		}
	}
	fi(0, SIZE(g) - 1) {
		printf("%d ", g[i]);
	}
	printf("\n");
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve2();
		fflush(stdout);
	}
	return 0;
}