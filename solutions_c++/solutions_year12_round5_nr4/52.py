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

int n, m, k;
int result;
string s;

char cc[256] = {0};

void readTestCase(int testCase)
{
    cc['o'] = '0';
    cc['i'] = '1';
    cc['e'] = '3';
    cc['a'] = '4';
    cc['s'] = '5';
    cc['t'] = '7';
    cc['b'] = '8';
    cc['g'] = '9';

    cin >> k;
    cin >> s;
}

void solveTestCase(int testCase)
{
    cout << "Case #" << testCase << ": ";

    char d[256] = {0};

    n = s.length();

    set<string> edges;

    forn(i, n - 1)
    {
        char a = s[i];
        char b = s[i + 1];

        vector<char> ca(1, a);
        if (cc[a] != 0)
            ca.push_back(cc[a]);

        vector<char> cb(1, b);
        if (cc[b] != 0)
            cb.push_back(cc[b]);

        forn(x, ca.size())
            forn(y, cb.size())
            {
                string f(2, ' ');
                f[0] = ca[x];
                f[1] = cb[y];
                edges.insert(f);
            }
    }

    for (set<string>::iterator i = edges.begin(); i != edges.end(); i++)
    {
        string x = *i;
        d[x[0]]++;
        d[x[1]]--;
    }

    int result = 0;

    forn(i, 256)
    {
        if (d[i] != 0)
        {
            result += abs(d[i]);
        }
    }

    if (result == 0)
    {
        result = edges.size() + 1;
    }
    else
    {          
        assert(result % 2 == 0);

        result = result / 2;
        result += edges.size();
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
