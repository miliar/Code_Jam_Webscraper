
#define _CRT_SECURE_NO_DEPRECATE 

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

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

#define SZ 250
#define INF (1 << 20)

int C[SZ][SZ];
int F[SZ][SZ];

int P[SZ][2];

int n;
int s;
int t;

int T;
int N;
int K;

int L[SZ][SZ];

int d[SZ][SZ];

int Q[SZ];
int h1;
int h2;

int FF()
{
	while(true)
	{
		memset(P, -1, sizeof(P));
		P[s][0] = -2;
		P[s][1] = INF;
		queue<int> Q;
		Q.push(s);
		int cur;
		while(!Q.empty())
		{
			cur = Q.front();
			Q.pop();
			REP(i, n)
				if(C[cur][i] - F[cur][i] > 0 && P[i][0] == -1)
				{
					P[i][0] = cur;
					P[i][1] = min(P[cur][1], C[cur][i] - F[cur][i]);
					Q.push(i);
				}
		}
		if(P[t][0] == -1)
		{
			int res = 0;
			REP(i, n)
				res += F[s][i];
			return res;
		}
		cur = t;
		while(cur != s)
		{
			F[P[cur][0]][cur] += P[t][1];
			F[cur][P[cur][0]] = -F[P[cur][0]][cur];
			cur = P[cur][0];
		}
	}
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	REP(I, T)
	{
		scanf("%d%d", &N, &K);
		REP(i, N)
			REP(j, K)
				scanf("%d", &L[i][j]);
		memset(d, 0, sizeof(d));
		REP(i, N)
			REP(j, N)
				REP(k, K)
				{
					if(L[i][k] == L[j][k] || ((L[i][0] < L[j][0]) ^ (L[i][k] < L[j][k])))
					{
						d[i][j] = 1;
						break;
					}
				}

		
		n = 2*N + 2;
		s = n - 2;
		t = n - 1;

		memset(C, 0, sizeof(C));
		memset(F, 0, sizeof(F));

		REP(i, N)
		{
			REP(j, N)
				if(d[i][j] == 0)
				{
					if(L[i][0] > L[j][0])
						C[i*2 + 1][j*2] = 1;
				}
			C[i*2][t] = 1;
			C[s][i*2 + 1] = 1;
		}

		printf("Case #%d: %d\n", I + 1, N - FF());
	}
	return 0;
}