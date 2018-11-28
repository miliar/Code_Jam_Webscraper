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
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 1005

int qnt[NMAX], len[NMAX];
int n, r, k;
int g[NMAX];

void solve(int tc)
{
    printf("Case #%d: ", tc);

    cerr << tc << endl;

    cin >> r >> k >> n;
    forn(i, n) cin >> g[i];

    forn(i, n)
    {
        qnt[i] = 0;
        len[i] = 0;
        int j = i;
        while (len[i] < n && qnt[i] + g[j] <= k)
        {
            qnt[i] += g[j];
            len[i]++;
            j = (j + 1) % n;    
        }
    }

    int s = 0;
    ll ans = 0;
    forn(i, r)
    {
        ans += qnt[s];
        s = (s + len[s]) % n;
    }

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
            
