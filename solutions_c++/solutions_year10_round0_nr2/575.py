#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<string>
#include<sstream>
#include<set>
#include<cmath>
#define REP(i,n) for(ll i=0;i<n;++i)
#define FOR(i,j,k) for(ll i=j;i<k;++i)
#define FORD(i,j,k) for(ll i=j;i>k;--i)
#define PB push_back
#define ll long long
using namespace std;

ll gcd(ll a,ll b)
{
  if(b==0) return a;
  else return gcd(b,a%b);
}

int main()
{
   ios_base::sync_with_stdio(0);
   int t;cin>>t;
   REP(ww,t)
   {
           ll N;cin>>N;vector<ll> t(N);
           REP(i,N) cin>>t[i];
           ll ret=0;
           vector<ll> pary;
           REP(i,N) FOR(j,i+1,N) if(abs(t[i]-t[j])) pary.PB(abs(t[i]-t[j]));
           sort(pary.begin(),pary.end());
           //REP(i,pary.size()) cout<<pary[i]<<" ";cout<<endl;
           ll T=pary[0];
           if(pary.size()>1) ll T=gcd(pary[0],pary[1]);
           REP(i,pary.size()) FOR(j,i+1,pary.size()) T=min(T,gcd(pary[j],pary[i]));
         //  cout<<T<<endl;
           (t[0]%T)?ret=T-t[0]%T:ret=0;
           
        
           
           cout<<"Case #"<<(ww+1)<<": "<<ret<<endl;
   }
}
