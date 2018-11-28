#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int t,a,b;

int dfs(int n){
  int i,k,s=0,l=1;
  int q[10];
  for (k=n/10;k;k/=10) l*=10;
  for (k=(n%10)*l+n/10;k!=n;k=(k%10)*l+k/10)
    if (k<n && k>=a){
      for (i=0;i<s;i++)
        if (q[i]==k) break;
      if (i==s || q[i]!=k) q[s++]=k;
    }
  return s;
}

int main(){
  int i,k,s;
//  freopen("c.in","r",stdin);
//  freopen("c.out","w",stdout);
  scanf("%d",&t);
  for (k=1;k<=t;k++){
    printf("Case #%d: ",k);
    scanf("%d%d",&a,&b);
    s=0;
    for (i=a+1;i<=b;i++) s+=dfs(i);
    printf("%d\n",s);
  }
  return 0;
}
