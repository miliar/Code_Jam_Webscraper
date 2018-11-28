#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
  int T;
  cin>>T;
  for(int x=1;x<=T;x++){
    string s;
    int out=1;
    cin>>s;
    
    for(;next_permutation(s.begin(),s.end());){
      out=0;
      break;
    }
    if(out){
      string p="0";
      p+=s;
      for(;next_permutation(p.begin(),p.end());){
        if(p[0]!='0')break;
      }
      printf("Case #%d: %s\n",x,p.c_str());
    }else{
      printf("Case #%d: %s\n",x,s.c_str());
    }
  }
  return 0;
}