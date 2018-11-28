/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;

ll gcd(ll a,ll b){
    if(a<b) return gcd(b,a);
    if(a==b) return a;
    if(b==0) return a;
    return gcd(b,a%b);
    
}

ll gcd3(ll a,ll b,ll c){
    return gcd(a,gcd(b,c));
}

int main(int argc,char **argv){
    int no,tc=1,N;
    scanf(" %d",&no);
    while(no--){
            scanf(" %d",&N);
            int i;

            ll x;
            set<ll> s;

            for(i=0;i<N;i++) { scanf(" %lld",&x);
            s.insert(x); }

            vector<ll> v(s.begin(),s.end());

            int n=v.size();

            ll ans;


            printf("Case #%d: ",tc++);

            if(n==1) printf("0\n");
            else if(n==2){
                    ll k=(v[1] - v[0]);
                    if((v[1]%k)==0)  ans=0;
                    else { ll z=v[1]/k;z++;ans=z*k -v[1]; }
                    printf("%lld\n",ans);
            } else {
                    ll x1=v[2]-v[1],y1=v[1]-v[0],z1=v[2]-v[0];
                    ll k=gcd3(x1,y1,z1);
                    if((v[2]%k)==0) ans=0;
                    else {
                        ll z=v[2]/k; z++; ans=z*k -v[2];
                            
                    }

            printf("%lld\n",ans);
            }


    }
    return 0;
}

