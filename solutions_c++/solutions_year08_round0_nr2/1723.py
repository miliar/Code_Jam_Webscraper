#include <cstdio>
#include <utility>
#include <mem.h>

#define f(i, n)				for(int i = 0; i < (n); i ++)

struct tr
{
	int st, end;
};

int T, t, time;
tr A[240], B[240];
int a, b;

bool gA[240][240], gB[240][240];

bool used[240];
int parent[240];

bool dfsA(int st)
{
	f(i, b) if( (gA[st][i]) && (used[i] == 0 ) )
	{
		used[i] = 1;
		if( (parent[i] == -1) || dfsA( parent[i] ) )
		{
			parent[i] = st;
			return 1;
		}
	}
	return 0;
}

bool dfsB(int st)
{
if(t == 30000) printf("%d\n", st);
	f(i, a) if( (gB[st][i]) && (used[i] == 0) )
	{
if(t == 30000) printf("%d %d\n", st, i);
		used[i] = 1;
		if( (parent[i] == -1) || dfsB( parent[i] ) )
		{
			parent[i] = st;
			return 1;
		}
	}
	return 0;
}

int matchA()
{
	int res = 0;
	memset(parent, -1, sizeof(parent));
if(t == 30000)	printf("in A\n");
	f(i, b)
	{
		memset(used, 0, sizeof(used));
		int t = dfsB(i);
		if( t )	res ++;
if(::t == 30000)		printf("%d %d\n", i, t);
	}
	return a - res;
}

int matchB()
{
	int res = 0;
	memset(parent, -1, sizeof(parent));
if(t == 30000)	printf("in B\n");
	f(i, a)
	{
		memset(used, 0, sizeof(used));
		int t = dfsA(i);
		if( t )	res ++;
if(::t == 30000)		printf("%d %d\n", i, t);
	}
	return b - res;
}

int main()
{
    scanf("%d", &T);
    for(t = 0; t < T; t ++)
    {
		memset(gA, 0, sizeof(gA));
		memset(gB, 0, sizeof(gB));
		scanf("%d", &time);
		scanf("%d %d", &a, &b);
		int h, m;
		f(i, a)
		{
			scanf("%d:%d", &h, &m);
			A[i].st = 60 * h + m;
			scanf("%d:%d", &h, &m);
			A[i].end = 60 * h + m;
			if(t == 30000)printf("%d %d\n", A[i].st, A[i].end);
		}
		f(i, b)
		{
			scanf("%d:%d", &h, &m);
			B[i].st = 60 * h + m;
			scanf("%d:%d", &h, &m);
			B[i].end = 60 * h + m;
			if(t == 30000)printf("%d %d\n", B[i].st, B[i].end);
		}
		f(i, a)
			f(j, b)
			{
				if( A[i].end + time <= B[j].st )	gA[i][j] = 1;
				if( B[j].end + time <= A[i].st )	gB[j][i] = 1;
			}
//if(t == 30000)		f(i, a){ f(j, b) printf("%d", gA[i][j]); printf("\n"); }
//if(t == 30000)		f(i, a){ f(j, b) printf("%d", gB[i][j]); printf("\n"); }
		printf("Case #%d: %d %d\n", t + 1, matchA(), matchB());
    }
    return 0;
}
