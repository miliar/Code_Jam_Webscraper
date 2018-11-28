#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<sstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
void solve(){
  int s;
  scanf(" %d ",&s);
  string e[100];
  char buff[200];
  for(int i=0;i<s;i++){
    gets(buff);
    e[i]=buff;
  }
  sort(e,e+s);
  int q;
  scanf(" %d ",&q);
  int m[100]={};
  for(int i=0;i<q;i++){
    gets(buff);
    string x=buff;
    int id=lower_bound(e,e+s,x)-e;
    for(int j=0;j<s;j++)
      if(j!=id)
        m[j]<?=m[id]+1;
    m[id]=q+2;
  }
  for(int j=1;j<s;j++)
    m[0]<?=m[j];
  printf("%d\n",m[0]);
}
int main(){
  int n;
  scanf(" %d ",&n);
  for(int t=1;t<=n;t++){
    printf("Case #%d: ",t);
    solve();
  }
}
