/*
Compiled and Tested using Visual C++ 2008 Express Edition.
ONLINE_JUDGE is a macro for the Sphere Online Judge (SPOJ), where G++
compilers are used.
*/

#define _CRT_SECURE_NO_WARNINGS
//#define TEST

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<list>
#include<deque>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<time.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include<hash_map>
using namespace stdext;
#else
#include<ext/hash_map>
using namespace __gnu_cxx;

namespace __gnu_cxx {
	template<> struct hash<string> {
		size_t operator()(const string& x) const {
			return hash<const char*>() (x.c_str());
		}
	};
}
#endif

//hash_map<string, int> hm;

int diamond[200][200];



bool testSubMatrix1(int a1, int a2, int b1, int b2) {
	for(int i = a1 + 1; i < a2; i++)
		for(int j = b1; j - b1 < i - a1; j++)
			if(diamond[i][j] != diamond[a1 + j - b1][b1 + i - a1])
				return false;
	return true;
}

bool testSubMatrix2(int a1, int a2, int b1, int b2) {
	int dim = a2 - a1;
	for(int i = a1; i < a2 - 1; i++)
		for(int j = b1; j < b2 - i + a1 - 1; j++)
			if(diamond[i][j] != diamond[a2 - j - 1 + b1][b2 - i - 1 + a1])
				return false;
	return true;
}


int main(void) {
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	int tt, it, result, i, j, k, n, l, d1, d2;
	scanf("%d", &tt);
	for(it = 1; it <= tt; it++) {
		scanf("%d", &k);
		n = k;
		for(l = 0; l < n; l++) {
			for(i = l, j = 0; i >= 0; i--, j++)
				scanf("%d", &diamond[i][j]);
		}
		for(l = 1; l < n; l++) {
			for(j = l, i = n - 1; j < n; i--, j++)
				scanf("%d", &diamond[i][j]);
		}
		/* look for the best diagonal */
		for(d1 = 0; d1 < n; d1++)
			if(testSubMatrix1(0, n - d1, d1, n) || testSubMatrix1(d1, n, 0, n - d1))
				break;
		for(d2 = 0; d2 < n; d2++)
			if(testSubMatrix2(0, n - d2, 0, n - d2) || testSubMatrix2(d2, n, d2, n))
				break;
		result = (n + d1 + d2) * (n + d1 + d2) - n * n;
		printf("Case #%d: %d\n", it, result);
		
/*		
		
		printf("d1 = %d, d2 = %d\n", d1, d2);
		for(i = 0; i < n; i++) {
			for(j = 0; j < n; j++)
				printf("%d ", diamond[i][j]);
			printf("\n");
		}
*/

	}
}
