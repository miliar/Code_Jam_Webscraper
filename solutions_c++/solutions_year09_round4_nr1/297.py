
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

#define SZ 100
#define INF (1 << 20)

int F[SZ][SZ];
int C[SZ][SZ];
int V[SZ][SZ];

int P[SZ][2];

int n;
int s;
int t;

int T;
int N;

int f()
{
	int res = 0;
	while(true)
	{
		memset(P, -1, sizeof(P));
		P[s][0] = -2;
		P[s][1] = 0;
		REP(I, n)
			REP(i, n)
				if(P[i][0] != -1)
					REP(j, n)
						if(C[i][j] - F[i][j] > 0)
						{
							if(P[j][0] == -1 || P[j][1] > P[i][1] + V[i][j])
							{
								P[j][0] = i;
								P[j][1] = P[i][1] + V[i][j];
							}
						}
		if(P[t][0] == -1)
		{
			int k = 0;
			REP(i, n)
				k += F[s][k];
			//if(k != N)
			//	throw 25;
			return res;
		}
		res += P[t][1];
		int cur = t;
		while(cur != s)
		{
			F[P[cur][0]][cur]++;
			F[cur][P[cur][0]]--;
			cur = P[cur][0];
		}
	}
}


char buf[1 << 17];

int L[100];

int res[100][100];

int solve(int a, int b)
{
	int &r = res[a][b];
	if(r != -1)
		return r;
	if(a + b == N)
		return r = 0;
	int cnt = 0;
	r = INF;
	REP(i, N)
		if(L[i] > a && L[i] <= N - b)
		{
			if(L[i] == a + 1)
				r = min(r, solve(a + 1, b) + cnt);
			else
				++cnt;
		}
	cnt = 0;
	RREP(i, N)
		if(L[i] > a && L[i] <= N - b)
		{
			if(L[i] == N - b)
				r = min(r, solve(a, b + 1) + cnt);
			else
				++cnt;
		}

	return r;
}

int R[100];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	gets(buf);
	sscanf(buf, "%d", &T);
	REP(I, T)
	{
		gets(buf);
		sscanf(buf, "%d", &N);
		memset(L , 0, sizeof(L));
		REP(i, N)
		{
			gets(buf);
			RREP(j, N)
				if(buf[j] == '1')
				{
					L[i] = j + 1;
					break;
				}
		}
		
		memset(R, -1, sizeof(R));
		REP(i, N)
			REP(j, N)
				if(L[j] <= i + 1 && R[j] == -1)
				{
					R[j] = i;
					break;
				}

		int r = 0;
		REP(i, N)
			FOR(j, i + 1, N)
				if(R[i] > R[j])
					++r;
		printf("Case #%d: %d\n", I + 1, r);

	}
	return 0;
}