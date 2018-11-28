/*{{{*/
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
/*}}}*/

// ile el. ma zbior (1..499); jaka na koncu (1..500);
int dp[1000][1000];
int nk[1000][1000];
const int MOD = 100003;

void gen(){
    nk[0][0] = 1;
    FUP(i,1,500){
        nk[i][0] = 1;
        nk[i][i] = 1;
        FUP(j,1,i-1)
            nk[i][j] = (nk[i-1][j-1]+nk[i-1][j]) % MOD;
    }

    FUP(i,1,500)
        dp[1][i] = 1;
    FUP(i,2,499){
        FUP(j,i+1,500){
            dp[i][j] = 0;
            FDN(k,i-1,1){
                if(dp[k][i] == 0) continue;
                long long tmp = dp[k][i];
                tmp *= nk[j-i-1][i-k-1];
                tmp %= MOD;
                dp[i][j] += tmp;
                dp[i][j] %= MOD;
            }
        }
    }
}

void run(int cnum){
    int n;
    cin >> n;
    int wyn = 0;
    FUP(i,1,n-1)
        wyn = (wyn + dp[i][n]) % MOD;
    cout << "Case #" << cnum << ": " <<wyn << endl;
}

int main(){
    ios::sync_with_stdio(0);
    gen();
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}


