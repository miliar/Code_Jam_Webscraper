#pragma comment(linker, "/STACK:10000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define debug(x) {cerr << #x << " = " << x << endl;}
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    cout.precision(10); cout << fixed;

    int testCount;
    cin >> testCount;

    forn(curTest, testCount){
        printf("Case #%d: ", curTest+1);

        //Place solution here
        
        int n;
        cin >> n;
        vector<int> a(n);
        int sum = 0;
        forn(i, n){
            cin >> a[i];
            sum ^= a[i];
        }

        if(sum != 0)
            puts("NO");
        else{
            int ans = accumulate(all(a), 0) - (*min_element(all(a)));
            cout << ans << endl;
        }


    }
    
    return 0;
}



