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
#define forn1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0) ? true : false

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

const string P = "welcome to code jam";

int z[1000][20];
string s;

int get(int posS, int posP)
{
    if (posP == 19)
        return 1;
    if (posS == (int)s.length())
        return 0;

    int& result = z[posS][posP];
    if (result != -1)
        return result;

    result = get(posS + 1, posP);
    if (s[posS] == P[posP])
        result += get(posS + 1, posP + 1);

    return result % 10000;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d\n", &tests);

    forn(test, tests)
    {
        getline(cin, s);
        memset(z, 255, sizeof(z));
        printf("Case #%d: %04d\n", test + 1, get(0, 0));
    }

    return 0;
}
