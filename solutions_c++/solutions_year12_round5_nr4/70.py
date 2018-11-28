#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

char eqv[255];
int din[255], dout[255];
int g[255][255];

void solve(int test)
{
    printf("Case #%d: ", test);

    int k;
    scanf("%d\n", &k);
    string s;
    getline(cin, s);

    memset(din, 0, sizeof(din));
    memset(dout, 0, sizeof(dout));

    memset(g,0, sizeof(g));

    forn(i, (int)s.size() - 1)
    {
        g[s[i]][s[i + 1]]++;

        if (eqv[s[i]])
        {
            g[eqv[s[i]]][s[i + 1]]++;
        }
        if (eqv[s[i + 1]])
        {
            g[s[i]][eqv[s[i + 1]]]++;
            if (eqv[s[i]])
            {
                g[eqv[s[i]]][eqv[s[i + 1]]]++;
            }
        }
    }

    int ans = 0;
    forn(i, 255) 
    {
        forn(j, 255)
        {
            if (g[i][j]) 
            {
                g[i][j] = 1;
                ans++;
                din[j]++;
                dout[i]++;
            }
        }
    }

    int p = 0;
    forn(i, 255)
    {
        p += max(din[i] - dout[i], 0);
    }
    if (p == 0) p++;
    cout << ans + p << endl;

}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    eqv['o'] = '0';
    eqv['i'] = '1';
    eqv['e'] = '3';
    eqv['a'] =  '4';
    eqv['s'] = '5';
    eqv['t'] = '7';
    eqv['b'] = '8';
    eqv['g'] = '9';

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}