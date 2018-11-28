#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
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
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UInt;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1<<30;
const int MAX = 1<<20;

int n, root;
int P[MAX];
vector < int > Q[MAX*2];
vector <int> D;
vector <int> DD;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("in.txt", "r", stdin);
	#endif

	cin >> n;
	for (int j = 0; j <= n; j ++)
	{
		if (j == 0)
		{
			FOR (i,2,n+1)
				Q[i + j].PB(j);
		}
		else
		{
			for (int i = 1; i*i <= j; i++)
				if (j % i == 0)
				{
					if (i != 1)
						Q[i+j].PB(j);
					if (i*i != j)
						Q[(j/i) + j].PB(j);
				}
		}
	}
	FOR (i,0,n)
	{
		int x = i, p = 2;
		while (p <= n)
		{
			if (x % p == 0)
			{
				x += (p-1);
				x = min(x, n-1);
				p ++;
			}
			else
			{
				int pos = upper_bound(ALL(Q[x + p]), x) - Q[x + p].begin() - 1;
				if (pos < 0)
				{
					x -= (n - p + 1);
					x = min(x, n-1);
					p = n+1;
				}
				else
				{
					int pp = p;
					p -= Q[x + p][pos] - x;
					x = Q[x + pp][pos];
					x = min(x, n-1);
				}
			}
		}
		P[x] = i;
	}
	FOR (i,0,n)
		printf("%d ", P[i] + 1);
	cout << endl;
	



	return 0;
}