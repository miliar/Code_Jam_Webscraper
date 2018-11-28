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

map <string, bool> h;
string b[200];

int main()
{
    int t;
    scanf("%d", &t);
    FOR(ii, 1, t + 1)
    {
        int n, m;
        h.cl;
        scanf("%d%d\n", &n, &m);
        h["/"] = 1;
        string s;
        REP(i, n)
        {
            getline(cin, s);
            string t = "/";
            FOR(j, 1, sz(s))
            {
                if (s[j] == '/')
                    h[t] = 1;
                t += s[j];
            }
            h[s] = 1;
        }
        int rt = 0;
        REP(i, m)
        {
            getline(cin, s);
            s = s + "/";
            string t = "/";
            FOR(j, 1, sz(s))
            {
                if (s[j] == '/')
                {
                    if (!h[t])
                    {
                        rt++;
                        h[t] = 1;
                    }
                }
                t += s[j];
            }
        }
        printf("Case #%d: %d\n", ii, rt);
    }
}
