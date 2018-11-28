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

int c,d;
pii tab[4000];

bool dasie(ll m){
    ll fst = -INFLL;
    REP(i,c){
        ll pocz = max(fst, tab[i].FI - m);
        ll kon = pocz + (ll)d * (tab[i].SE - 1);
        if(abs(kon-tab[i].FI) > m)
            return false;
        fst = kon + d;
    }
    return true;
}

void run(int cnum){
    cin >> c >> d;
    d *= 2;
    REP(i,c){
        cin >> tab[i].FI >> tab[i].SE;
        tab[i].FI *= 2;
    }

    ll lb = 0, ub = 10000000;
    ub *= ub;
    while(lb < ub-1){
        ll m = (lb+ub)/2 - 1;
        if(!dasie(m))
            lb = m + 1;
        else
            ub = m + 1;
    }
    cout << "Case #" << cnum << ": " << (lb/2) << "." << ((lb/2)*2 == lb ? 0 : 5) << "\n";
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}

