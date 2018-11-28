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



int res[100][1<<11]; // 1..m, last_binary
bool ok[100][100];

bool good(int i, int x, int y, int n) {
    REP(j,n) if(!ok[i-1][j] && (y&(1<<j))!=0) return 0;
    REP(j,n-1) if((y&(1<<j)) != 0 && (y&(1<<(j+1)))!=0) return 0;
    FOR(j,1,n-1) if((x&(1<<j)) != 0 && (y&(1<<(j-1)))!=0 ) 
        return 0;
    FOR(j,0,n-2) if((x&(1<<j)) != 0 && (y&(1<<(j+1))) != 0)
        return 0;
    return 1;
}

int main()
{
    int TT;
    int m,n;
    char str[100];
    
    scanf("%d",&TT);
    FOR(cs,1,TT) {
        
        scanf("%d%d",&m,&n);
        REP(i,m) {
            scanf("%s",str);
            REP(j,n) ok[i][j] = (str[j]=='.');
        }
        REP(i,m+1) REP(j,1<<n) res[i][j] = 0;
        FOR(i,1,m) {
            REP(j,1<<n) {
                REP(k,1<<n) {
                    if(good(i,j,k,n))
                        res[i][k] >?= res[i-1][j] + __builtin_popcount(k);
                }
            }
        }
        int best = 0;
        REP(j,1<<n) best >?= res[m][j];
        printf("Case #%d: %d\n", cs, best);
    }
    
    
}
