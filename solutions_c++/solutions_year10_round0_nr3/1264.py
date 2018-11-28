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
           long long R,k,N; cin>>R>>k>>N;
         //  cout<<R<<" "<<k<<" "<<N<<endl;
   /*       queue<int> kol;
           REP(i,N) {int u;cin>>u;kol.push(u);}
           int ret=0;
           REP(i,R)
           {
                   int cnt=0;vector<int> tmp;
                   while(!kol.empty()&&cnt+kol.front()<=k)
                   {
                          tmp.PB(kol.front());
                          cnt+=kol.front();
                          kol.pop();
                   }
                   REP(j,tmp.size()) {//cout<<tmp[j]<<" ";
                   kol.push(tmp[j]);}
                //   cout<<"| "<<cnt<<endl;
                   ret+=cnt;
           }*/
           
           
           
           vector<long long> tmp(N); 
           vector<long long> start(N,0); start[0]=1;
           REP(i,N) cin>>tmp[i];
           vector<long long> groups,begins; begins.PB(0);
           long long ret=0;   
           
           long long wsk=0,cnt=0,p=0;
           while(true)
           {
             
             if(cnt+tmp[wsk]<=k) cnt+=tmp[wsk++];
             else
             {
                 groups.PB(cnt);
                 if(start[wsk]){ break;}
                 
                 start[wsk]=1; p=wsk;
                 begins.PB(p);
                 cnt=tmp[wsk++];
                 
                 
             } 
             
             if(wsk>=N) wsk-=N;
             if(wsk==p)
             {
              groups.PB(cnt); break;
             }
           } 
           
           
           
     //      REP(i,groups.size()) cout<<groups[i]<<" ";cout<<endl;
     //      REP(i,groups.size()) cout<<begins[i]<<" ";cout<<endl;
     //      cout<<wsk<<endl;
          if(R>groups.size())
          {
            long long j=0; while(j<begins.size()&&begins[j]!=wsk) {ret+=groups[j++];--R;}
             
            vector<int> help; FOR(i,j,groups.size()) help.PB(groups[i]);
      //      cout<<"! "<<j<<" "<<ret<<endl;
            long long ct=0; REP(i,help.size()) ct+=help[i];
      //      cout<<ct<<endl;
            ret+=ct*(long long)(R/help.size());
            R=R%help.size();
            REP(i,R) ret+=help[i];
          }
          else REP(i,R) ret+=groups[i];
              
           cout<<"Case #"<<(ww+1)<<": "<<ret<<endl;
   }
}
