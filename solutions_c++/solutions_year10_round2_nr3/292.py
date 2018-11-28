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

const int MOD=100003;
int c[555][555];
int a[555][555];

int f(int n, int k){
  if(k==1){
    if(n>1)return 1;
    return 0;
  }
  if(k>=n)return 0;
  if(a[n][k]!=-1)return a[n][k];
  int r=0;
  for(int j=1;j<k;j++){
    int v = f(k, j) * c[n-k-1][k-j-1];
    v%=MOD;
    r+=v;
    r%=MOD;
  }
  return a[n][k]=r;
}

int main(){
  int _cases; scanf("%d",&_cases);
    CLEAR(c);
    c[0][0]=1;
    for(int i=1;i<555;i++){
      c[i][0]=1;
      for(int j=1;j<=i;j++)
        c[i][j]=(c[i-1][j-1]+c[i-1][j])%MOD;
    }
  memset(a,-1,sizeof(a)); 
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    int n;scanf("%d",&n);
    int s=0;
    for(int i=1;i<n;i++)s=(s+f(n,i))%MOD;
    printf(" %d\n",s);
 }
  return 0;
}
