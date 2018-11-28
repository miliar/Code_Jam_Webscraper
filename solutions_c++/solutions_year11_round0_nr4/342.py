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

void solve(int test)
{
    printf("Case #%d: ", test);

    int n; cin >> n;

    vector<int> p(n);

    forn(i, n)
    {
        cin >> p[i]; p[i]--;
    }

    vector<int> len;

    vector<bool> used(n, false);

    forn(i, n)
    {
        if (used[i]) continue;

        int u = i;

        int cur = 1;

        while (p[u] != i)
        {
            cur++;
            u = p[u];
            used[u] = true;  
        }

        used[u] = true;

        len.pb(cur);
    }

    int ans = 0;
    forv(i, len)
    {
        if (len[i] == 1) continue;
        ans += len[i];
    }

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}