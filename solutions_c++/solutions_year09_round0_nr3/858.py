#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
using namespace std;
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()
const string pat = "welcome to code jam";
string s;
const int MOD = 10000;
int n, m;

int d[22][506];

void solve(int tc)
{
    getline(cin, s);
    n = s.size();
    m = pat.size();
    forn(i, 22) forn(j, 506) d[i][j] = 0;
    d[0][0] = 1;
    forn(i, m+1)
    {
        forv(j, s)
        {
            if (i < m && pat[i] == s[j])
            {
                d[i+1][j+1] += d[i][j];
                d[i+1][j+1] %= MOD;
            }
            d[i][j+1] += d[i][j];
            d[i][j+1] %= MOD;
        }
    }
    int ans = d[m][n];
    printf("Case #%d: ", tc);
    if (ans < 1000) cout << 0;
    if (ans < 100) cout << 0;
    if (ans < 10) cout << 0;
    cout << ans << endl;
}

int main()
{
    int tc;
    string s;
    getline(cin, s);
    tc = atoi(s.c_str());
    forn(it, tc) solve(it+1);
}