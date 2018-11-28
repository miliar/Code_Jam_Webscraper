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
    set<string> dirs;
    dirs.insert("/");
    int a[2];scanf("%d%d",&a[0],&a[1]);
    int res=0;
    REP(x,2){
    REP(i,a[x]){
      char s[1111]; scanf("%s",s);
      vector<string> v=parse<string>(s+1,'/');
      string p="";
      REP(i,(int)v.size()){
        p+="/"+v[i];
        if(x==1 && !dirs.count(p))res++;
        dirs.insert(p);
      }
    }
    }
    printf(" %d\n",res);
  }
  return 0;
}
