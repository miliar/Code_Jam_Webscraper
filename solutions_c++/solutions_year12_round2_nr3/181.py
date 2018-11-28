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
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int testCount = 0;
    scanf("%d", &testCount); char testBuf[10]; gets(testBuf);
    for1(currentTest, testCount){
        printf("Case #%d: ", currentTest);
        //solution

        int n;
        cin >> n;
        vector<int> a(n);
        forn(i, n)
            cin >> a[i];

        int ansm1 = -1, ansm2 = -1;
        map<int, int> cnt;
        fore(mask, 1, 1 << n){
            int cur = 0;
            forn(i, n)
                if(mask & (1 << i))
                    cur += a[i];
            if(cnt.count(cur)){
                ansm1 = mask, 
                ansm2 = cnt[cur];
                break;
            }
            cnt[cur] = mask;       
        }
            
        if(ansm1 == -1)
            puts("\nImpossible");
        else{
            puts("");
            forn(i, n)
                if(ansm1 & (1 << i))
                    printf("%d ", a[i]);
            puts("");
            forn(i, n)
                if((ansm2 & (1 << i)))
                    printf("%d ", a[i]);
            puts("");    
        }
//        fprintf(stderr, "Test #%d: %d\n", currentTest, (int)clock());
    }

    return 0;
}


