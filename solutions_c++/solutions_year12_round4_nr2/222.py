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

const int N = 10000;
const int INF = 1000000000;

int n, w, l;
int result;
int r[N];

void readTestCase(int testCase)
{
    cin >> n >> w >> l;
    forn(i, n)
        cin >> r[i];
}

int x[N], y[N], d[N];

bool cross(int l1, int r1, int l2, int r2)
{
    return max(l1, l2) < min(r1, r2);
}

bool cross(int x1, int y1, int d1, int x2, int y2, int d2)
{
    return cross(x1, x1 + 2 * d1, x2, x2 + 2 * d2) &&
        cross(y1, y1 + 2 * d1, y2, y2 + 2 * d2);
}

bool ok(int n, int& X, int& Y, int D)
{
    if (X + D < 0)
        X = -D;

    if (Y + D < 0)
        Y = -D;

    if (X + D < 0 || X + D > w || Y + D < 0 || Y + D > l)
        return false;

    forn(i, n)
        if (cross(x[i], y[i], d[i], X, Y, D))
            return false;

    return true;
}

double rx[N], ry[N];

void solveTestCase(int testCase)
{
    cout << "Case #" << testCase << ":";

    vector<int> perm(n);
    forn(i, n)
        perm[i] = i;

    /*
    vector<pair<int,int> > pp;
    forn(i, n)
        pp.push_back(make_pair(r[i], i));
    sort(pp.begin(), pp.end());
    reverse(pp.begin(), pp.end());
    forn(i, n)
    {
        r[i] = pp[i].first;
        perm[i] = pp[i].second;
    }
    */

    while (true)
    {
        vector<int> a, b;
        a.push_back(-r[perm[0]]);
        b.push_back(-r[perm[0]]);

        bool yes = true;

        forn(i, n)
        {
            bool found = false;

            forn(j, a.size())
            {
                int aa = a[j], bb = b[j];
                if (ok(i, aa, bb, r[perm[i]]))
                {           
                    x[i] = aa;
                    y[i] = bb;
                    d[i] = r[perm[i]];

                    rx[perm[i]] = x[i] + d[i];
                    ry[perm[i]] = y[i] + d[i];

                    found = true;
                    
                    a.erase(a.begin() + j, a.begin() + j + 1);
                    b.erase(b.begin() + j, b.begin() + j + 1);

                    break;
                }
            }

            if (!found)
            {
                cerr << "FAILED!" << endl;
                yes = false;
                break;
            }

            a.push_back(x[i]);
            b.push_back(y[i] + 2 * d[i]);

            a.push_back(x[i] + 2 * d[i]);
            b.push_back(y[i]);
        }

        if (yes)
            break;

        random_shuffle(perm.begin(), perm.end());
    }

    forn(i, n)
    {
        printf(" %.2lf %.2lf", rx[i], ry[i]);
    }

    cout << endl;
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
