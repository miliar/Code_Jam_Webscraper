#pragma comment(linker, "/STACK:1000000000")

#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstring>
#include <utility>
#include <memory>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(n)) != 0) ? true : false

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

int s, q;
string engine[200], query[2000];
int d[2000][200];

int get(int processed, int currentEngine)
{
	if (processed == q)
		return 0;

	int& result = d[processed][currentEngine];
	
	if (result != -1)
		return result;

	result = INF;

	forn(i, s)
		if (query[processed] != engine[i])
		{
			int t = get(processed + 1, i);
			if (currentEngine != i)
				++t;

			result = min(result, t);
		}

    return result;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
    	scanf("%d\n", &s);
    	forn(i, s)
    		getline(cin, engine[i]);

    	scanf("%d\n", &q);
    	forn(i, q)
    		getline(cin, query[i]);

    	memset(d, 255, sizeof(d));

    	int result = get(0, 150) - 1;
    	result = max(result, 0);

        printf("Case #%d: %d\n", test + 1, result);
    }

    return 0;
}
