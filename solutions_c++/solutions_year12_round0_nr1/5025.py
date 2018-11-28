#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <stack>
#include <map>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <fstream>
#include <cassert>
using namespace std;
 
#ifdef MYDEBUG
#pragma comment(linker, "/stack:1000000000")
#endif

typedef pair<int, int> PII;
typedef long long LL;
typedef unsigned long long ULL;
 
#define MAX(a, b) ((a >= b) ? a : b)
#define MIN(a, b) ((a <= b) ? a : b)
#define ABS(a) ((a < 0) ? -(a) : a)
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define sz size()
#define mp make_pair
#define pb push_back
#define HAS(S, v) ((S).find(v) != (S).end())
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define CLR(a, b) memset(a, b, sizeof(a))
#define sqr(a) ((a) * (a))
#define V(t) vector<t>
#define VV(t) V(V(t))

int mas[32];
int main() {
#ifdef MYDEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    clock_t beg = clock();
#endif

	mas[0] = 24;
	mas[1] = 7;
	mas[2] = 4;
	mas[3] = 18;
	mas[4] = 14;
	mas[5] = 2;
	mas[6] = 21;
	mas[7] = 23;
	mas[8] = 3;
	mas[9] = 20;
	mas[10] = 8;
	mas[11] = 6;
	mas[12] = 11;
	mas[13] = 1;
	mas[14] = 10;
	mas[15] = 17;
	mas[16] = 25;
	mas[17] = 19;
	mas[18] = 13;
	mas[19] = 22;
	mas[20] = 9;
	mas[21] = 15;
	mas[22] = 5;
	mas[23] = 12;
	mas[24] = 0;
	mas[25] = 16;

	int T;
	char c;
	scanf("%d%c", &T, &c);
	FOR (t, 0, T) {
		printf("Case #%d: ", t + 1);
		string s;
		getline(cin, s);
		FOR (i, 0, s.sz)
			if (s[i] >= 'a' && s[i] <= 'z')
				s[i] = mas[s[i] - 'a'] + 'a';
		printf("%s\n", s.c_str());
	}

#ifdef MYDEBUG
    fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0 * (clock() - beg) / CLOCKS_PER_SEC);
#endif
	return 0;
}
