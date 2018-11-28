#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <bitset>
#include <list>
#include <algorithm>
#include <cassert>


using namespace std;

#define rep(i, a, b) for(typeof(a) i=(a); i<(typeof(a))(b); ++i)
#define trav(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

inline bool solve(int tc){
    int n, l, h;
    scanf("%d%d%d", &n, &l, &h);
    vi f(n);
    rep(i, 0, n){
        scanf("%d", &f[i]);
    }
    printf("Case #%d: ", tc);
    rep(i, l, h+1){
        bool bad = false;
        rep(j, 0, n){
            int a = f[j];
            int b = i;
            if (a % b != 0 && b % a != 0){
                bad = true;
                break;
            }
        }
        if(!bad){
            printf("%d\n", i);
            return true;
        }
    }
    printf("NO\n");
    return true;
}

int main (int argc, char const *argv[]) {
    int n; scanf("%d",&n);
    for(int k=1;solve(k)&&k<n;k++);
    return 0;
}