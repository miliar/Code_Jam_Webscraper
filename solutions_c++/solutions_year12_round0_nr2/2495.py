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

int val[200];
int n , s , p  ,ans ;

void solve(){
  ans = 0;
  sort(val,val+n);  
  int tmp , valu = 0 ;   
  for(int i = 0 ;i < n ; ++i ){
    if( valu < s ){
        tmp = val[i] - max(0,2 * ( p - 2 ));
        ans += (int)( tmp >= p);
        valu +=  (int)( tmp >= p);
    }
    else{
    
        tmp = val[i] - max(2 * ( p - 1 ),0);
        ans += (int)( tmp >= p);
    }                
  //  cout << tmp << "  " << val [i] << "  "<<  p<<endl;
  }   
  
  cout <<ans ;   
}

int main(){
   freopen("in.txt","r",stdin);
   freopen("sal.txt","w",stdout);
  
   int tc;
   cin >> tc;
   for(int i = 1 ;i <= tc ; ++i){
      cin >> n >> s >> p;     
      for(int j = 0 ; j < n ; ++j)
         cin >> val[j];
      cout << "Case #"<<i<<": ";
      solve();              
      cout <<endl;     
   }
}




