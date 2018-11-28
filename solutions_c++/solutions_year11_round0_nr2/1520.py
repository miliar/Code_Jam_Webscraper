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
#include <string>
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
  int tc , opuestas , reemplazo , SZ , SZZ ; 
  cin>>tc;
  pair<char,char> t ;
  string current ,result , temp  ; 
  set< pair<char,char> > Sborra ;
  map<pair<char,char>,char> Mapea ;  
  

 for(int i = 1 ; i <= tc ; ++i ){
    
    Mapea.clear();
    Sborra.clear();
    result="";
    cin>>reemplazo;
    for(int j=0;j<reemplazo; ++j){
      cin>>temp;
      Mapea[mp(min(temp[0],temp[1]),max( temp[0],temp[1] ) ) ]= temp[2];
    }
    cin>>opuestas;
    for(int j = 0;j<opuestas;++j){
      cin>>temp;
      Sborra.insert(mp(min(temp[0],temp[1]),max(temp[0],temp[1] ) ) );
    }
    cin>>SZ; //fintea o como sea
    cin>>current;
    SZZ = 0 ;
    for(int j = 0 ; j < SZ ; ++ j){
        result += current[j];
        ++SZZ;
       if(SZZ>=2){
           t.first = min(result[SZZ-2],result[SZZ-1]);
           t.second = max(result[SZZ-2],result[SZZ-1]);
           char c;    
           if( c = Mapea[t] ){
              result.erase(result.begin()+ --SZZ );
              result[SZZ-1]=c;
           }   
           for(int k = 0 ; k < SZZ - 1 ; ++ k ){
             t.first = min(result[k],result[SZZ-1]);
             t.second = max(result[k],result[SZZ-1]);              
             if(Sborra.count(t)){SZZ=0;result="";}
           }
        }        
    }
    cout<<"Case #"<<i<<": [";
    if(SZZ>=1)cout<<result[0];
    for(int j = 1; j < SZZ ; ++j )
      cout<<", "<<result[j];
    cout<<"]"<<endl;
  }
   
  return 0;
}
