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

const int ALP = 26 + 3;

int z[ALP][ALP];
int op[ALP];
int used[ALP];

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;
    
    cin >> testCnt;
    
    forn(t, testCnt)
    {
        memset(z, -1, sizeof(z));
        memset(op, -1, sizeof(op));
        memset(used, 0, sizeof(used));
        
        int n;
        
        cin >> n;
        
        forn(i, n)
        {
            string s;
            
            cin >> s;
            
            z[ s[0] - 'A' ][ s[1] - 'A' ] = z[ s[1] - 'A' ][ s[0] - 'A' ] = s[2] - 'A';
        }
        
        int k;
        
        cin >> k;
        
        forn(i, k)
        {
            string s;
            
            cin >> s;
            
            op[ s[0] - 'A' ] = s[1] - 'A';
            op[ s[1] - 'A' ] = s[0] - 'A';
        }
        
        int len;
        
        cin >> len;
        
        string s;
        
        cin >> s;
        
        vector<int> st;
        
        forn(i, len)
        {
            if (st.empty())
            {
                st.pb(s[i] - 'A');
                used[ s[i] - 'A' ]++;
                continue;
            }
            
            int last = st[sz(st) - 1];
            
            if (z[last][s[i] - 'A'] != -1)
            {
                used[last]--;
                
                st.pop_back();
                
                used[ z[last][s[i] - 'A'] ]++;
                
                st.pb( z[last][s[i] - 'A'] );
                
                continue;
            }
            
            if (used[ op[ s[i] - 'A'] ] > 0)
            {
                st.clear();
                memset(used, 0, sizeof(used));
            }
            else
            {
                st.pb(s[i] - 'A');
                used[ s[i] - 'A' ]++;
            }
        }
        
        cout << "Case #" << t + 1 << ": ";
        
        cout << "[";
        
        forn(i, sz(st))
        {
            cout << char(st[i] + int('A'));
            
            if (i + 1 < sz(st))
                cout << ", ";
        }
        
        cout << "]" << endl;
    }
    
    return 0;
}
