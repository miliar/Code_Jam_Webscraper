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

#define NMAX 1000006
int cp = 0;
bool prime[NMAX];
ll p[NMAX];

void solve(int test)
{
    printf("Case #%d: ", test);
    cerr << test << endl;

    ll n;  cin >> n;
//    n = 1000000000000;

    if (n == 1) 
    {
        cout << 0 << endl;
        return;        
    }

    int ans = 1;
    for (int i = 0; p[i] * p[i] <= n; i++)
    {
        ll m = n;
        int cnt = 0;
        while (m / p[i] > 0)
        {
            cnt++;
            m /= p[i];
        }        

        ans += cnt - 1;
    }

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    forn(i, NMAX) prime[i] = true;
    prime[0] = prime[1] = false;

    for (int i = 2; i < NMAX; i++)
    {
        if (!prime[i]) continue;
        p[cp++] = i;
//        if (i < 100) cerr << i << endl;
        for (int j = i + i; j < NMAX; j += i)
        {
            prime[j] = false;
        }    
    }


    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}