#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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

using namespace std;

template<class T> inline const T& Max(const T& a, const T& b){return a > b ? a : b;}
template<class T> inline const T& Min(const T& a, const T& b){return a < b ? a : b;}
template<class T> inline T sqr(const T a) {return a * a;}
const double PI = acos(-1);

FILE *fin = fopen("prob1l.in", "r");
FILE *fout = fopen("prob1l.out", "w");

__int64 keyboard[1001][1001];
struct Letter
{
	int id;
	int fre;
};
__int64 letter[1001];
int P, K, L;

int cmp(const Letter& a, const Letter& b)
{
	return b.fre < a.fre;
}

int main()
{
	int test;
	fscanf(fin, "%d", &test);
//	scanf("%d", &test);
	int tt;
	for (tt=1; tt<=test; ++tt) {
		fprintf(fout, "Case #%d: ", tt);
		printf("Case #%d: ", tt);
		memset(keyboard, 0, sizeof keyboard);
		fscanf(fin, "%d%d%d", &P, &K, &L);
//		scanf("%d%d%d", &P, &K, &L);
		int i;
		for (i=0; i<L; ++i) {
			fscanf(fin, "%I64d", &letter[i]);
//			scanf("%d", &letter[i]);
		}
		sort(letter, letter + L);
		reverse(letter, letter + L);
		int pad = 0;
		for (i=0; i<L; ++i) {
			++keyboard[pad][0];
			keyboard[pad][keyboard[pad][0]] = i;
			pad = (pad + 1) % K;
		}
		__int64 ans = 0;
		for (i=0; i<K; ++i) {
			for (__int64 t=1; t<=keyboard[i][0]; ++t) {
				ans += (t * letter[keyboard[i][t]]);
			}
		}
		fprintf(fout, "%I64d\n", ans);
		printf("%I64d\n", ans);
	}

	return 0;
}