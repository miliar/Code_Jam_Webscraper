/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : 1.cpp

* Purpose : SPOJ

* Creation Date : 13-04-2013

* Last Modified : Saturday 13 April 2013 02:44:37 PM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include <iterator>
#include <cctype>
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
#include <string>
using namespace std;

//Macros
#define dbl double
#define fl float
#define ll long long
#define ull unsigned long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define vi vector<int>
#define vll vector<ll>

#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))

#define MOD 1000000007
#define MAXN 100010
#define MAXBUF 5000000
#define EPS 1e-9
#define NIL 0
#define INF (INT_MAX/2)
#define LLINF (LONG_LONG_MAX/2LL)
#define NEWLINE '\n'

#define SET(A) memset(A, 1,sizeof(A));                     //NOTE: Works only for x = 0 and -1. Only for integers.
#define CLR(A) memset(A, 0,sizeof(A));
#define MEM(A,x) memset(A,x,sizeof(A));
#define CPY(A,B) memcpy(A,B,sizeof(A));

#define SIZE(A) ((int)(A.size()))
#define ALL(x)  x.begin(),x.end()
#define FILL(A,x) fill(ALL(A),x)
#define REP(i,N) for(int i=0;i<(int)(N); ++i)
#define FORab(i,a,b) for(int i=(int)(a);i<=(int)(b); ++i)
#define RFORab(i,a,b) for(int i=(int)(a);i>=(int)(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define SORTV(x) sort(ALL(x))
#define REVV(x) reverse(ALL(x))

#define GI ({int t;scanf("%d",&t);t;})                  //NOTE: Don't comma separate two inputs.
#define GLL ({long long t;scanf("%lld",&t);t;})          //NOTE: Don't comma separate two inputs.
#define GLD ({double t;scanf("%lf",&t);t;})              //NOTE: Don't comma separate two inputs.

#define mp make_pair
#define pb push_back
#define ff first
#define ss second

#define nbits(n) __builtin_popcount(n)                  //NOTE: Works only for int. Write your own function for long long :-/
#define atbit(x,i) (((x)>>(i))&1)
#define FIXMOD(a) (((a)%MOD+MOD)%MOD)

#define   debug(x)              if(!SUBMIT){ cout<<"-> "<<#x<<" = "<<x<<"\n";}
#define   debugv(x)             if(!SUBMIT){ cout<<"-> "<<#x<<" =\n";REP(i,SIZE(x))cout<<x[i]<<" ";cout<<"\n";}
#define   debugvv(x)            if(!SUBMIT){ cout<<"-> "<<#x<<" =\n";REP(i,SIZE(x)){REP(j,SIZE(x[i])){cout<<x[i][j]<<" ";}cout<<"\n";}}
#define   debug1(A,N)           if(!SUBMIT){ cout<<"-> "<<#A<<" =\n";REP(i,N)cout<<A[i]<<" ";cout<<"\n";}
#define   debug2(A,R,C)         if(!SUBMIT){ cout<<"-> "<<#A<<" =\n";REP(i,R){REP(j,C){cout<<A[i][j]<<" ";}cout<<"\n";}}

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

//template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (a > b ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
//template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool BTW(T a, T b, T c) { return a<=b && b<=c; }         // To check whether b is in [a,c]
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }                 // set max(a,b) to a
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }                 // set min(a,b) to b

#define SUBMIT false                                    //NOTE: Set this to true before submitting

bool checkWin(vector<string>& inp, char check){
    REP(i, 4){
        bool iflag = true;
        REP(j, 4){
            if(inp[i][j] != check && inp[i][j] != 'T'){
                iflag = false;
                break;
            }
        }
        if(iflag)
            return true;
        iflag = true;
        REP(j, 4){
            if(inp[j][i] != check && inp[j][i] != 'T'){
                iflag = false;
                break;
            }
        }
        if(iflag)
            return true;
    }
    bool iflag = true;
    REP(i, 4){
        if(inp[i][i] != check && inp[i][i] != 'T'){
            iflag = false;
            break;
        }
    }
    if(iflag)
        return true;
    iflag = true;
    REP(i, 4){
        if(inp[i][4-i-1] != check && inp[i][4-i-1] != 'T'){
            iflag = false;
            break;
        }
    }
    if(iflag)
        return true;
    return false;
}

bool checkDraw(vector<string>& inp){
    REP(i, 4){
        REP(j, 4){
            if(inp[i][j] == '.')
                return false;
        }
    }
    return true;
}

int main(){
    int c;
    cin>>c;
    int k = 1;
    while(c--){
        vector<string> inp;
        REP(i, 4){
            string s;
            cin>>s;
            inp.pb(s);
        }
        cout<<"Case #"<<k<<": ";
        k++;
        if(checkWin(inp, 'X'))
            cout<<"X won"<<endl;
        else if(checkWin(inp, 'O'))
            cout<<"O won"<<endl;
        else if(checkDraw(inp))
            cout<<"Draw"<<endl;
        else
            cout<<"Game has not completed"<<endl;
    }
    return 0;
}
