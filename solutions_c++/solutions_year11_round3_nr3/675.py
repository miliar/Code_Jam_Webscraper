//{{{
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <utility>
#include <queue>
#include <sstream>
using namespace std;
 
typedef long long ll;
typedef pair<int,int> ii;
#define size(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define REP(i,n) FOR(i,0,(n)-1) 
//}}}

int N;
int L, H;
int F[100];
int main() {
    // freopen("inp","r",stdin);
    int tn;
    scanf("%d", &tn);

    FOR(cc,1,tn) {
        cin >> N >> L >> H;
        REP(i,N) cin >> F[i];
        int ret = -1;
        FOR(i,L,H) {
            int cnt = 0;
            REP(j,N) if( F[j] % i == 0 || ( F[j] > 0 && (i % F[j] == 0) ) ) ++cnt;
            if( cnt == N ) {
                ret = i;
                break;
            }
        }
        printf("Case #%d: ", cc);
        if( ret == -1 ) printf("NO\n");
        else printf("%d\n", ret);
    }
}


