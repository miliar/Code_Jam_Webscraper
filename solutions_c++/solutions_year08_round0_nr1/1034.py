#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define CLEAR(t) memset((t), 0, sizeof(t))

#define sz size()
#define pb push_back
#define pf push_front

#define VI vector<int>
#define VS vector<string>
#define LL long long

#define INF (1<<30)

int memo[105][1005];
VS engine;
VS searchx;

int solve( int sindex, int len ) {
    if( len == searchx.sz ) return 0;
    int& best = memo[sindex][len];
    
    if( best != -1 ) return best;
    best = INF;
    
    if( engine[sindex] == searchx[len] ) return best;
    best <?= solve( sindex, len+1); //keeping same index
    REP(i,engine.sz) {
        if( i == sindex ) continue;
        best <?= 1 + solve( i, len+1 );
    } 
    
    return best;
    
}

int main() {
    int tcase;
    int n;
    char buffer[1000];
    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    
    cin >> tcase;
    
    REP(xxx,tcase) {
        
        // getting the search engines
        cin >> n;
        engine.resize( n );
        gets( buffer ); //newline
        REP(i,n) {
            gets( buffer );
            engine[i] = buffer;        
        }
        
        // getting the searchs
        cin >> n;
        searchx.resize(n);
        gets( buffer ); // newline
        
        REP(i,n) {
            gets( buffer );
            searchx[i] = buffer;
        }
        
        memset( memo, -1, sizeof( memo) );
        int ans = INF;
        REP(i,engine.sz) ans <?= solve( i, 0 );        
        printf("Case #%d: %d\n",xxx+1,ans);
    }
    
    //system("pause");
    return 0;
}
