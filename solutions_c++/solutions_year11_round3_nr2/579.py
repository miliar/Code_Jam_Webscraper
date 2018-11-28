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
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
#define SUBMIT false                                    //NOTE: Set this to true before submitting
#define   debug(x)              if(!SUBMIT){ cout<<"-> "<<#x<<" = "<<x<<"\n";}
#define   debugv(x)             if(!SUBMIT){ cout<<"-> "<<#x<<" =\n";REP(i,SIZE(x))cout<<x[i]<<" ";cout<<"\n";}
#define   debugvv(x)            if(!SUBMIT){ cout<<"-> "<<#x<<" =\n";REP(i,SIZE(x)){REP(j,SIZE(x[i])){cout<<x[i][j]<<" ";}cout<<"\n";}}
#define   debug1(A,N)           if(!SUBMIT){ cout<<"-> "<<#A<<" =\n";REP(i,N)cout<<A[i]<<" ";cout<<"\n";}
#define   debug2(A,R,C)         if(!SUBMIT){ cout<<"-> "<<#A<<" =\n";REP(i,R){REP(j,C){cout<<A[i][j]<<" ";}cout<<"\n";}}
//Main code starts here
int main(){
	LL Tests;
	cin >> Tests ; 
	for(LL tests=1;tests<=Tests;tests++){
        printf("Case #%lld: ",tests);
        LL L,t,N,C;
        cin >> L >> t >> N >> C ;
        vector<LL> v;
        v.resize(N+1);
        v[0]=0;
        REP(i,C){
            cin >> v[i+1];
        }
        for(LL i=C+1;i<=N;i++){
            v[i]=v[i-C];
        }
//         REP(i,SIZE(v)){
//             cout << v[i] << " ";
//         }
//         cout << endl ;
        vector<LL> times;
        times.resize(N+1);
        times[0]=0;
        for(LL i=1;i<=N;i++){
            times[i]+=times[i-1]+2*v[i];
        }
//         REP(i,SIZE(v)){
//             cout << times[i] << " ";
//         }
//         cout << endl ;
        if(L==0){
            cout << times[N] << endl ;
        }else if(L == 1){
            LL ans = 0;
            REP(i,N){
                if(times[i+1]>=t){
                    ans = max( ans , times[i+1]-max(times[i],t));
                }
            }
            assert( ans % 2 == 0 ) ;
            cout << times[N] - ans/2 << endl ;
        }else if(L == 2){
            LL ans = 0 ;
            REP(i,N){
                REP(j,i){
                    LL temp = 0 ;
                    if(times[i+1]>=t){
                        temp += times[i+1]-max(times[i],t);
                    }
                    if(times[j+1]>=t){
                        temp += times[j+1]-max(times[j],t);
                    }
                    ans=max(ans,temp);
                }
            }
            assert( ans % 2 == 0 ) ;
            cout << times[N] - ans/2 << endl ;
        }
    }
	return 0;
}
// That's all folks!