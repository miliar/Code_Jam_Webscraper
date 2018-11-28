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

int testq;
int test;

int n, k;
int p;

int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", test);
		p = 1;
		fi(1, n) {
			p *= 2;
		}
		p--;
		if ((k & p) == p) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}
	return 0;
}
