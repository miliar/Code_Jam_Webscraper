#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main(){
   int t,r,k,n,st,s,m,tot,ttt;
   freopen("in","r",stdin);
   freopen("out","w",stdout);
   cin>>t;
   vector<int> v;
   for(int fc=1;fc<=t;fc++){
   st=0;
   tot=0;
   v.clear();
   cin>>r>>k>>n;
   for(int i=0;i<n;i++){
      cin>>ttt;
      v.push_back(ttt);
   }
   for(int i=0;i<r;i++){
      s=0;
      m=st;
      while(s+v[m]<=k){
         s=s+v[m];
         m++;
         m=m%n;
         if(m==st)
            break;
      }
      tot = tot + s;
      st=m;
   }
   cout<<"Case #"<<fc<<": "<<tot<<"\n";}
   return 0;
}
