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

int k[800110];

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    ll l;
    int n,b[1000];
    cin>>l>>n;
    REP(i,n)cin>>b[i];
    memset(k,60,sizeof(k));
    k[0]=0;
    for(int i=0;i<=800000;i++)
      REP(j,n)k[i+b[j]]=min(k[i+b[j]], k[i]+1);
    ll m=-1;
    REP(i,n){
      ll p = (l - 800010)/(ll)b[i];
      ll ans=p;
      ll cl = l - p * (ll)b[i];
      while(cl>800000){
        cl-=b[i];
        ans++;
      }
      if(k[cl]>1000000)continue;
      ans += (ll)k[cl];
      if(ans < m||m==-1)m=ans;
    }
    if(m==-1)cout<<" IMPOSSIBLE"<<endl;
    else cout<<" "<<m<<endl;
  }
  return 0;
}
