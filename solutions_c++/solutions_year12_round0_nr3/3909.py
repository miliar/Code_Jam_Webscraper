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
    cerr << test << endl;
    printf("Case #%d: ", test);

    int a, b;
    cin >> a >> b;

    int ans = 0;
    for (int n = a; n <= b; n++)
    {
        char s[10];
        memset(s, 0, sizeof(s));

        sprintf(s, "%d", n);
        int l = strlen(s);

        set<int> used;

        forn(j, l)
        {
            rotate(s, s + 1, s + l);
            if (s[0] == '0') continue;
            int m;
            sscanf(s, "%d", &m);
            if (a <= m && m <= b && m > n && !used.count(m))
            {
                ans++;
                used.insert(m);
            }
        }
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