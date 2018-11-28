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

#define LL long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define mem(x,i) memset(x,i,sizeof(x))
#define cpresent(V,e) (find(all(V),(e))!=(V).end())
#define foreach(c,it) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define FOR(i,a,n) for(int (i)=(int)(a);i<(int)(n);++(i))
#define FORR(i,a,n) for(int (i)=(int)(a);i>(int)(n);--(i))

using namespace std;

long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}
long long lcm(long long a,long long b){return a*(b/gcd(a,b));}
long long bits(long long a){return a?1+bits(a&(a-1)):0;};
long long pot(long long a,long long b){if(!b)return 1;if(b&1)return a*pot(a*a,b>>1); else return pot(a*a,b>>1);}

const int elementos = 1000;
int table[elementos];

int main(){
 int tc ,el,ans; 
 cin>>tc;
 for(int i = 1 ; i <= tc ; ++i){
   cin>>el;
   ans =0;
   for(int j = 0 ; j < el ; ++j)
    cin>>table[j];
   sort(table,table+el);   
   for(int j=1;j<el; ++j){
    int a =0, b=0 , aa=0, bb=0;
    for(int k = 0 ; k < j ; ++k){
     a+=table[k];
     aa^=table[k];
    }    
    for(int k=j;k < el ; ++k)
    { b+=table[k];
      bb^=table[k];      
    }
    if(aa==bb)ans=max(ans,max(a,b));
   }
   cout<<"Case #"<<i<<": ";
   if(ans)cout<<ans;
   else cout<<"NO";
   cout<<endl;  
 }
 return 0;
}
