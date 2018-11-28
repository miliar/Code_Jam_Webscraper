#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int C,D,N;
    map<string,string> comb;
    map<string,bool> del;
    
    cin>>C;
    for(int i=0;i<C;i++){
      string s,s1,s2;
      cin>>s;
      
      s2 += s[2];
      
      s1 += s[0];
      s1 += s[1];        
      comb[s1]=s2;
      
      s1 = "";
      s1 += s[1];
      s1 += s[0];
      comb[s1]=s2;
    }
    
    cin>>D;
    for(int i=0;i<D;i++){
      string s;
      cin>>s;
      
      del[s]=true;
      
      string s1;
      s1 += s[1];
      s1 += s[0];
      del[s1]=true;
    }
    
    cin>>N;
    string s,res;
    cin>>s;
    for(int i=0;i<N;i++){
      //combine
      if(res.size()>=1){
          string zad;
          zad += res[res.size()-1];
          zad += s[i];
          if(comb.find(zad)!=comb.end() ){
            res = res.substr(0,res.size()-1) + comb.find(zad)->second;
            continue;
          }
      }
      
      //delete
      if(res.size()>=1){
        bool ddd=false;
        
        for(int j=0;j<res.size();++j){
          string str;
          str += res[j];
          str += s[i];
          if(del.find(str)!=del.end() ){
            res="";
            ddd=true;
            break;
          }
        }
        
        if(ddd==true) continue;
      }
      
      res+=s[i];
    }

    cout<<"Case #"<<t<<": [";
    for(int i=0;i<res.size();++i){
      if(i>0) cout<<", ";
      cout<<res[i];
    }
    cout<<"]"<<endl;
  }
  
  return 0;
}