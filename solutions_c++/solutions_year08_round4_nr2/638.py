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

vector<PI> d;
int n, m,a,A; 
int res = 1000000000;

double area(int x1, int y1,int x2, int y2,int x3,int y3) {
    return abs(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/2.0;
}
        
int main()
{
    int T;
    scanf("%d",&T);
    FOR(cs,1,T) {
        
        scanf("%d%d%d",&n,&m,&A);
        
        bool ok = 0;
        FOR(x1,0,n){
            FOR(y2,0,m) {
                FOR(x3,x1,n) {
                    FOR(y3,0,m) {
                        if(area(x1,0,0,y2,x3,y3) == A/2.0) {
                            printf("Case #%d: %d %d %d %d %d %d\n",cs,x1,0,0,y2,x3,y3);
                            ok = 1;
                            break;
                        }
                    }
                    if(ok)break;
                }
                if(ok)break;
            }
            if(ok) break;
        }
        if(!ok) {
            printf("Case #%d: IMPOSSIBLE\n", cs);
        }

    }
}
