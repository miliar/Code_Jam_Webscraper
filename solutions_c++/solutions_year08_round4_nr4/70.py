#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef signed long long i64;  
typedef unsigned long long u64;
typedef long double real;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#define forr(i,n0,n1) for(int i=(n0); i<(n1); i++)
#define forn(i,n) for(int i=0; i<(n); i++)
#define fors(i,s) forn(i, (int)s.length())
#define forv(i,v) forn(i, (int)v.size())
#define fore(t, it, obj) for (t :: iterator it = obj.begin(); it != obj.end(); it++)

#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

string s, t;
int n;

int find(vector<int>& p)
{
    t = s;
    forn(i, s.length() / n)
    {
        forn(j, n)
        {
            t[i * n + p[j]] = s[i * n + j];
        }
    }

    int rle = 0;

    t = "#" + t;

    for (int i = 1; i < t.length(); i++)
        if (t[i] != t[i - 1])
            rle++;

    return rle;
}

int solve()
{
    vector<int> p(n);

    forn(i, n)
        p[i] = i;

    int result = s.length();

    do
    {
        result = min(result, find(p));
    }
    while (next_permutation(all(p)));

    return result;
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        cin >> n;
        cin >> s;
        cout << "Case #" << ta + 1 << ": " << solve() << endl;
    }

    return 0;
}
