//#pragma comment(linker, "/STACK:10000000")
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
typedef long long lint;

struct Seg
{
	int a, b;
	Seg(int a = 0, int b = 0) : a(a), b(b) {}
};

inline bool Intersect(Seg p, Seg q)
{
	if(q.a > p.b || p.a > q.b)
		return false;
	return true;
}
inline Seg Intersection(Seg p, Seg q)
{
	return Seg(min(p.a, q.a), max(p.b, q.b));
}

int DP[1011][1011];

int GetDP(int a, int b)
{
	if(DP[a][b] != -1)
		return DP[a][b];
	DP[a][b] = 1 << 20;
	for(int i = a + 1; i < b; ++i)
		DP[a][b] = min(DP[a][b], GetDP(a, i) + GetDP(i, b));
	return DP[a][b];
}

char E[111][1111];

bool Solve(int test)
{
	int S;
	scanf("%d\n", &S);
	for(int i = 0; i < S; ++i)
	{
		gets(E[i]);
	}
	int a[111];
	for(int i = 0; i < S; ++i)
		a[i] = 0;
	int Q;
	scanf("%d\n", &Q);
	for(int i = 0; i <= Q; ++i)
		for(int j = 0; j <= Q; ++j)
			DP[i][j] = -1;
	char buf[111];
	for(int i = 0; i < Q; ++i)
	{
		gets(buf);
		for(int j = 0; j < S; ++j)
		{
			if(!strcmp(buf, E[j]))
			{
				int x = a[j];
				int y = i;
				for(int aa = x; aa < y; ++aa)
					for(int bb = aa + 1; bb <= y; ++bb)
						DP[aa][bb] = 1;
				//DP[a[j]][i] = 1;
				a[j] = i + 1;
				break;
			}
		}
	}
	for(int i = 0; i < S; ++i)
		DP[a[i]][Q] = 1;
	printf("Case #%d: %d\n", test, GetDP(0, Q) - 1);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
		Solve(i + 1);
	//while(Solve(++t));
	return 0;
}