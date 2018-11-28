#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

long long n, pd, pg;

void read_input() {
	scanf("%lld %lld %lld", &n, &pd, &pg);
}

bool ans() {
	if(pd != 100 && pg == 100)return false;
	if(pd != 0 && pg == 0)return false;

	long long d;
	long long md = 100;
	REMIN(md, n);
	for(d = 1; d <= md; d++)
		if(pd * d % 100 == 0)
			return true;
	return false;
}

void find_ans() {
	read_input();

	if(ans())printf("Possible");
	else printf("Broken");
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
