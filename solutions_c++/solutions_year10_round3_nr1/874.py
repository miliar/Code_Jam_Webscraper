#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <queue>
#include<cstring>
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int,int> pii;
typedef long long int64;
typedef unsigned long long uint64;
//template<typename T> int size(const T& c) { return int(c.size()); }
//template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n) - 1); i >= 0; --i)

int main() {
    //char finname[] = "A_test.in";
    //char finname[] = "A-small-attempt0.in";
    //char finname[] = "A-small-attempt1.in";
    //char finname[] = "A-small-attempt2.in";
    char finname[] = "A-large.in";
    FILE *fp;
    if((fp=fopen(finname,"r")) == NULL) {
        printf("File not found\n");
        exit(0);
    }
    fclose(fp);
    freopen(finname,"r",stdin);
    freopen(strcat(finname,".outFile"),"w",stdout);
    int tc,n,r,k,ans;
    scanf("%d",&tc);
    int ha[1000],hb[1000];
    for(int tci=0;tci<tc;tci++) {
        scanf("%d",&n);
        ans=0;
        REP(i,n)
            scanf("%d%d",&ha[i],&hb[i]);
        REP(i,n) {
            for(int j=i+1;j<n;j++) {
                if(ha[i]<ha[j]) {
                    if(hb[i]>hb[j])
                        ans++;
                }
                else if(hb[i]<hb[j])
                    ans++;
            }
        }
        //if(canreach<k)
    //printf("Case #%d: IMPOSSSIBLE\n",tci+1);
        //else
        printf("Case #%d: %d\n",tci+1,ans);
    }
    return 0;
}



