#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <climits>
#include <limits>
using namespace std;
//Macros
#define SIZE(A) ((int)(A.size()))
#define SET(A,x) memset(A,x,sizeof(A));                 //NOTE: Works only for x = 0 and -1. Only for integers.
#define FILL(A,x) fill(A.begin(),A.end(),x)
#define REP(i,N) for(int i=0;i<(int)(N);i++)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define REV(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ALL(x)  x.begin(),x.end()
#define INF (INT_MAX/2)
#define LLINF (LONG_LONG_MAX/2LL)
#define EPS 1e-11
#define GI ({int t;scanf("%d",&t);t;})                  //NOTE: Don't comma separate two inputs.
#define GL ({long long t;scanf("%lld",&t);t;})          //NOTE: Don't comma separate two inputs.
#define GF ({double t;scanf("%lf",&t);t;})              //NOTE: Don't comma separate two inputs.
#define MP make_pair
#define PB push_back
#define gcd(a,b) __gcd(a,b)                             //NOTE: Both the arguments should be of the same type.
#define nbits(n) __builtin_popcount(n)                  //NOTE: Works only for int. Write your own function for long long :-/
#define MOD 1000000007
#define FIX(a) (((a)%MOD+MOD)%MOD)
#define SUBMIT false                                    //NOTE: Set this to true before submitting
#define   debug(x)              if(!SUBMIT){ cout<<"-> "<<#x<<" = "<<x<<"\n";}
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
//Main code starts here
int n;
pair<char,int> seq[105];
int ans[105];
int main(){
    int Tests;
    cin >> Tests ;
    for(int tests=1;tests<=Tests;tests++){
        cout<<"Case #"<<tests<<": ";
        int sub=0;
        int lastO=1;
        int lastB=1;
        cin >> n ; 
        REP(i,n){
            cin >> seq[i].first >> seq[i].second ;
        }
        REP(i,n){
            ans[i] =  abs( seq[i].second - ( seq[i].first=='O' ? lastO : lastB )  ) ;
            if( i >= 1 ){
                if( seq[i].first != seq[i-1].first ){
                    ans[i] -= min( ans[i] , sub ) ;
                }
            }
            ans[i] ++ ;
            if( i >= 1 ){
                if( seq[i].first != seq[i-1].first ){
                    sub = ans[i] ;
                }else{
                    sub += ans[i] ;
                }
            }else{
                sub = ans[i] ; 
            }
            if( seq[i].first == 'O' )
                lastO = seq[i].second ; 
            else
                lastB = seq[i].second ; 
            ans[i] += ans[i-1] ;  
        }
        cout << ans[n-1] << endl ; 
    }
    return 0;
}
// That's all folks!