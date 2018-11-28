
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N - 1; i >= 0; --i)

#define ABS(N) (((N) < 0) ? (-(N)) : (N))
#define MIN(A, B) (((A) < (B)) ? (A) : (B))
#define MAX(A, B) (((A) > (B)) ? (A) : (B))
#define EPS 1e-7
#define ALL(V) V.begin(), V.end()
#define pb push_back
#define mp make_pair
#define Pi 3.14159265358979323846
#define SIZE(V) V.size()


typedef vector <int> VI;
typedef pair <int, int> PI;
typedef long long Long;
typedef unsigned int Uint;
typedef unsigned long long ULong;
typedef unsigned char Uchar;

int res[] = {
1,
5,
27,
143,
751,
935,
607,
903,
991,
335,
47,
943,
471,
55,
447,
463,
991,
95,
607,
263,
151,
855,
527,
743,
351,
135,
407,
903,
791,
135,
647,
343,
471,
455,
847,
263,
191,
95
};

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int N;
	scanf("%d", &T);
	REP(I, T)
	{
		scanf("%d", &N);
		printf("Case #%d: %03d\n", I + 1, res[N]);
	}
	return 0;
}