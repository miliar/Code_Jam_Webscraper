#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn=102;
int n,s,p,t;

int main(){
  int i,j,k,m1,m2,s1,s2;
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  scanf("%d",&t);
  for (k=1;k<=t;k++){
    printf("Case #%d: ",k);
    scanf("%d%d%d",&n,&s,&p);
    m1=max(3*p-4,1);
    m2=max(3*p-2,1);
    for (s1=s2=i=0;i<n;i++){
      scanf("%d",&j);
      if (j>=m1 && j<m2) s1++;
      else if (j>=m2) s2++;
    }
    s1=min(s1,s);
    if (p==0) printf("%d\n",n);
    else printf("%d\n",s1+s2);
  }
  return 0;
}
