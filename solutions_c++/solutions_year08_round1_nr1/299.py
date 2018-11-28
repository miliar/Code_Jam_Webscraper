
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

#define SZ (1 << 20)

int T;
int N;
Long A[SZ];
Long B[SZ];
int t;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	REP(I, T)
	{
		scanf("%d", &N);
		REP(i, N)
		{
			scanf("%d", &t);
			A[i] = t;
		}
		REP(i, N)
		{
			scanf("%d", &t);
			B[i] = t;
		}
		sort(A, A + N);
		sort(B, B + N, greater <Long>());
		Long res = 0;
		REP(i, N)
			res += A[i]*B[i];
		printf("Case #%d: %lld\n", I + 1, res);
	}
	return 0;
}