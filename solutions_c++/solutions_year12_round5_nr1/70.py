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

const int N = 1000000000;
const int INF = 1000000000;

int n, m;
int result;

struct level
{
    int p, l, id;
};

vector<level> levels;

bool operator <(const level& a, const level& b)
{
    /*
    if (a.p < b.p)
        return true;
    if (a.p > b.p)
        return false;
    if (a.l > b.l)
        return true;
    if (a.l < b.l)
        return false;
    */

    if ((100 - a.p) * b.l != (100 - b.p) * a.l)
        return (100 - a.p) * b.l > (100 - b.p) * a.l;

    return a.id < b.id;
}

void readTestCase(int testCase)
{
    cin >> n;
    levels = vector<level>(n);
    forn(i, n)
        cin >> levels[i].l;
    forn(i, n)
    {
        cin >> levels[i].p;
        levels[i].p = 100 - levels[i].p;
    }
    forn(i, n)
        levels[i].id = i;
}
/*
double cost()
{
    double result = 0;

    forn(i, n)
    {
        result = (levels[i].l + result) / (levels[i].p / 100.0);
    }

    return result;
}
*/

void solveTestCase(int testCase)
{
    cout << "Case #" << testCase << ":";

    sort(levels.begin(), levels.end());
    vector<level> result;

    /*
    vector<level> ini = levels;

    vector<int> idx;
    double best = 1E20;

    do
    {
        double c = cost();
        vector<int> cad;
        forn(i, n)
            cad.push_back(levels[i].id);
        //cout << c << endl;
        if (c + 1E-9 < best)
        {
            best = c;
            result = levels;
            idx = cad;
            cout << "**" << endl;
        }
        else
        {
            if (fabs(c - best) < 1E-9)
            {
                if (cad < idx)
                {
            best = c;
                    result = levels;
                    idx = cad;
            cout << "**" << endl;
                }
            }
        }
    }
    while (next_permutation(levels.begin(), levels.end()));

    if (ini < result || ini > result)
    {
        for(;;)
        {
        }
    }
    */
    
    result = levels;
    
    forn(i, n)
        cout << " " << result[i].id;

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
