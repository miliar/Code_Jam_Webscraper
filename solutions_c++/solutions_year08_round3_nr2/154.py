#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a-1); i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
typedef long long LG;

char str[44];
int num[44];
int n;
LG r;

int q(char x) {
	return int(x - '0');
}

void count(int k) {
	if(k == 0) {
		LG ww = 0, buf = 0;
		LG v = 1;
		FORD(i,n,0) {
			if(num[i] == 0) {
				ww += buf + v * q(str[i]);
				buf = 0; v = 1;
			} else if(num[i] == 1) {
				ww -= buf + v * q(str[i]);
				buf = 0; v = 1;
			} else {
				buf += v * q(str[i]);
				v *= 10;
			}
		}
		if(ww%2 == 0 || ww%3 == 0 || ww%5 == 0 || ww%7 == 0)
			++r;
	} else {
		LG r = 0;
		FOR(i,0,3) {
			num[k] = i;
			count(k-1);
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%s", str);
		r = 0;
		n = strlen(str);
		count(n-1);
		printf("Case #%d: %lld\n", z, r);
	}
	return 0;
}
