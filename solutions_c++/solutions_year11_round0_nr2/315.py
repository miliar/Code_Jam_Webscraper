#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define X first
#define Y second

using namespace std;

typedef unsigned int uint;
typedef unsigned char byte;
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

int to[256][256], is[256][256];

inline void solve(int test)
{
    memset(to, -1, sizeof(to));
    memset(is, false, sizeof(is));
    
    int n;
    cin >> n;
    
    forn(i, n)
    {
        string s;
        cin >> s;
        
        to[s[0]][s[1]] = to[s[1]][s[0]] = s[2];
    }
    
    cin >> n;
    
    forn(i, n)
    {
        string s;
        cin >> s;
        
        is[s[0]][s[1]] = is[s[1]][s[0]] = true;
    }
    
    cin >> n;
    
    int cnt[26];
    memset(cnt, 0, sizeof(cnt));
    
    vector<char> z;
    
    forn(i, n)
    {
        char c;
        cin >> c;
        
        z.pb(c);
        cnt[c - 'A']++;
        
        if (sz(z) > 1 && to[z[sz(z) - 2]][z[sz(z) - 1]] != -1)
        {
            char a = z[sz(z) - 2], b = z[sz(z) - 1];
            
            cnt[a - 'A']--;
            cnt[b - 'A']--;
        
            z.pop_back();
            z.back() = to[a][b];
        }
        else
        {
            forn(i, 26)
                if (is[i + 'A'][c] && cnt[i] > 0)
                {
                    z.clear();
                    memset(cnt, 0, sizeof(cnt));
                    break;
                }
        }
    }
    
    printf("Case #%d: [", test + 1);
    
    forn(i, sz(z))
    {
        printf("%c", z[i]);
        
        if (i + 1 < sz(z))
            printf(", ");
    }
    
    printf("]\n");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
        solve(test);
    
    return 0;
}
