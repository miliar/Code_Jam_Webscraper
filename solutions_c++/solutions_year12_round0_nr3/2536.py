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
#include <ctime>
#include <cstring>

#define ll long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define mem(x,i) memset(x,i,sizeof(x))
#define cpresent(V,e) (find(all(V),(e))!=(V).end())
#define foreach(c,it) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define f(i,a,n) for(int (i)=(int)(a);i<(int)(n);++(i))
#define fr(i,a,n) for(int (i)=(int)(a);i>(int)(n);--(i))

using namespace std;

long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}
long long lcm(long long a,long long b){return a*(b/gcd(a,b));}
long long bits(long long a){return a?1+bits(a&(a-1)):0;};
long long pot(long long a,long long b){if(!b)return 1;if(b&1)return a*pot(a*a,b>>1); else return pot(a*a,b>>1);}

int a , b , ans = 0;

inline void go( int g ){
  int pot = 1 , start , number = g , p2 = 1 , tmp ;
  while(p2<=g) p2  *= 10;
  p2/=10;       
  
  start = number / p2;
  number %= p2;
  pot *= 10;
  p2/= 10;
  set <int> S;
  while(number){
    tmp =  number * pot + start ;       
    pot *= 10 ;
    start  = start * 10 + number / p2 ;
    if( number/p2 != 0 && tmp > g && tmp <= b) S.insert(tmp);
    number %= p2 ;
    p2/= 10;     
  }      
  ans += S.sz;
}
inline void solve(){
      ans = 0;
      cin >> a >> b ;   
      while( a <= b ) { go(a) , ++a; }
}

int main(){
    freopen("sal.txt","w",stdout);
    freopen("in.txt","r",stdin);
    int tc ;
    cin >> tc ;
    
  //  go(a);
    for(int i = 1 ;i <= tc ; ++i){
      cout << "Case #"<<i<<": " ;        
      solve();      
      cout <<ans<<endl;
    }    
}













