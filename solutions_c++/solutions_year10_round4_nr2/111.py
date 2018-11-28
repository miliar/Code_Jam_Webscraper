#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <utility>

using namespace std;
//using namespace __gnu_cxx;

typedef long long ll;
typedef double db;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef istringstream is;
typedef ostringstream os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);--(i))
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();++(i))
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define PRINT(v) for(int (i)=0;(i)<(int)(v).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

// druzyna, poziom, ile mniej
long long dp[2000][50][50];

// druzyna, poziom
int tab[2000][50];

// musi byc na
int ile[2000];

void run(int cnum){
    int n;
    scanf("%d", &n);
    int c = (1 << n);
    int p = 1;
    REP(i,c){ scanf("%d", &ile[i]); ile[i] = n - ile[i]; }
    c >>= 1;
    while(c){
        REP(i,c)
            scanf("%d", &tab[i][p]);
        c >>= 1;
        p++;
    }
//    printf("%d %d\n", p , n);

    REP(j,(1<<n)) REP(i,p+1){
        if(i >= ile[j]) dp[j][0][i] = 0;
        else dp[j][0][i] = INF;
    }
    FUP(i,1,p-1){
        REP(j,1<<(n-i)){
            FUP(k,0,p-1){
                dp[j][i][k] = min(tab[j][i] + dp[j+j][i-1][k+1] + dp[j+j+1][i-1][k+1], dp[j+j][i-1][k] + dp[j+j+1][i-1][k]);
            }
            dp[j][i][p] = dp[j+j][i-1][p] + dp[j+j+1][i-1][p];
        }
    }
    printf("Case #%d: %lld\n", cnum, dp[0][p-1][0]);
}

int main(){
    int C;
    scanf("%d", &C);
    REP(i,C) run(i+1);
    return 0;
}


