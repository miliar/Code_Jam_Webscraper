#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
template <typename T> inline bool checkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template <typename T> inline bool checkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long lint;

int a, b, len, tmp;

int getLen(int a){
    if(a == 0) return 1;
    int ans = 0;
    tmp = 1;
    while(a){
        a /= 10;
        tmp *= 10;
        ans++;
    }
    tmp /= 10;
    return ans;
}

int gao(int n){
    int pre = n % 10;
    return n  = n / 10 + pre * tmp;
}

int solve(){
    int ans = 0;
    len = getLen(a);
    if(len == 1) return 0;
    for(int i = a; i <= b; i++){
        int m = i;
        for(int j = 1; j < len; j++){
            m = gao(m);
            if(m == i) break;
            if(m > i  && a <= m && m <= b) ans++;
        }
    }
    return ans;
}

int main(){
    freopen("q3.out", "w", stdout);
    int T, t = 0;
    for (scanf("%d", &T); t < T; ++t) {
    	scanf("%d%d", &a, &b);
    	printf("Case #%d: %d\n", t + 1, solve());
    }
    return 0;
}

