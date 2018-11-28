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

int n, b;
int ans;
vector<int> d[105];
int cnt[12][12];

bool can_add(int v)
{
    forv(i, d[v])
    {
        if (cnt[i][d[v][i]]) return false;
    }
    return true;
}

void add(int v, int c)
{
    forv(i, d[v]) cnt[i][d[v][i]] += c;
}

void rec(int s, int st)
{
    if (s < st) return;

    if (can_add(s))
    {
        ans++;       
    }    

    for (int k = st; (s - k) > k; k++)
    {
        if (!can_add(k)) continue;

        add(k, 1);

        rec(s - k, k + 1);

        add(k, -1); 
    }
}

void solve(int tc)
{
    printf("Case #%d: ", tc);
    cin >> n >> b;

    ans = 0;

    for1(i, n)
    {
        d[i].clear();
        int j = i;
        while (j > 0)
        {
            d[i].pb(j % b);
            j /= b;
        } 
    }

    rec(n, 1);

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
            
