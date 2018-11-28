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
//Main code starts here
int C,D,N;
char combine[(int)(255)][(int)(255)];
bool oppose[(int)(255)][(int)(255)];
string str;
string solve(){
    string ans;
    REP(i,N){
        if(SIZE(ans)==0){
            ans.push_back(str[(int)(i)]);
        }else{
            if(combine[(int)(ans[(int)(SIZE(ans)-1)])][(int)(str[(int)(i)])]!='0'){
                ans[(int)(SIZE(ans)-1)]=combine[(int)(ans[(int)(SIZE(ans)-1)])][(int)(str[(int)(i)])];
            }else{
                bool cleared=false;
                REP(j,SIZE(ans)){
                    if(oppose[(int)(ans[(int)(j)])][(int)(str[(int)(i)])]){
                        ans.clear();
                        cleared=true;
                        break;
                    }
                }
                if(!cleared){
                    ans.push_back(str[i]);
                }
            }
        }
    }
    return ans;
}


int main(){
    int Tests;
    cin >> Tests ;
    for(int tests=1;tests<=Tests;tests++){
        cout<<"Case #"<<tests<<": ";
        REP(i,255) REP(j,255){
            combine[(int)(i)][(int)(j)]='0'; 
            oppose[(int)(i)][(int)(j)]=false;
        }
        cin>>C;
        REP(i,C){
            string temp;
            cin>>temp;
            combine[(int)(temp[(int)(0)])][(int)(temp[(int)(1)])]=temp[(int)(2)];
            combine[(int)(temp[(int)(1)])][(int)(temp[(int)(0)])]=temp[(int)(2)];
        }
        cin>>D;
        REP(i,D){
            string temp;
            cin>>temp;
            oppose[(int)(temp[(int)(0)])][(int)(temp[(int)(1)])]=true;
            oppose[(int)(temp[(int)(1)])][(int)(temp[(int)(0)])]=true;
        }
        cin>>N;
        cin>>str;
        string ans=solve();
        cout<<"[";
        for(int i=0;i<SIZE(ans);i++){
            cout<<ans[(int)(i)];
            if(i!=SIZE(ans)-1){
                cout<<", ";
            }
        }
        cout<<"]\n";
    }
    return 0;
}
// That's all folks!