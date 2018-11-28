
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

#define SZ 1200
#define INF 1234567

int C[SZ][SZ];
int F[SZ][SZ];
int P[SZ][2];

int n;
int s;
int t;

int FordFulkerson()
{
	while(true)
	{
		REP(i, n)
			P[i][0] = -1;
		P[s][0] = -2;
		P[s][1] = INF;
		queue <int> Q;
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
					P[i][1] = MIN(P[cur][1], C[cur][i] - F[cur][i]);
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
			F[ P[cur][0] ][cur] += P[t][1];
			F[cur][ P[cur][0] ] = -F[ P[cur][0] ][cur];
			cur = P[cur][0];
		}
	}
}


int N;
int M;

void add(int a, int b)
{
	C[a][b] = 1;
}

void solve()
{
	memset(C, 0, sizeof(C));
	memset(F, 0, sizeof(F));
	scanf("%d%d", &M, &N);
	n = N*M + 2;
	s = n - 2;
	t = n - 1;
	char ch;
	int cnt = 0;
	REP(i, M)
		REP(j, N)
		{
			ch = ' ';
			while(isspace(ch))
				scanf("%c", &ch);
			if(ch == '.')
			{
				if(j & 1)
				{
					add(s, i*N + j);
					add(i*N + j, i*N + j - 1);
					if(i)
						add(i*N + j, (i - 1)*N + j - 1);
					if(i < N - 1)
						add(i*N + j, (i + 1)*N + j - 1);
					if(j < N - 1)
					{
						add(i*N + j, i*N + j + 1);
						if(i)
							add(i*N + j, (i - 1)*N + j + 1);
						if(i < N - 1)
							add(i*N + j, (i + 1)*N + j + 1);
					}
				}
				else
					add(i*N + j, t);
			}
			else
				++cnt;
		}
	printf("%d\n", N*M - cnt - FordFulkerson());
}

int res[SZ][SZ];
int a[SZ];

void solve1()
{
	memset(res, -1, sizeof(res));
	memset(a, 0, sizeof(a));
	scanf("%d%d", &M, &N);
	char ch;
	REP(i, M)
		REP(j, N)
		{
			ch = ' ';
			while(isspace(ch))
				scanf("%c", &ch);
			if(ch == 'x')
				a[i] |= (1 << j);
		}
	res[0][0] = 0;
	FOR(i, 1, M + 1)
		REP(j, 1 << N)
		{
			if(j & a[i - 1])
				continue;
			bool b = 1;
			REP(k, N - 1)
				if((j & (1 << k)) &&(j & (1 << (k + 1))))
				{
					b = 0;
					break;
				}
			if(!b)
				continue;
			int cnt = 0;
			REP(k, N)
				if(j & (1 << k))
					++cnt;
			REP(k, 1 << N)
				if(res[i - 1][k] != -1 && !(j & (k << 1)) && !((j << 1) & k))
					res[i][j] = MAX(cnt + res[i - 1][k], res[i][j]);
		}
	int r = 0;
	REP(i, 1 << N)
		r = MAX(r, res[M][i]);
	printf("%d\n", r);
}

int c;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &c);
	REP(i, c)
	{
		printf("Case #%d: ", i + 1);
		solve1();
	}
	return 0;
}