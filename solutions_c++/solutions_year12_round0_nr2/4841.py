
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

//TopCoder defines
#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define dbg(e) cout<<(#e)<<" : "<<e<<endl
#define REP(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define pb  push_back
#define mp make_pair

//Extras
#define SI(x) scanf("%d", &x)
#define SLL(x) scanf("%lld", &x)
#define SD(x) scanf("%lf", &x)

typedef long long LL;

#define gt(x) ((x)>=0)

void main2() {
    int n, surprise, L, tmp;
    vector <int> V;
    scanf("%d%d%d", &n, &surprise, &L);
    REP(i,n) scanf("%d", &tmp), V.pb(tmp);
    sort(V.rbegin(), V.rend());
    int ans = 0;
    REP(i,n) {
        if(V[i] - L >= 2 * L - 2 && gt(V[i] - L)) ans++;
        else {
            if(surprise == 0) break;
            if(V[i] - L <= 2 * L - 3 && V[i] - L >= 2 * L - 4 && gt(V[i]-L)) ans++, surprise--;
        }
    }
    printf("%d\n", ans);
}

int main() {
    int test; SI(test); REP(tt,test) {
        printf("Case #%d: ", tt+1);
        main2();
    }
}

