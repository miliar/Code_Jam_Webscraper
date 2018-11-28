#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define ft first
#define sc second

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long double ld;
typedef pair<ld, ld> ptd;
typedef pair <int, int> pt;
typedef long long li;
typedef unsigned char byte;

const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int N = 100 + 13;

vector <pt> v;
vector <int> a, b;

inline int sign (int a)
{
    return a > 0 ? 1 : a < 0 ? -1 : 0;
}

int solve ()
{
    int res = 0;
    a.clear();
    b.clear();
    
    forn(i, sz(v))
        if (v[i].ft == 0)
            a.pb(v[i].sc);
        else
            b.pb(v[i].sc);
            
    int idx = 0;
    int apos = 0, bpos = 0;
    int aidx = 0, bidx = 0;
    a.pb(INF);
    b.pb(INF);

    while (idx < sz(v))
    {
        if (v[idx].ft == 0)
        {
            int cnt = abs(apos - v[idx].sc);
            res += (cnt + 1);
            
            apos = v[idx].sc;
            bpos += sign(b[bidx] - bpos) * min(cnt + 1, abs(b[bidx] - bpos));
            
            aidx++;
            
        } else
        {
            int cnt = abs(bpos - v[idx].sc);
            res += (cnt + 1);
            
            bpos = v[idx].sc;
            apos += sign(a[aidx] - apos) * min(cnt + 1, abs(a[aidx] - apos));
            
            bidx++;
        }
        
        idx++;
    }
    
    return res;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        v.clear();
    
        int cnt;
        scanf("%d ", &cnt);
        
        forn(i, cnt)
        {
            char c;
            int pos;
            
            if (i < cnt - 1)
                scanf("%c %d ", &c, &pos);
            else
                scanf("%c %d\n", &c, &pos);
                
            pos--;
            
            if (c == 'O')
                v.pb(mp(0, pos));
            else
                v.pb(mp(1, pos));
        }
        
        printf("Case #%d: %d\n", test + 1, solve());
    }

    return 0;
}
























































