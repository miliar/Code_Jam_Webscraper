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

const int N = 1000000;
const int INF = 1000000000;

int n;
int d[N], l[N];
int D;
bool result;

void readTestCase(int testCase)
{
    cin >> n;
    forn(i, n)
        cin >> d[i] >> l[i];
    cin >> D;
}

void solveTestCase(int testCase)
{
    cout << "Case #" << testCase << ": ";

    vector<int> t(n, 0);
    t[0] = d[0];
    queue<int> q;
    q.push(0);
    set<int> in_q;
    in_q.insert(0);

    while (!q.empty())
    {
        int v = q.front();
        q.pop();
        in_q.erase(v);

        forn(i, n)
            if (d[i] > d[v] && d[i] - d[v] <= t[v])
            {
                int ti = min(l[i], d[i] - d[v]);
                if (ti > t[i])
                {
                    t[i] = ti;
                    if (!in_q.count(i))
                    {
                        q.push(i);
                        in_q.insert(i);
                    }
                }
            }
        
    }

    result = false;

    forn(i, n)
        if (d[i] + t[i] >= D && t[i] > 0)
            result = true;

    cout << (result ? "YES" : "NO") << endl;
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
