#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <string.h>

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
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

#define P 100003

int add(int a, int b) {
	return (a + b) % P;
}

int sub(int a, int b) {
	return (a - b + P) % P;
}

int mult(int a, int b) {
	return int((int64)(a - b) % (int64)P);
}

int test, testq;

int n;

#define MAX 1000

int a[MAX];
int q;

int ans;

bool Check() {
	int i;
	int x;	
	int f;
	x = n;
	while (x != 1) {
		f = 0;
		fi(1, q) {
			if (a[i] == x) {
				x = i;
				f = 1;
				break;
			}
		}
		if (!f) return false;
	}
	return true;
}

void Fun(int x) {
	int i;
	q = x;
	a[q] = n;
	if (Check()) ans = add(ans, 1);
	fi(a[x - 1] + 1, n - 1) {
		a[x] = i;
		Fun(x + 1);
	}
}

void Solve() {
	ans = 0;
	a[0] = 1;
	Fun(1);
	printf("%d\n", ans);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		Solve();
	}
	return 0;
}
