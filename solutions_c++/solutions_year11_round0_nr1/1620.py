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

int main(){
 int tc , sc , res , orange ,blue , pos , actual , naranja , azul , advance ; 
 bool dale;
 char color ;
 cin>>tc; 
 for(int i = 1 ; i <= tc ; ++i){
    orange = blue = 1 ;    
    naranja = azul  = 0;
    res = 0 ;
    cin>>sc;
    for(int j = 0 ; j < sc ; ++j){
      cin>>color>>pos;    
    // codealo  ahi
	if(color=='O'){
           if( pos < orange )  orange = ( orange - naranja > pos)? orange-naranja: pos ;
           else  orange = ( orange + naranja > pos ) ? pos : orange + naranja ;  
         
           res += (advance = abs(pos - orange) + 1 ); // 1 de push :)      

           naranja = 0;
           orange = pos ;
           azul += advance ;           
        }
  	else{           
           if( pos < blue )  blue = ( blue - azul > pos) ? blue-azul: pos ;
           else blue = ( blue + azul > pos ) ? pos : blue + azul ;
           res += ( advance = abs(pos - blue) + 1 ); // :) 1 de push

           azul = 0 ;
           blue = pos ; 
           naranja += advance ;          
        }
   //end code 
    //cout<<":"<<res<<"  "<<orange<<" ->"<<naranja<<"   "<<blue<<" ->"<<azul<<endl;
   }   
    cout<<"Case #"<<i<<": "<<res<<endl;
  }
 return 0;
}
