#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#if defined LOCAL_RUN || defined _DEBUG
#   define DEBUG_OUTPUT
#   include "local_run.h"
#else
#   define _(x) void(0)
#endif

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long long li;
typedef long double ld;

using namespace std;

const int N = 2100000;
const int INF = 1000000000;

int n, m, f;
int result;

struct food
{
    int p, t;
};

bool operator <(const food& a, const food& b)
{
    return a.t < b.t;
}

vector<food> foods;

int z[N], w[N];
int nz;

void readTestCase(int testCase)
{
    cin >> m >> f >> n;

    foods = vector<food>(n);

    forn(i, n)
        cin >> foods[i].p >> foods[i].t;
}

void solveTestCase(int testCase)
{
    cout << "Case #" << testCase << ": ";

    sort(foods.begin(), foods.end());

    vector<int> pre(n + 1, INF);

    for (int i = n - 1; i >= 0; i--)
        pre[i] = min(pre[i + 1], foods[i].p);

    int result = 0;

    int minp = INF;
    forn(i, n)
        minp = min(minp, foods[i].p);

    int cost = f;
    int mm = m - f;
    nz = 0;
    for (int day = 0;; day++)
    {
        if (mm <= 0)
            break;

        food ff = {0, day};
        int pos = lower_bound(foods.begin(), foods.end(), ff) - foods.begin();
        int minv = pre[pos];

        if (minv > mm)
            break;

        cost += minv;
        mm -= minv;

        z[nz++] = cost;
    }

    forn(i, m + 1)
        w[i] = INF;
    w[0] = 0;

    //cerr << m << " " << nz << endl;

    forn(i, m + 1)
    {
        //if (i % 1000 == 0)
        //    cout << "=" << i << endl;

        if (w[i] == INF)
        {
            result = i - 1;
            break;
        }

        int lim = min(nz, 20000);

        forn(j, lim)
        {
            if (w[i] + z[j] > m)
                break;
            if (w[i + j + 1] > w[i] + z[j])
            {
                w[i + j + 1] = w[i] + z[j];
                //cout << "*" << endl;
            }
            //else
            //    break;
        }

        for (int j = nz - lim - 1; j < nz; j++)
        {
            if (w[i] + z[j] > m)
                break;
            if (w[i + j + 1] > w[i] + z[j])
            {
                w[i + j + 1] = w[i] + z[j];
                //cout << "*" << endl;
            }
            //else
            //    break;
        }
    }

    cout << result << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);

    if (argc != 1 && argc != 3)
    {
        cout << "Usage: solution.exe [<first-test> <last-test>] (1-based)" << endl;
        return 1;
    }

    int testCount;
    string line;
    getline(cin, line);
    sscanf(line.c_str(), "%d", &testCount);

    int beginTestCase = 1;
    int endTestCase = testCount;

    if (argc == 3)
    {
        beginTestCase = max(beginTestCase, atoi(argv[1]));
        endTestCase = min(endTestCase, atoi(argv[2]));
    }

    for (int testCase = 1; testCase <= testCount; testCase++)
    {
        readTestCase(testCase);

        if (beginTestCase <= testCase && testCase <= endTestCase) {
            solveTestCase(testCase);
        }
    }

    return 0;
}
