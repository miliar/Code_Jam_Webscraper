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

#define NMAX 2005

int n;
int h[NMAX];
int next[NMAX];

ll det(int x1, int y1, int x2, int y2)
{
    return ll(x1) * y2 - ll(x2) * y1;
}

int find_next(int i)
{
    int k = i + 1;
    for (int j = i + 2; j < n; j++)
    {
        ll tmp = det(k - i, h[k] - h[i], j - i, h[j] - h[i]); 
        if (tmp > 0)
        {
            k = j;
        }
    }
    return k;
}

bool used[NMAX];
void solve(int test)
{
    cerr << test << endl;
    printf("Case #%d:", test);

    cin >> n;
    forn(i, n - 1) 
    {
        cin >> next[i];
        next[i]--;
    }
    memset(used, 0, sizeof(used));

    h[n - 1] = 1000000000;
    used[n - 1] = true;


    int step = 1;
    forn(i, n)
    {
        if (used[i]) continue;
        vector<int> path;
        int u = i;
        while (!used[u])
        {
            path.pb(u);
            u = next[u];
        }
        
        reverse(all(path));
        forv(j, path)
        {
            h[path[j]] = h[u] - step * (u - path[j]);
            u = path[j];
            used[u] = true;
        }
        step++;
    }

    forn(i, n - 1)
    {
        if (find_next(i) != next[i])
        {
            cout << " Impossible\n";
            return;
        }
    }
    forn(i, n)
    {
        printf(" %d", h[i]);
    }
    printf("\n");
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