#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define inf 0x3f3f3f3f

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;
typedef double real;

#define slen 20
#define maxl (1 << 9)
#define P 10000

char ss[slen] = "welcome to code jam";

char buf[maxl];

int tbl[maxl][slen];

inline void add(int& a, int b) {
	a += b;
	a %= P;
}

int main() {
	int t = 1, tc;
	scanf("%d", &tc);
	for(gets(buf); t <= tc; t++) {
		gets(buf);
		int l = strlen(buf), i, j;
		memset(tbl, 0, sizeof(tbl));
		tbl[0][0] = 1;
		for(i = 0; i < l; i++)
			for(j = 0; j < slen; j++) {
				if(buf[i] == ss[j])
					add(tbl[i+1][j+1], tbl[i][j]);
				add(tbl[i+1][j], tbl[i][j]);
			}
		//for(i = 0; i < l; i++, fprintf(stderr, "\n"))
		//	for(j = 0; j < slen; j++)
		//		fprintf(stderr, "%d ", tbl[i][j]);
		printf("Case #%d: %04d\n", t, tbl[l][slen-1]);
	}
	return 0;
}
