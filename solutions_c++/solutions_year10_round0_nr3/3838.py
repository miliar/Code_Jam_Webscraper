//Wojciech Kubies Potyczki Algorytmiczne 2010
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <algorithm>
#include <cmath>
#include <stack>
#include <iterator>
#include <deque>
#include <string>
#include <sstream>
#include <cstdio>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); i++)
#define FOR(i,a,b) for (int i=(a); i<=(b); i++)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define db(x) cerr << #x << " = " << x << "\n"; 
#define ALL(x) (x).begin(),(x).end()  
#define CLR(x) memset(x,0,sizeof x)  
#define SIZE(x) (int)x.size()
#define VAR(v,n) typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define beg ios_base::sync_with_stdio(0);
#define stop system("pause");
#define ends return 0;
#define MP make_pair
#define PB push_back
#define P push
#define ST first
#define ND second
#define PI 3.14159265358979323846 
template<class T> string tostring(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toint(string s){int n=0;istringstream sin(s);sin>>n;return n;}
const int INF = 1000000001;
const long double EPS = 10E-9;
typedef vector <int> vi;
typedef unsigned long long ull;
typedef pair <int,int> P;
typedef long double LD;
using namespace std;
int t,r,n,k,a,b,c,ans,ile;
queue <int> tab;
int main(){
    beg
    cin>>t;
    FOR(i,1,t){
       cin>>r>>k>>n;
       ans=a=c=0;
       REP(j,n){
          cin>>a;
          tab.P(a);
       }while(r){
          a=0; ile=0;
          for(;;){
             a+=tab.front();
             ile++;
             c=tab.front();
             if(a>k || ile>n){
                ans+=a-c;
                break;
             }tab.pop();
             tab.P(c);
          }r--;
       }cout<<"Case #"<<i<<": "<<ans<<"\n";
       while(!tab.empty()){
          tab.pop();
       }
    }ends; 
}
