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
struct walkway{
    double  index;
    double  dist , speed ;
};
double  walk,run, dist;
double time_left ;
int n ;
double b[1005];
double e[1005];
double s[1005];
bool operator < (const walkway &p, const walkway &q){
    if( (q.speed + walk)*(q.speed+run) < (p.speed+walk)*(p.speed+run) ) 
        return true ;
    return false; 
}
void solve(){
    cin >> dist >> walk >> run >> time_left >> n ;
    vector<walkway> v;
    LL total = 0LL;
    REP(i,n){
        cin >> b[i] >> e[i] >> s[i] ;
        walkway temp;
        temp.index = i ;
        temp.dist = e[i] - b[i] ; 
        total += temp.dist;
        temp.speed = s[i] ;
        v.push_back(temp);
    }
    walkway temp;
    temp.index = n ;
    temp.dist = dist - total ;
    temp.speed = 0 ;
    v.push_back(temp);
    sort(ALL(v));
    reverse(ALL(v));
//     cout << dist - total << endl ;
    double ans = 0.0 ;
//     cout << time_left << endl ;
    REP(i,SIZE(v)){
//         printf( "\n%lld %lld %f",v[i].dist , v[i].speed , time_left) ; 
        if( fabs( time_left ) < EPS ){
            ans += v[i].dist / ( v[i].speed + walk ) ;
//             cout << " 1  "<< ans ;
        }else{
            if(v[i].dist >= time_left * ( v[i].speed + run ) ) {
                v[i].dist -= time_left * ( v[i].speed + run );
                ans += time_left ;
//                 cout << endl << v[i].dist << " " << ans << endl ;
                ans += (double)(v[i].dist / ( v[i].speed + walk )) ;
                time_left = 0 ;
//                 cout << " 2  "<< ans ;
            }else{
                ans += (double)(v[i].dist /  ( v[i].speed + run ));
                time_left -= (double)(v[i].dist /  ( v[i].speed + run ));
//                 cout << " 3  "<< ans ;
            }
        }
    }
//     cout << endl ;
    printf("%.9f\n",ans);
}

int main(){
	int Tests;
	cin >> Tests ; 
	for(int tests=1;tests<=Tests;tests++){
        printf("Case #%d: ",tests);
        solve();
    }
	return 0;
}
// That's all folks!