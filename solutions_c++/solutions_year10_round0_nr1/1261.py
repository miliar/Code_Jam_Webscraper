#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<string>
#include<sstream>
#include<set>
#include<cmath>
#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define PB push_back
using namespace std;

int main()
{

    ios_base::sync_with_stdio(0);
    
   int t;cin>>t;
   REP(ww,t)
   {
           int N,K; cin>>N>>K;
           string ret="OFF";
           
           K=K%(int)pow(2.0,N);
           //cout<<K<<endl;
           if(K+1==(int)pow(2.0,N)) ret="ON";
                 
           cout<<"Case #"<<(ww+1)<<": "<<ret<<endl;
   }
}

    /*       vector<int> turned(N,0),power(N,0);
           power[0]=1;
           
           REP(i,K)
           {
                   vector<int> help=turned;
                   REP(i,turned.size())
                   {
                     if(power[i]) { (help[i]==0)?turned[i]=1:turned[i]=0;}
                   }
                   FOR(i,1,power.size()) if(turned[i-1]&&power[i-1]) power[i]=1; else power[i]=0;
           }
           if(turned[N-1]&&power[N-1]) ret="ON";*/
