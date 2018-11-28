#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int p[701];
int sol[701][701];
int s[701];

bool w[701][701];
int cc[701][701];

int c(int n, int k)
{
    if (n == k)
        return 1;
    if (k == 0)
        return 1;
    if (k == 1)
        return n;
    if  (w[n][k])
        return cc[n][k];
    cc[n][k] = (c(n - 1, k) + c(n - 1, k - 1)) % 100003;
    w[n][k] = 1;
    return cc[n][k];
}

int main()
{
    p[0] = 1;
    FOR(i, 1, 501)
        p[i] = p[i - 1] * 2 % 100003;
    sol[2][1] = 1;
    s[2] = 1;
    FOR(i, 3, 501)
    {
        sol[i][1] = 1;
        s[i] = 1;
        FOR(l, 2, i)
        {
            sol[i][l] = 0;
            FOR(j, 1, l)
                if (i - l >= l - j)
                    sol[i][l] = ((ll)sol[i][l] + (ll)sol[l][j] * (ll)c(i - l - 1, l - j - 1)) % 100003ll;
            //cout << sol[i][l] << " ";
            s[i] = (s[i] + sol[i][l]) % 100003;
        }
        s[i] %= 100003;
        //cout << endl;
    }
    int t;
    scanf("%d", &t);
    REP(i, t)
    {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", i + 1, s[n]);
    }
    return 0;
}
