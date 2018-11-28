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

#define NMAX 10005

int n;
int x[NMAX], l[NMAX];
int d[NMAX];
bool used[NMAX];

int random(int n)
{
    return abs((rand() << 15) + rand()) % n;
}
void solve(int test)
{
    memset(d, 0,  sizeof(d));
    memset(used, 0, sizeof(used));

    printf("Case #%d: ", test);


    cerr << test << endl;
    scanf("%d", &n);
    forn(i, n) scanf("%d %d", &x[i], &l[i]);
    scanf("%d", &x[n]);
  
    /*
    n = 10000;
    vector<pii> v(n);
    forn(i, n)
    {
        v[i].first = random(1000000000) + 1;
        v[i].second = random(1000000000) + 1;
    }
    sort(all(v));
    forn(i, n)
    {
        x[i] = v[i].first;
        l[i] = v[i].second;
    }
    x[n] = 1000000000;
    */

    d[0] = x[0];
    queue<int> q;
    q.push(0);

    while (!q.empty())
    {
        int u = q.front(); q.pop();
        used[u] = false;
    
        if (x[u] + d[u] >= x[n])
        {
            cout << "YES\n";
            return;
        }

        for (int v = u + 1; v < n; v++)
        {
            if (x[u] + d[u] < x[v]) break;
            int tmp = min(l[v], x[v] - x[u]);
            if (tmp > d[v])
            {
                d[v] = tmp;
                if (!used[v]) 
                {
                    q.push(v);
                    used[v] = true;
                }
            }
        }
    } 

    cout << "NO\n";
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