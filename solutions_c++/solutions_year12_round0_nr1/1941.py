#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 7;

char iin[4][nmax] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "y qeez"};
char iout[4][nmax] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "a zooq"};

char p[nmax];
char s[nmax];

void initPerm() {

	for(int i = 0; i < nmax; ++i) {
		p[i] = i;
	}

	for(int i = 'a'; i <= 'z'; ++i) {
		p[i] = -1;
	}

	for(int i = 0; i < 4; ++i) {

		int n = strlen(iin[i]);
		for(int j = 0; j < n; ++j) {
			p[iin[i][j]] = iout[i][j];
		}
	}

  	for(int i = 'a'; i <= 'z'; ++i) {
		if (p[i] == -1) {
			cerr << "Unitialized: " << (char)i;
			p[i] = i;
		}
	}


}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
#endif

	initPerm();

	int t;
	scanf("%d\n", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		printf("Case #%d: ", tt + 1);

		gets(s);
		int n = strlen(s);


		for(int j = 0; j < n; ++j) {
			putchar(p[s[j]]);
		}

//		printf("%d", t);
		puts("");
	}
	return 0;
}