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
	int Tests;
    int won[105];
    int lost[105];
    double WP[105];
    double OWP[105];
    double OOWP[105];
    double ans[105];
    int n;
    vector<string> s;
	cin >> Tests ; 
	for(int tests=1;tests<=Tests;tests++){
        printf("Case #%d:\n",tests);
        cin >> n ;
        s.resize(n);
        REP(i,n){
            cin >> s[i] ;
        }
        REP(i,n){
            won[i]=lost[i]=0;
            REP(j,n){
                if(s[i][j]=='1')
                    won[i]++;
                else if(s[i][j]=='0')
                    lost[i]++;
                WP[i] = (double)(won[i])/((double)(won[i]+lost[i]));
            }
        }
        REP(i,n){
            OWP[i]=0;
            REP(j,n){
                if( i == j )
                    continue;
                if( s[i][j]=='.')
                    continue;
                if( s[i][j]=='0'){
                    OWP[i] += (double)(won[j]-1)/(won[j]+lost[j]-1);
                }else{
                    OWP[i] += (double)(won[j])/(won[j]+lost[j]-1);
                }
            }
            OWP[i]/=(won[i]+lost[i]);
        }
        REP(i,n){
            OOWP[i]=0;
            REP(j,n){
                if( i == j )
                    continue;
                if( s[i][j]=='.')
                    continue;
                OOWP[i] += OWP[j];
            }
            OOWP[i]/=(won[i]+lost[i]);
        }
        REP(i,n){
            ans[i] = 0.25 * WP[i] + 0.5 * OWP[i] + .25 * OOWP[i] ;
        }
//         REP(i,n){ 
//             printf("%.6f %.6f %.6f\n",WP[i],OWP[i],OOWP[i]);
//         }
        REP(i,n){
            printf("%.12f\n",ans[i]);
        }
    }
	return 0;
}
// That's all folks!