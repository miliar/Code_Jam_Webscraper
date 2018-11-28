#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cmath>
using namespace std;

#define eps 1e-9
#define pb push_back
#define mp make_pair
#define RE(i, a, b) for(int (i) = a; (i) < (int)(b); (i)++)
#define REF(i, a, b) RE(i, a, b + 1)
#define REP(i, n) RE(i, 0, n) 
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define SZ(v) ((int)(v).size())
template<class T>string toString(T a) { stringstream t; t << a; return t.str(); }

FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
FILE *fout = freopen("C.out", "w", stdout);

int main()
{
	int ncase;
	scanf("%d ", &ncase);
	for (int cases = 1; cases <= ncase; cases++) {
		int res = -1;
		int n;
		scanf("%d ", &n);
		vector<int> c(n, 0);
		for (int i = 0; i < n; i++) scanf("%d ", &c[i]);
		for (int i = 0; i < (1 << n); i++) {
			int ss = -1, sp = -1;
			int rss = 0, rsp = 0;
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) {
					if (ss == -1) ss = c[j]; else ss ^= c[j];
					rss += c[j];
				}
				else {
					if (sp == -1) sp = c[j]; else sp ^= c[j];
					rsp += c[j];
				}
			}
			if (ss == sp) {
				if (res < rss) res = rss;
			}
		}
		if (res == -1) printf("Case #%d: NO\n", cases);
		else printf("Case #%d: %d\n", cases, res);
	}
/*

int bitset;
// i 번 째 비 트 가 켜 져 있 다 면 ?
if(bitset & (1 << i))
// i 번 째 비 트 를 켠 다
bitset |= (1 << i);
// i 번 째 비 트 를 끈 다
bitset&= ~(1 << i);
 & : Bitwise AND
 | : Bitwise OR
 ^ : Bitwise XOR
 << : Shift left
 >> : Shift right
// i 번 째 비 트 를 토 글
bitset ^= (1 << i);
// 모 든 비 트 를 왼 쪽 으 로 한 칸 씩 옮 긴 다
bitset <<= 1;
// 마 지 막 비 트 를 끈 다
bitset = (bitset - 1) & bitset;

*/

//	fcloseall();
	return 0;
}
