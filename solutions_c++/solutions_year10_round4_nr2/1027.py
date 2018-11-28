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
#define REPD(i,n) for(ll i=n;i>-1;--i)
#define FOR(i,j,k) for(ll i=j;i<k;++i)
#define FORD(i,j,k) for(ll i=j;i>k;--i)
#define PB push_back
#define ll long long
using namespace std;

int main()
{
   ios_base::sync_with_stdio(0);
   int T;cin>>T;
   REP(ww,T)
   {
          int P;cin>>P;
          vector<int> M((int)pow(2.0,P),0);
          REP(i,M.size()) cin>>M[i];
          
          vector<vector<int> >pr;
          
          REP(i,P)
          {
            int w; 
             REP(j,(int)pow(2.0,P-(i+1))) cin>>w;
          }
           
         // REP(i,M.size()) cout<<M[i]<<" ";cout<<endl;
          
          vector<int> mt((int)pow(2.0,P)-1,0);
          mt[0]=(int) pow(2.0,P);
          
         REP(i,mt.size())
          {
             if(2*i+1<mt.size()) mt[2*i+1]=mt[i]/2;
             if(2*i+2<mt.size()) mt[2*i+2]=mt[i]/2;
          }
         // REP(i,mt.size()) cout<<mt[i]<<" ";cout<<endl;
          vector<int> acc((int)pow(2.0,P)-1,0);
          REP(i,M.size())
          { //cout<<i<<": ";
          int tmp=i;
              int j=0;
              int wsk=P-M[i];
              while(wsk&&j<mt.size())
              {    
              //     cout<<j<<" ";
                   acc[j]=1;
                   if(tmp<(mt[j]/2))
                   {
                     j=2*j+1;
                   }
                   else {
                        tmp-=mt[j]/2;
                        j=2*j+2;
                   }
                   --wsk;     
              }
          //    cout<<endl;
          }
         
          // REP(i,mt.size()) cout<<mt[i]<<" ";cout<<endl;
          
        //  REP(i,acc.size()) cout<<acc[i]<<" ";cout<<endl;
           ll ret=0;
           
          REP(i,acc.size())if(acc[i]) ++ret;
          
           
           cout<<"Case #"<<(ww+1)<<": "<<ret<<endl;
   }
}



