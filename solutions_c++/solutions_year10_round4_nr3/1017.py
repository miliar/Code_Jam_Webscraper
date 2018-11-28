#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>

using namespace std;

const int INF = 1000000000;

typedef long long int64; 
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }

#define MOD 10000003;

//////////////////////////////////////////////////////////////////////////

const int N = 300;
int a[N][N], a1[N][N];

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests_count;
	cin >> tests_count;



for (int test = 1; test <= tests_count; ++test) 
{
	fprintf(stderr, "Test: #%d\n", test);
	printf("Case #%d: ", test);

	int n;
	cin >> n;

	memset(a, 0, sizeof a);
	int count = 0;
	for (int i = 0; i < n ; i++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		for (int y = y1; y <= y2 ; y++)
		{
			for (int x = x1; x <= x2 ; x++)
			{
				if (!a[y][x]) count++;
				a[y][x] = 1;
			}
		}
	}

	memcpy(a1, a, sizeof a);

	int iters = 0;
	while (count > 0) {
		iters++;
		for (int y = N; y >= 1 ; y--)
		{
			for (int x = N; x >= 1 ; x--)
			{
				if (!a[y][x] && a[y-1][x] && a[y][x-1])
				{
					count++;
					a1[y][x] = 1;
				} else
				if (a[y][x] && !a[y-1][x] && !a[y][x-1]) 
				{
					count--;
					a1[y][x] = 0;
				}
			}
		}
		memcpy(a, a1, sizeof a);
	}

	

//	int res = rec (n);

	printf("%d", iters);



	printf("\n");
}

}