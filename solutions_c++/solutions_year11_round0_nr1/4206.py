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
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 13;

int d[N][N][N];
int n;
pt a[N];

int bfs(int si, int s1, int s2)
{
    memset(d, 63, sizeof(d));
    
    d[si][s1][s2] = 0;
    
    queue<pair<int, pt> > q;
    
    q.push(mp(si, mp(s1, s2)));
    
    while(!q.empty())
    {
        int idx = q.front().ft;
        pt cur = q.front().sc;
        q.pop();
        
        if (idx == n)
            continue;
        
        int x1 = cur.ft;
        int x2 = cur.sc;
        
        for(int dx1 = -1; dx1 <= 1; dx1++)
            for(int dx2 = -1; dx2 <= 1; dx2++)
            {            
               int n1 = x1 + dx1;
               int n2 = x2 + dx2;
               int nidx = idx;
               
               if (0 <= n1 && n1 < N && 0 <= n2 && n2 < N && d[nidx][n1][n2] > d[idx][x1][x2] + 1)
               {
                   d[nidx][n1][n2] = d[idx][x1][x2] + 1;
                   q.push(mp(nidx, mp(n1, n2)));
               }
           }
       
        for(int dx1 = -1; dx1 <= 1; dx1++)
            for(int dx2 = -1; dx2 <= 1; dx2++)
            {            
               int n1 = x1 + dx1;
               int n2 = x2 + dx2;
               
               if (!(dx1 == 0 && a[idx] == mp(0, n1)) && !(dx2 == 0 && a[idx] == mp(1, n2)))
                   continue;
                   
               int nidx = idx + 1;
               
               if (0 <= n1 && n1 < N && 0 <= n2 && n2 < N && d[nidx][n1][n2] > d[idx][x1][x2] + 1)
               {
                   d[nidx][n1][n2] = d[idx][x1][x2] + 1;
                   q.push(mp(nidx, mp(n1, n2)));
               }
           }
    }
    
    int ans = INF;
    
    forn(s1, N)
        forn(s2, N)
            ans = min(ans, d[n][s1][s2]);
            
    assert(ans < INF / 2);
            
    return ans;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;
    
    cin >> testCnt;
    
    forn(t, testCnt)
    {
        cin >> n;
        
        forn(i, n)
        {
            char c;
            int x;
            
            cin >> c >> x;
            
            x--;
            
            int h = c == 'B'? 0: 1;
            
            a[i] = mp(h, x);
        }
        
        int ans = bfs(0, 0, 0);
        
        printf("Case #%d: %d\n", t + 1, ans);
    }
    
    return 0;
}
