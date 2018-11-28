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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

int d, p, k;
int arr[16];

const int SIZE = 1<<20;
bool pr[SIZE];

void sub(int &x, int y) {
	x -= y;
	if (x < 0) x += p;
}
void add(int &x, int y) {
	x += y;
	if (x >= p) x -= p;
}
int mult(int x, int y) {
	return (int64(x) * y) % p;
}
int recgcd(int a, int b, int &x, int &y) {
	if (!b) {
		x = 1;
		y = 0;
		return a;
	}
	int q = a / b;
	int g = recgcd(b, a%b, y, x);
	y -= q*x;
	return g;
}
int anti(int x) {
	assert(x);
	int aa, bb;
	int ggg = recgcd(x, p, aa, bb);
	assert(ggg == 1);
	if (aa < 0) aa += p;
	return aa;
}

bool ok;
int tans;
void Check(int a, int b) {
	int newx;
	for (int i = 0; i<k; i++) {
		newx = mult(a, arr[i]);
		add(newx, b);
		if (i+1<k && newx != arr[i+1]) return;
	}
//	fprintf(stderr, "%d %d: %d\n", a, b, newx);
	if (tans < 0) tans = newx;
	else if (tans != newx) ok = false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	memset(pr, true, sizeof(pr));
	pr[0] = pr[1] = false;
	for (int i = 2; i*i<SIZE; i++) if (pr[i])
		for (int j = i*i; j<SIZE; j+=i)
			pr[j] = false;

	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &d, &k);
		for (int i = 0; i<k; i++) scanf("%d", arr+i);

		ok = true;
		tans = -1;

		if (k == 1) ok = false;
		else {
			int maxp = 1;
			for (int i = 0; i<d; i++) maxp *= 10;
	
		    for (p = 0; p<maxp; p++) if (pr[p]) {
		    	int i;
				for (i = 0; i<k; i++) if (!(arr[i] < p)) break;
				if (i < k) continue;
				
				if (arr[0] == arr[1]) Check(1, 0);
				else {
					if (k < 3) {
						ok = false;
						continue;
					}
					int s = arr[0];
					int u = arr[1];
					int v = arr[2];
					int d0 = u; sub(d0, s);
					int d1 = v; sub(d1, u);

					int ca = mult(anti(d0), d1);
					int cb = u;  sub(cb, mult(s, ca));

					Check(ca, cb);
				}
		    }
	    }
		
		printf("Case #%d: ", tt);
		if (ok) {
			assert(tans >= 0);
			printf("%d\n", tans);
		}
		else printf("I don't know.\n");
		fflush(stdout);
	}
	return 0;
}
