#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int x=1;x<=T;x++){
    string s; cin>>s;
    map<char,char> mp;
    
    int num=0;
    string str;
    for(int i=0;i<s.size();i++){
      if(i){
        if(mp[s[i]]==0){
          if(num==1)mp[s[i]]='0';
          else mp[s[i]]=num+'0';

          if(num==1)str+='0';
          else str+=num+'0';
          
          num++;
        }else{
          str+=mp[s[i]];
        }
      }
      else{
        mp[s[i]]='1';
        str+='1';
        num++;
      }
    }
    if(num==1)num++;
    long long ans=0;
    int a=str.size()-1;
    for(int i=0;i<str.size();i++){
      ans+=(long long)pow((double)num,(double)a)*(long long)(str[i]-'0');
      a--;
    }
    printf("Case #%d: %lld\n",x,ans);
  }
  return 0;
}