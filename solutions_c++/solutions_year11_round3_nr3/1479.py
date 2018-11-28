/*
 * PerfectHarmony
 * May 22, 2011,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

vector<int> v;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	loop(id,t) {
		int n, l, h;
		v.clear();
		scanf("%d%d%d", &n, &l, &h);
		v.resize(n);
		loop(i,n)
			scanf("%d", &v[i]);
		bool bad = 1;
		printf("Case #%d: ", id + 1);

		for (int i = l; i <= h; i++) {
			int c = 0;
			for (int j = 0; j < SZ(v); j++)
				if (v[j] % i == 0 || i % v[j] == 0)
					c++;
			if (c == SZ(v)) {
				printf("%d\n", i);
				bad = 0;
				break;
			}
		}
		if (bad)
			printf("NO\n");
	}
	return 0;
}
