#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <queue>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
typedef pair<int,int> PI;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define REP(i,n)	for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,s,k)	for(int i=(s),_k=(k);i<=_k;++i)
#define FORD(i,s,k)	for(int i=(s),_k=(k);i>=_k;--i)
#define FORE(it,q)	for(__typeof((q).begin()) it=(q).begin();it!=(q).end();++it)
#define FORED(it,q) for(__typeof((q).rbegin())it=(q).rbegin();it!=(q).rend();++it)
#define SIZE(x)     x.size()
#define ALL(v)      v.begin(),v.end()
#define SE          second
#define FI          first
#define pb          push_back





template<typename T1,typename T2,typename T3>
struct triple {
    T1 first;
    T2 second;
    T3 third;
    triple() {}
    triple(T1 f,T2 s,T3 t) : first(f),second(s),third(t) {}
};
#define TH          third
#define TI          triple<int,int,int>

const int MOD = 10007;

int res[200][200];
bool rock[200][200];

int main()
{
    int TT;
    int W,H,R;
    int x,y;
    scanf("%d",&TT);
    FOR(cs,1,TT) {
        scanf("%d%d%d",&W,&H,&R);
        REP(i,W) REP(j,H) res[i][j] = rock[i][j] = 0;
        REP(i,R) { scanf("%d%d",&x,&y); --x;--y; rock[x][y] = 1; }
        res[0][0] = 1;
        FOR(i,1,W-1) FOR(j,1,H-1) if(!rock[i][j]) {
            if(j>=2) res[i][j] = res[i-1][j-2]%MOD;
            if(i>=2) res[i][j] = (res[i][j] + res[i-2][j-1])%MOD;
        }
        
        printf("Case #%d: %d\n", cs, res[W-1][H-1]);
    }
    
    
}
