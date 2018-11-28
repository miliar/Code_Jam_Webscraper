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
    ll n, x[111], v[111], k, t, b;
    scanf("%lld%lld%lld%lld",&n,&k,&b,&t);
    REP(i,n)scanf("%lld",&x[i]);
    REP(i,n)scanf("%lld",&v[i]);
    bool can[111];
    REP(i,n){
      if(x[i]+t*v[i]>=b)can[i]=true;
      else can[i]=false;
    }
    if(k==0){printf(" 0\n");continue;};
    int f=0;
    bool found=false;
    for(int i=n-1;i>=0;i--)
      if(can[i]){
        f++;
        if(f==k){
          found=true;
          int res=0;
          int tmp=0;
          for(int j=i;j<n;j++)
            if(can[j])tmp++;
            else res+=tmp;
          printf(" %d\n",res);
          break;
        }
      }
    if(!found)printf(" IMPOSSIBLE\n");
  }
  return 0;
}
