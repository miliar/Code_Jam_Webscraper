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

int x[1000];
int v[1000];
bool czy[1000];

void run(int cnum){
    int n,k,b,t;
    cin >> n >> k >> b >> t;
    REP(i,n) cin >> x[i];
    REP(i,n) cin >> v[i];
    REP(i,n){
        if(b-x[i] <= t * v[i]) czy[i] = true;
        else czy[i] = false;
    }
    int wyn = 0;
    int ilen = 0;
    FDN(i,n-1,0){
        if(k == 0) break;
        if(!czy[i]) ilen++;
        else{ wyn += ilen; --k; }
    }
    cout << "Case #" << cnum << ": ";
    if(k == 0) cout << wyn << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}

