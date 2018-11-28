#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int tcase;

void solve(){
  
   vector < string > va,vb;
   int a,b; 
   cin>>a;  for(int i=1;i<=a;++i) { string nm; cin>>nm; va.push_back(nm); }
   cin>>b;  for(int i=1;i<=b;++i) { string nm; cin>>nm; vb.push_back(nm); }
   int n; string st; cin>>n>>st;
   vector < char > rs;
   for(int i=0;i<n;++i) {
        rs.push_back(st[i]);
        int sz = (int)rs.size()-1;
        for(int j=0;j<va.size();++j) 
          if( (rs.size()>=2 && va[j][0]==rs[sz] && va[j][1]==rs[sz-1]) || (rs.size()>=2 && va[j][0]==rs[sz-1] && va[j][1]==rs[sz]) ) {
              rs.pop_back(); rs.pop_back(); rs.push_back(va[j][2]); break;
          }
        for(int j=0;j<vb.size();++j){
           int sz = (int)rs.size()-1;   
           if(rs.size()>=2 && (rs[sz]==vb[j][0] || rs[sz]==vb[j][1])) {
               for(int k=0;k<sz;++k){
                  int idx = (vb[j][0]==rs[sz])?1:0; 
                  if(rs[k]==vb[j][idx]){
                       rs.clear();
                  }
               }
           }
        }  
      //  for(int j=0;j<rs.size();++j) cout<<rs[j]<<" "; cout<<endl;
   }
   cout<<"[";
   for(int i=0;i<rs.size();++i){
       if(i==(int)rs.size()-1) cout<<rs[i]; else cout<<rs[i]<<", ";
   } 
   cout<<"]"<<endl;
} 

int main(){
  cin>>tcase;
  for(int tc=1;tc<=tcase;++tc) {
   cout<<"Case #"<<tc<<": "; solve();
  }
  return 0;
}

