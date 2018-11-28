#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int tcase,n;

int solve(){
  int co = 1; int cb = 1;
  int to = 0; int tb = 0; int ct = 0;
  cin>>n;
  for(int i=1;i<=n;++i){
     string color; int nm;
     cin>>color>>nm;
     if(color=="O"){
       int nxt = to+abs(nm-co);
       if(nxt<=ct) ct++; else ct += nxt-ct+1; 
       co = nm; to = ct;
     }
     else {
       int nxt = tb+abs(nm-cb);
       if(nxt<=ct) ct++; else ct += nxt-ct+1;
       cb = nm; tb = ct;
     } 
  }
  return ct;
}

int main(){
   
   cin>>tcase;
   for(int tc=1;tc<=tcase;++tc){
     cout<<"Case #"<<tc<<": "<<solve()<<endl;
   } 
   return 0;
}


