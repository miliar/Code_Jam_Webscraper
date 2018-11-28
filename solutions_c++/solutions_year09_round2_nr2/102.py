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

int cnt[10];

string fill_str(string s, int l)
{
    int cur[10];
    forn(i, 10) cur[i] = 0;

    forn(i, l)
    {
        cur[s[i] - '0']++;
    }   

    for1(i, 9) if (cur[i] > cnt[i]) return "figvam";

    s = s.substr(0, l);

    forn(i, 10)
    {
        forn(j, cnt[i] - cur[i])
        {
            s += char(i + '0');
        }
    }

    return s;
}

void solve(int tc)
{
    printf("Case #%d: ", tc);

    string s;
    cin >> s;

    memset(cnt, 0, sizeof(cnt));

    forv(i, s)
    {
        cnt[s[i] - '0']++;
    }

    for (int i = s.size() - 1; i >= 0; i--)
    {
        for (char c = s[i] + 1; c <= '9'; c++)
        {
            if (cnt[c - '0'] == 0) continue;
            char t = s[i];
            s[i] = c;
            if (fill_str(s, i + 1) != "figvam")
            {
                cout << fill_str(s, i + 1) << endl;
                return;    
            }
            s[i] = t;
        }
    }

    string ans = "";

    int f = 1;
    while (cnt[f] == 0) ++f;

    ans += char(f + '0');

    cnt[f]--;
    cnt[0]++;

    forn(c, 10)
    {
        forn(it, cnt[c]) ans += char(c + '0');
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
            
