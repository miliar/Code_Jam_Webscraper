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

#define AND 1
#define OR  0


int gate[10100],ch[10100];
int val[10100];
map<bool,int> pos[10100];

int main()
{
    int T,m,V;
    scanf("%d",&T);
    FOR(cs,1,T) {
        
        scanf("%d%d",&m,&V);
        FOR(i,1,(m-1)/2) scanf("%d%d",gate+i,ch+i);
        FOR(j,(m-1)/2+1,m) scanf("%d", val+j);
        FORD(j,(m-1)/2,1) if(gate[j] == AND) val[j] = val[2*j] & val[2*j+1];
                          else if(gate[j] == OR) val[j] = val[2*j] | val[2*j+1];
        int res = 0;
        FOR(j,1,m) {
            pos[j][0] = 1000000;
            pos[j][1] = 1000000;
        }    
        //if(V != val[1]) {
            FOR(j,(m-1)/2+1,m) pos[j][val[j]] = 0;
            FORD(j,(m-1)/2,1) {
                if(gate[j] == AND) {
                    FORE(it,pos[2*j]) FORE(it2,pos[2*j+1]) {
                        if(ch[j] == 1) {
                            pos[j][it->first | it2->first] <?= it->second + it2->second + 1;
                        }
                        pos[j][it->first & it2->first] <?= it->second + it2->second;
                    }
                } else if(gate[j] == OR) {
                    FORE(it,pos[2*j]) FORE(it2,pos[2*j+1]) {
                        if(ch[j] == 1)
                            pos[j][it->first & it2->first] <?= it->second + it2->second + 1;
                        pos[j][it->first | it2->first] <?= it->second + it2->second;
                    }
                }

            }
        //} 
        
        if(pos[1][V] == 1000000) 
            printf("Case #%d: IMPOSSIBLE\n", cs);
        else
            printf("Case #%d: %d\n", cs, pos[1][V]);
    }
}
