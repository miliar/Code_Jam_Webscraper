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

int gr[10000];
ll cst[10000];
int ile[10000];

int main(){
    int t;
    scanf("%d", &t);
    REP(i,t){
        int r,k,n;
        scanf("%d%d%d", &r, &k, &n);
        REP(j,n){
            scanf("%d", &gr[j]);
            cst[j] = -1LL;
        }
        ll C = 0LL;
        cst[0] = 0LL;
        ile[0] = 0;
        int p = 0;
        int Z = 0;
        bool jeszcze = true;
        while(r){
            ll ss = 0LL;
            int licz = 0;
            while(ss + gr[p] <= k && licz < n){
                ++licz;
                ss += gr[p];
                p = (p + 1) % n;
            }
            C += ss;
//            printf("%d %d %lld\n", p, r, C);
            --r;
            ++Z;
            if(jeszcze){
                if(cst[p] == -1LL){
                    cst[p] = C;
                    ile[p] = Z;
                }
                else{
                    C += (C - cst[p]) * (r / (Z - ile[p]));
                    r %= (Z - ile[p]);
                    jeszcze = false;
                }
            }
        }
        printf("Case #%d: %lld\n", i+1, C);
    }
    return 0;
}

