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

int dia[60][60];

void run(int cnum){
    int n;
    scanf("%d", &n);
    FUP(i,0,n-1)
       FUP(j,0,i)
            scanf("%d", &dia[i-j][j]);
    FUP(i,1,n-1)
        FDN(j,n-1,i)
            scanf("%d", &dia[j][i+n-1-j]);


/*    printf("  %d\n",n);
    REP(i,n){
        REP(j,n)
            printf("%d ", dia[i][j]);
        printf("\n");
    }*/

    FUP(i,n,4*n){
        FUP(a,0,i-n) FUP(b,0,i-n){
            bool c = true;
            REP(j,n){
                REP(k,n){
                    int A = k+b-a;
                    int B = j+a-b;
                    if(A >= 0 && A < n && B >= 0 && B < n && dia[j][k] != dia[A][B]){
                        c = false;
                        break;
                    }
                }
                if(!c) break;
            }
            if(!c) continue;
            REP(j,n){
                REP(k,n){
                    int A = i-1-k-b-a;
                    int B = i-1-j-a-b;
                    if(A >= 0 && A < n && B >= 0 && B < n && dia[j][k] != dia[A][B]){
                        c = false;
                        break;
                    }
                }
                if(!c) break;
            }
            if(c){
                printf("Case #%d: %d\n", cnum, i*i - n*n);
                return;
            }
        }
    }
}

int main(){
    int C;
    scanf("%d", &C);
    REP(i,C) run(i+1);
    return 0;
}


