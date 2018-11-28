#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

#define inf 100000000
#define maxn 1000005

using namespace std;

int start[maxn];
int game[1000];

bool solvegame(int n)
{	
	bool w = false;
	for (int i = n-1; i >= 0; i--)
		if (!w)
		{
			w = true;
		}
		else
		{
			if (game[i] == 1)
				w = false;
			else
				w = true;
		}
	return w;
}

bool check(int a, int b)
{	
	int n = 0;
	while (true)
	{
		if (a > b) swap(a, b);
		if (a == b) break;
		int t = b / a;
		b = b % a;
		if (b == 0)
		{
			game[n++] = t-1;
			break;
		}
		else
		{
			game[n++] = t;
		}
	}
	return solvegame(n);
}

bool check2(int a, int b)
{
	if (a < b)
		swap(a, b);
	if (a / b <= 1) return false;
	return true;
}

int gcd(int a, int b)
{
	return b == 0 ? a : gcd(b, a % b);
}

inline int cnt(int a, int b, int c, int d)
{
	int le = max(a, c);
	int rt = min(b, d);
	if (le > rt) return 0;
	return rt - le + 1;
}

void precalc()
{
	int cur = 1;
	for (int i = 1; i < maxn; i++)
	{
		while (!check(i, cur)) cur++;
		start[i] = cur;
	}
}

LL solvefast(int a1, int a2, int b1, int b2)
{
	LL res = 0;
	for (int i = a1; i <= a2; i++)
	{
		res += cnt(b1, b2, start[i], inf);
	}
	return res;
}

void solvecase() {
	LL res = 0, res2 = 0;
	int a1, a2, b1, b2;
	scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
	//for (int i = a1; i <= a2; i++)
	//	for (int j = b1; j <= b2; j++)
	//	{
	//		if (check(i, j)) res++;
	//		//if (check2(i, j)) res2++;
	//	}
	res2 += solvefast(a1, a2, b1, b2);
	res2 += solvefast(b1, b2, a1, a2);
	//assert(res == res2);
	printf("%lld", res2);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	precalc();
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}	
}

int main() {
	//freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}