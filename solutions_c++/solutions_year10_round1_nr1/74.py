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

using namespace std;

#define maxn 55

int n, k;
char b[maxn][maxn], br[maxn][maxn];

void rotate()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			br[j][n-1-i] = b[i][j];
}

void drop()
{
	for (int i = n-1; i >= 0; i--)
		for (int j = 0; j < n; j++)
		{
			int t = i;
			while (t + 1 < n && br[t+1][j] == '.')
			{
				swap(br[t][j], br[t+1][j]);
				t++;
			}
		}
}

bool check(char c)
{	
	// hor
	for (int i = 0; i < n; i++)
		for (int j = 0; j + k <= n; j++)
		{
			int t = 0;
			for (int q = 0; q < k; q++) if (br[i][j+q] == c) t++;
			if (t == k)
			{
				return true;
			}
		}
	// ver
	for (int i = 0; i + k <= n; i++)
		for (int j = 0; j < n; j++)
		{
			int t = 0;
			for (int q = 0; q < k; q++) if (br[i+q][j] == c) t++;
			if (t == k)
			{
				return true;
			}
		}
	// diag 1
	for (int i = 0; i + k <= n; i++)
		for (int j = 0; j + k <= n; j++)
		{
			int t = 0;
			for (int q = 0; q < k; q++) if (br[i+q][j+q] == c) t++;
			if (t == k)
			{
				return true;
			}
		}
	// diag 2
	for (int i = 0; i + k <= n; i++)
		for (int j = 0; j + k <= n; j++)
		{
			int t = 0;
			for (int q = 0; q < k; q++) if (br[i+q][j+k-q-1] == c) t++;
			if (t == k)
			{
				return true;
			}
		}
	return false;
}

void print()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			printf("%c", br[i][j]);
		printf("\n");
	}
	printf("\n");
}

void solvecase() {
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", b[i]);
	}
	//print();
	rotate();
	//print();
	drop();
	//print();
	{
		bool r, b;
		r = check('R');
		b = check('B');
		if (r)
		{
			printf("%s", b ? "Both" : "Red");
		}
		else
		{
			printf("%s", b ? "Blue" : "Neither");
		}
	}
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	//freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}