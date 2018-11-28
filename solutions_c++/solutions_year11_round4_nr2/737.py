#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define fs first
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pti;
typedef pair<ld, ld> pt;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 10 + 3;

ld a[N][N];

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCnt;
    
    cin >> testCnt;
    
    forn(t, testCnt)
    {
        int n, m;
        ld d;
        
        cin >> n >> m >> d;
        
        forn(i, n)
            forn(j, m)
            {
                char c;
                
                cin >> c;
                
                a[i][j] = d + ld(c - '0');
            }
            
        int ans = 0;
        
        forn(i1, n)
            forn(j1, m)
                fore(k, 3, 20)
                {
                    int i2 = i1 + k - 1;
                    int j2 = j1 + k - 1;
                    
                    if (i2 >= n || j2 >= m)
                        continue;
                        
                    pt need = mp(ld(i2 + i1 + 1) / ld(2.0), ld(j2 + j1 + 1) / ld(2.0));
                    
                    pt cur;
                    ld curm = 0.0;
                    
                    fore(x, i1, i2)
                        fore(y, j1, j2)
                        {
                            if (x == i1 && y == j1)
                                continue;
                            if (x == i2 && y == j1)
                                continue;
                            if (x == i1 && y == j2)
                                continue;
                            if (x == i2 && y == j2)
                                continue;
                                
                            if (abs(curm) < EPS)
                            {
                                curm = a[x][y];
                                cur = mp(ld(x) + 0.5, ld(y) + 0.5);
                                continue;
                            }
                            
                            ld l = curm / a[x][y];
							l = ld(1.0) / l;
                            pt next = mp( (cur.ft + l * (ld(x) + 0.5)) / ld(1.0 + l), (cur.sc + l * (ld(y) + 0.5)) / ld(1.0 + l) ); 
                            
                            cur = next;
                            curm += a[x][y];
                        }
                        
                    if (abs(cur.ft - need.ft) < EPS && abs(cur.sc - need.sc) < EPS)
                        ans = max(ans, k);
                }
        
        if (ans < 3)
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        else
            printf("Case #%d: %d\n", t + 1, ans);
    }

    return 0;
}
