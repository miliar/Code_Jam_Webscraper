#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <list>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <sstream>
#include <fstream>
#include <functional>
#include <deque>
#include <utility>
#include <memory>

using namespace std;

typedef long long int64;

const int INF = 1000 * 1000 * 1000;
const int64 INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-8;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forn1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define mp make_pair
#define pb push_back
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

int n;
char a[200][200];
double wp[200], owp[200], oowp[200];
int wg[200], pg[200];

void calculateGames()
{
    forn(i, n)
    {
        pg[i] = 0;
        wg[i] = 0;

        forn(j, n)
        {
            if (a[i][j] != '.')
                ++pg[i];
            if (a[i][j] == '1')
                ++wg[i];
        }
    }
}

void calculateWp()
{
    forn(i, n)
        wp[i] = (double)wg[i] / (double)pg[i];
}

void calculateOwp()
{
    forn(i, n)
    {
        double sum = 0.0;
        int count = 0;

        forn(j, n)
        {
            if (a[i][j] == '.')
                continue;

            ++count;
            sum += (double)(wg[j] - (a[i][j] == '0' ? 1 : 0)) / (double)(pg[j] - 1);
        }

        owp[i] = sum / (double)count;
    }
}

void calculateOowp()
{
    forn(i, n)
    {
        double sum = 0.0;
        int count = 0;

        forn(j, n)
        {
            if (a[i][j] == '.')
                continue;

            ++count;
            sum += owp[j];
        }

        oowp[i] = sum / (double)count;
    }
}

int main()
{
    //freopen("input.txt", "rt", stdin);

    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
        scanf("%d\n", &n);

        forn(i, n)
            scanf("%s", a[i]);

        calculateGames();
        calculateWp();
        calculateOwp();
        calculateOowp();

        printf("Case #%d:\n", test + 1);
        forn(i, n)
            printf("%.12lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }

    return 0;
}
