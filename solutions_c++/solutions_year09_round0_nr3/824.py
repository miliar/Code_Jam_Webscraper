#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define NMAX 505
#define MMAX 20

string s = "welcome to code jam";
string t;

int d[NMAX][MMAX];
int n, m;

void solve(int tc)
{
    printf("Case #%d: ", tc);

    getline(cin, t);

    memset(d, 0, sizeof(d));

    m = s.size();
    n = t.size();

    d[0][0] = 1;

    forn(i, n)
    {
        forn(j, m)
        {
            if (d[i][j] == 0) continue;

            for (int k = i; k < n; k++)
            {
                if (t[k] == s[j])
                {
                    d[k + 1][j + 1] = (d[k + 1][j + 1] + d[i][j]) % 10000;
                }
            }
        }
    }

    int ans = 0;
    forn(i, n + 1) ans = (ans + d[i][m]) % 10000;
    
    printf("%04d\n", ans);
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    string st;
    getline(cin, st);
    int tc = atoi(st.c_str());

    forn(it, tc) solve(it + 1);
    return 0;
}
            
