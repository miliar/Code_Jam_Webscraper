
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

int T;
int N;
int M;

bool B[1000][10][2];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	REP(I, T)
	{
		memset(B, 0, sizeof(B));
		scanf("%d%d", &N, &M);
		int k;
		REP(i, M)
		{
			scanf("%d", &k);
			int t;
			int a;
			REP(j, k)
			{
				scanf("%d%d", &t, &a);
				B[i][t - 1][a] = 1;
			}
		}
		int res = -1;
		int val;
		REP(i, 1 << N)
		{
			bool b = 1;
			REP(j, M)
			{
				bool bb = 0;
				REP(k, N)
					if((!(i & (1 << k)) && B[j][k][0]) || ((i & (1 << k)) && B[j][k][1]))
					{
						bb = 1;
						break;
					}
				if(!bb)
				{
					b = 0;
					break;
				}
			}
			if(b)
			{
				int valL = 0;
				REP(j, N)
					if(i & (1 << j))
						++valL;
				if(res == -1 || val > valL)
				{
					res = i;
					val = valL;
				}
			}
		}
		if(res == -1)
			printf("Case #%d: IMPOSSIBLE\n", I + 1);
		else
		{
			printf("Case #%d:", I + 1);
			REP(i, N)
				if(res & (1 << i))
					printf(" 1");
				else
					printf(" 0");
			printf("\n");
		}
	}
	return 0;
}