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

//     int mn[50100][30]; // min ending at letter x.
    char S[50100];
    char W[50100];
    
int main()
{
    int T;

    scanf("%d",&T);
    

    int k;
    FOR(cs,1,T) {

        scanf("%d",&k);
        scanf("%s",&S);
        
                
        vi d;
        REP(i,k) d.pb(i);
        int n = strlen(S);
        int res = 1000000;
        do {
            for(int s = 0; s < n; s += k) {
                FOR(j,0,k-1) {
                    W[s + j] = S[s + d[j]];
                }
            }
            char last = 0;
            int wyn = 0;
            REP(i,n) {
                if(W[i] != last) ++wyn;
                last = W[i];
            }
            res <?= wyn;
        } while(next_permutation(ALL(d)));
        
        
/*
        FOR(i,1,n/k) FOR(j,0,25) mn[i][j] = 1000000;
        set<char> M;
        M.clear();
        FOR(j,1,k) M.insert(S[j-1]);
        FOR(j,0,25) {
            mn[1][j] = M.size();
            if(M.find('a'+j) == M.end()) ++mn[1][j];
        }
        FOR(b,2,n/k) {
            M.clear();
            FOR(j,(b-1)*k+1,b*k) M.insert(S[j-1]);
            FOR(last,0,25) {
                FOR(next,0,25) {
                    int s = mn[b-1][last] + SIZE(M);
                    if(M.find('a'+last) != M.end()) --s;
                    if(M.find('a'+next) == M.end()) ++s;
                    if(next==last && M.find('a'+next) != M.end() && SIZE(M) != 1)
                        ++s;
                    mn[b][next] <?= s;
                    if(next <3)
                    printf("mn[%d][%c] = %d\n", b, 'a'+next,mn[b][next] );
                }
            }
        }
        int res = 1000000;
        FOR(j,0,25) res <?= mn[n/k][j];*/
        printf("Case #%d: %d\n", cs, res);
    }
}
