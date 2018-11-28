#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

#define NMAX 10005

int d[NMAX];
int x[NMAX], l[NMAX];
bool used[NMAX];
int D, n;

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);

    cin >> n;
    forn(i, n)
    {
        scanf("%d %d", &x[i], &l[i]);
    }
    cin >> D;

    forn(i, n) d[i] = 0;

    d[0] = x[0];

    forn(i, n) used[i] = false;

    forn(it, n)
    {
        int j = -1;
        forn(i, n)
        {
            if (!used[i] && (j == -1 || d[i] > d[j])) j = i;
        }

        if (d[j] == 0) break;

        used[j] = true;

        forn(i, n)
        {
            if (used[i]) continue;
            if (abs(x[i] - x[j]) <= d[j] && d[i] < min(abs(x[i] - x[j]), l[i]))            
            {
                d[i] = min(abs(x[i] - x[j]), l[i]);   
            }
        }
    }

    forn(i, n)
    {
        if (x[i] + d[i] >= D)
        {
            printf("YES\n");
            return;
        }
    }

    printf("NO\n");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
