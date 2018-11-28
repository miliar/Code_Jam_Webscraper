#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "A-large"
// #define TEST_NAME "A-sample"

bool prime[1000100];

inline ll inv(ll x,int p) {
     x=(x%p+p)%p;
     ll res=1;
     int pw=p-2;
     while(pw) {
          if(pw&1)res=(res*x)%p;
          x=(x*x)%p;
          pw>>=1;
     }
     return res;
}

void verify(int x[],int d,int k,int d10) {
     if(k>=2) {
          ll a,b;
          bool ok,ok2;
          ok2=false;
          for(int p=2;p<=d10;++p)
               if(prime[p]) {
                    if(x[1]!=x[0]) {
                         a=((ll)(x[2]-x[1])*inv(x[1]-x[0],p)+p)%p;
                         b=((x[1]-a*(ll)x[0])%p+p)%p;
                    }
                    else {a=1;b=0;}
                    bool ok=true;
                    REP(i,k+1)
                         if(x[i]>=p)ok=false;
                    REP(i,k-1)
                         if(x[i+1]!=(a*x[i]+b)%p)ok=false;
                    if(ok) {
                         if(x[k]!=(a*x[k-1]+b)%p) {
                         }
                         ok2=true;
                    }
               }
          if(!ok2) {
               cout<<"BUG!"<<endl;
               cout<<d<<" "<<k<<endl;
               REP(i,k+1)cout<<x[i]<<" ";cerr<<endl;
               exit(1);
          }
     }
     else {
          cerr<<"k<=1"<<endl;
     }
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int d,k,d10;
          int x[15];          
          set<int> variants;

          cin>>d>>k;
          REP(i,k)cin>>x[i];

          d10=1;
          REP(i,d)d10*=10;
          memset(prime,1,sizeof(prime));
          int a,b,ok;
          int kk=k;
          for(int p=2;p<=d10;++p)
               if(prime[p]) {
                    for(int j=p+p;j<=d10;j+=p)prime[j]=0;     
                    
                    if(k>=3&&x[1]!=x[0]) {
                         a=((ll(x[2]-x[1])*inv(x[1]-x[0],p))%p+p)%p;
                         b=((x[1]-a*(ll)x[0])%p+p)%p;
                    }
                    else {
                         a=1;
                         b=0;
                    }
                    ok=true;
                    REP(i,k)
                         if(x[i]>=p)ok=false;
                    if(k<=2&&x[1]!=x[0])ok=false;
                    if(k<=1)ok=false;
                    REP(i,k-1)
                         if(x[i+1]!=(a*(ll)x[i]+b)%p)ok=false;
                    if(ok) {
                         variants.insert((a*(ll)x[k-1]+b)%p);
//                          cout<<"p="<<p<<" a="<<a<<" b="<<b<<" next="<<(a*(ll)x[k-1]+b)%p<<endl;
                    }
               }

          cout<<"Case #"<<test<<": ";

//           FOREACH(r,variants) {
//                x[k]=*r;
//                verify(x,d,k,d10);
//           }
          
          if(SZ(variants)==1)cout<<*variants.begin()<<endl;
          else cout<<"I don't know."<<endl;

     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
