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
int n,m;
int a[555][555];
int row[555][555] , col[555][555] , d ;

int r(int whichRow,int from,int to){
    return row[whichRow][to]-row[whichRow][from-1];
}
int c(int whichCol,int from,int to){
    return col[to][whichCol]-col[from-1][whichCol];
}

bool pos(int k,int i,int j){
    if( i + k - 1 > n ) 
        return false ;
    if( j + k - 1 > m ) 
        return false ;
    if( k % 2 == 0 ){
        int x , y ;
        x = y = 0 ;
        int add = - k  + 1;
        for(int ii = 0 ; ii < k ; ii ++){
            x += r(i+ii,j + ((ii == 0 || ii == k -1 ) ? 1 : 0) , j + k - 1 + ((ii == 0 || ii == k -1 ) ? -1 : 0) ) * ( 2 * ii + add) ;
        }
        for(int jj = 0 ; jj < k ; jj ++ ){
            y += c(j+jj,i + ((jj == 0 || jj == k -1 ) ? 1 : 0) , i + k - 1 + ((jj == 0 || jj == k -1 ) ? -1 : 0) ) * ( 2 * jj + add) ;
        }
        if( x == 0 && y == 0 ) 
            return true ;
    }else{
        int x , y ;
        x = y = 0 ;
        int add = - k / 2 ; 
        for(int ii = 0 ; ii < k ; ii ++){
            x += r(i+ii,j + ((ii == 0 || ii == k -1 ) ? 1 : 0) , j + k - 1 + ((ii == 0 || ii == k -1 ) ? -1 : 0) ) * ( ii + add) ;
        }
        for(int jj = 0 ; jj < k ; jj ++ ){
            y += c(j+jj,i + ((jj == 0 || jj == k -1 ) ? 1 : 0) , i + k - 1 + ((jj == 0 || jj == k -1 ) ? -1 : 0) ) * ( jj + add) ;
        }
        if( x == 0 && y == 0 ) 
            return true ;
    }
    return false ;
}

void solve(){
    cin >> n >> m >> d ;
    memset(row,0,sizeof(row));
    memset(col,0,sizeof(col));
    FOR(i,1,n){
        string s;
        cin >> s ;
        REP(j,m){
            a[i][j+1]=s[j]-'0';
        }
    }
    FOR(i,1,n) FOR(j,1,m){
        row[i][j]=a[i][j];
        col[i][j]=a[i][j];
    }
    FOR(i,1,n) FOR(j,1,m){
        row[i][j] += row[i][j-1];
        col[i][j] += col[i-1][j];
    }
    
    int ans = 2 ;
    FOR(k,1,n){
        FOR(i,1,n){
            FOR(j,1,m){
                if(pos(k,i,j)){
                    ans = k;
                }
            }
        }
    }
    if( ans >= 3){
        cout << ans << endl;
    }else{
        cout << "IMPOSSIBLE" << endl; 
    }
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