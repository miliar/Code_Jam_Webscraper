#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    multiset<int> mc;
    int n;
    cin>>n;
    REP(i,n){int v,p;cin>>p>>v; REP(i,v)mc.insert(p);};
    int res=0;
    while(1){
      bool ch=false;
      for(multiset<int>::iterator it=mc.begin();it!=mc.end();it++){
        int val=*it;
        if(mc.count(val)>1){
          ch=true;
          res++;
          mc.insert(val+1);mc.insert(val-1);
          mc.erase(mc.find(val));
          mc.erase(mc.find(val));
          break;
        }
      }
      if(!ch)break;
    }
    cout<<" "<<res<<endl;
  }
  return 0;
}
