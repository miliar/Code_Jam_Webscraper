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

int l, d;

vector<string> dict;

vector<set<char> > parse(const string& s)
{
    vector<set<char> > result(l);

    int pos = 0;

    forn(i, l)
    {
        if (s[pos] == '(')
        {
            ++pos;
            while (s[pos] != ')')
            {
                result[i].insert(s[pos]);
                ++pos;
            }
            ++pos;
        }
        else
        {
            result[i].insert(s[pos]);
            ++pos;
        }
    }

    return result;
}

bool ok(const vector<set<char> >& w, const string& s)
{
    forn(i, l)
        if (w[i].count(s[i]) == 0)
            return false;
    return true;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d%d%d", &l, &d, &tests);
    dict.resize(d);
    forn(i, d)
        cin >> dict[i];

    forn(test, tests)
    {
        string word;
        cin >> word;
        vector<set<char> > w = parse(word);
        int cnt = 0;
        forn(i, d)
            if (ok(w, dict[i]))
                ++cnt;
        printf("Case #%d: %d\n", test + 1, cnt);
    }

    return 0;
}
