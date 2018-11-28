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

ll a[11][1111][11];
int p;
int pr[11][1111];
int c[1111];

ll f(int r, int m, int sel){
  if(r==0){
    if(sel>=c[m])return 0;
    return 100000000000LL;
  }
  if(a[r][m][sel]!=-1)return a[r][m][sel];
  ll res=f(r-1,2*m,sel)+f(r-1,2*m+1,sel);
  res=min(res,f(r-1,2*m,sel+1)+f(r-1,2*m+1,sel+1)+pr[r][m]);
  return a[r][m][sel] = res;
}

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    memset(a,-1,sizeof(a));
    scanf("%d",&p);
    int n=1<<p;
    REP(i,n){scanf("%d",&c[i]);c[i]=p-c[i];}
    for(int i=1;i<=p;i++)REP(j,(1<<(p-i)))scanf("%d",&pr[i][j]);
    printf(" %lld\n",f(p,0,0));


  }
  return 0;
}
