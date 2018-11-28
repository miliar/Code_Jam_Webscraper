#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<set>
#include<algorithm>
using namespace std;

typedef struct Point
{
	int r, c;
	Point() {}
	Point(int a, int b):r(a), c(b) {}
	inline bool operator<(const struct Point &a) const
	{
		if(r != a.r) return r < a.r;
		else return c < a.c;
	}
	inline bool operator==(const struct Point &a) const
	{
		return r == a.r && c == a.c;
	}
}Point;

int csK, csN;
int R, C, nB, nG, ans;
long long start, goal;
char M[16][16], dr[4] = {1, 0, -1, 0}, dc[4] = {0, 1, 0, -1};
Point B[8], G[8];
set<long long> S;
list<int> step;
list<long long> Q;

inline long long encode(Point *p)
{
	long long s = 0;
	for(int i = 0; i < nB; ++i)
		s = s*169 + p[i].r*13 + p[i].c;
	return s;
}

inline void decode(long long x, Point *p)
{
	for(int i = nB-1; i >= 0; --i)
	{
		p[i].c = x % 13;
		x /= 13;
		p[i].r = x % 13;
		x /= 13;
	}
}

inline bool isConnected(Point *a, Point *b)
{
	return (a->r == b->r && abs(a->c-b->c) <= 1) || (a->c == b->c && abs(a->r-b->r) <= 1);
}

inline bool isDangerous(Point *p)
{
	int i, j, con[8][8] = {0}, q[8], qt, ok[8] = {0};
	for(i = 0; i < nB; ++i)
		for(j = i+1; j < nB; ++j)
			if(isConnected(p+i, p+j))
				con[i][j] = con[j][i] = 1;
	q[0] = 0, qt = 1;
	ok[0] = 1;
	for(i = 0; i < qt; ++i)
	{
		for(j = 0; j < nB; ++j)
			if(!ok[j] && con[q[i]][j])
				ok[j] = 1, q[qt++] = j;
	}
	return qt < nB;
}

int main()
{
	int i, j, k, m, t, s;
	long long tmp;
	Point nxt[8];
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &R, &C);
		for(i = 1; i <= R; ++i)
		{
			scanf("%s", M[i]+1);
			M[i][0] = M[i][C+1] = '#';
		}
		for(i = 0; i <= C+1; ++i)
			M[0][i] = M[R+1][i] = '#';
		nB = nG = 0;
		for(i = 1; i <= R; ++i)
			for(j = 1; j <= C; ++j)
				if(M[i][j] == 'o')
					B[nB++] = Point(i, j), M[i][j] = '.';
				else if(M[i][j] == 'x')
					G[nG++] = Point(i, j), M[i][j] = '.';
				else if(M[i][j] == 'w')
					B[nB++] = Point(i, j), G[nG++] = Point(i, j), M[i][j] = '.';
		sort(B, B+nB);
		sort(G, G+nG);
		S.clear();
		start = encode(B);
		goal = encode(G);
		if(start == goal)
		{
			printf("Case #%d: 0\n", csK);
			continue;
		}
		S.insert(start);
		Q.clear();
		Q.push_back(start);
		step.clear();
		step.push_back(0);
		ans = -1;
		while(!Q.empty() && ans == -1)
		{
			s = step.front();
			step.pop_front();
			tmp = Q.front();
			Q.pop_front();
			decode(tmp, B);
//			fprintf(stderr, "%d: (%d,%d) (%d,%d) (%d,%d)\n", s, B[0].r, B[0].c, B[1].r, B[1].c, B[2].r, B[2].c);
			m = isDangerous(B);
			for(i = 0; i < nB; ++i)
			{
				for(j = 0; j < 4; ++j)
				{
					for(k = 0; k < nB; ++k) nxt[k] = B[k];
	//					fprintf(stderr, "\t%d %d", i, j);
					if(M[nxt[i].r+dr[j]][nxt[i].c+dc[j]] != '.' ||
							M[nxt[i].r-dr[j]][nxt[i].c-dc[j]] != '.')
					{
	//					fprintf(stderr, "\t\t meat #\n");
						continue;
					}
					for(k = 0; k < nB; ++k)
						if(nxt[k].r == nxt[i].r-dr[j] && nxt[k].c == nxt[i].c-dc[j]) break;
						else if(nxt[k].r == nxt[i].r+dr[j] && nxt[k].c == nxt[i].c+dc[j]) break;
					if(k < nB)
					{
	//					fprintf(stderr, "\t\tmeat box\n");
						continue;
					}
					nxt[i].r += dr[j], nxt[i].c += dc[j];
					sort(nxt, nxt+nB);
					tmp = encode(nxt);
					if(tmp == goal)
					{
						ans = s + 1;
						break;
					}
					if((!m || !isDangerous(nxt)) && S.find(tmp) == S.end())
					{
	//					fprintf(stderr, "\t\tpush (%d,%d) (%d,%d) (%d,%d)\n",
	//						nxt[0].r, nxt[0].c, nxt[1].r, nxt[1].c, nxt[2].r, nxt[2].c);
						Q.push_back(tmp), step.push_back(s+1), S.insert(tmp);
					}
	//				else fprintf(stderr, "\t\tdang (%d,%d) or find\n", m, isDangerous(nxt));
				}
				if(j < 4) break;
			}
		}
		printf("Case #%d: %d\n", csK, ans);
	}
}
