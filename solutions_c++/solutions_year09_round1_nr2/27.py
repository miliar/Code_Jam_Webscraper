#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;

typedef struct Node
{
	int r, c, k;
	long long t;
	Node() {}
	Node(int x, int y, int z, long long u):r(x), c(y), k(z), t(u) {}
	bool operator<(const struct Node &a) const
	{
		return t > a.t;
	}
}Node;

int csN, csK;
int R, C;
long long S[32][32], W[32][32], N[32][32], T[32][32], last[32][32][4];
priority_queue<Node> PQ;

inline void relax(int r, int c, int k, long long t)
{
	if(t < last[r][c][k])
	{
		last[r][c][k] = t;
		PQ.push(Node(r, c, k, t));
	}
}

inline long long getNextGreenNS(int r, int c, long long t)
{
	long long q = t % N[r][c]; 
	q = (q-T[r][c]) % N[r][c];
	if(q < S[r][c]) return t;
	else return t + N[r][c] - q;
}

inline long long getNextGreenEW(int r, int c, long long t)
{
	long long q = t % N[r][c]; 
	q = (q-T[r][c]+W[r][c]) % N[r][c];
	if(q < W[r][c]) return t;
	else return t + N[r][c] - q;
}

int main()
{
	int i, j;
	long long ns, ew;
	Node tmp;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &R, &C);
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				scanf("%lld %lld %lld",
						&S[i][j], &W[i][j], &T[i][j]);
				N[i][j] = S[i][j] + W[i][j];
				T[i][j] = T[i][j]%N[i][j] - N[i][j];
			}
		}
		memset(last, 63, sizeof(last));
		while(!PQ.empty()) PQ.pop();
		last[R-1][0][0] = 0;
		PQ.push(Node(R-1, 0, 0, 0));
		while(!PQ.empty())
		{
			tmp = PQ.top();
			PQ.pop();
		//	fprintf(stderr, "pop %d %d %d %lld\n", tmp.r, tmp.c, tmp.k, tmp.t);
			if(tmp.r == 0 && tmp.c == C-1 && tmp.k == 2) break;
			if(last[tmp.r][tmp.c][tmp.k] != tmp.t) continue;
			ns = getNextGreenNS(tmp.r, tmp.c, tmp.t);
			ew = getNextGreenEW(tmp.r, tmp.c, tmp.t);
			relax(tmp.r, tmp.c, tmp.k^3, ns+1);
			relax(tmp.r, tmp.c, tmp.k^1, ew+1);
			if(tmp.k == 0)
			{
				if(tmp.r+1 < R) relax(tmp.r+1, tmp.c, 3, tmp.t+2);
				if(tmp.c > 0) relax(tmp.r, tmp.c-1, 1, tmp.t+2);
			}
			else if(tmp.k == 1)
			{
				if(tmp.r+1 < R) relax(tmp.r+1, tmp.c, 2, tmp.t+2);
				if(tmp.c+1 < C) relax(tmp.r, tmp.c+1, 0, tmp.t+2);
			}
			else if(tmp.k == 2)
			{
				if(tmp.r > 0) relax(tmp.r-1, tmp.c, 1, tmp.t+2);
				if(tmp.c+1 < C) relax(tmp.r, tmp.c+1, 3, tmp.t+2);
			}
			else if(tmp.k == 3)
			{
				if(tmp.r > 0) relax(tmp.r-1, tmp.c, 0, tmp.t+2);
				if(tmp.c > 0) relax(tmp.r, tmp.c-1, 2, tmp.t+2);
			}
		}
		printf("Case #%d: %lld\n", csK, last[0][C-1][2]);
	}
}
