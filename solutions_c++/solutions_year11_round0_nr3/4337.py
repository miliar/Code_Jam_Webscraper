// ----------------
// Author - LUONG VAN DO
// google jam
// Time Limit
// ----------------
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <map>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int x[20],a[20],Ans,Sum,n;
void Check(int k){
   int p = a[x[1]];
   int s = a[x[1]];
   int o;
   for (int i=2;i<=k;i++){
      p = p^(a[x[i]]);
      s+=a[x[i]];
   }
   if (p==Sum-s){
      if (Ans<s) Ans = s;
   }
}
void Try(int i, int k){
   for (int j = x[i-1]+1;j<=n-k+i;j++){
      x[i] = j;
      if (i==k) Check(k);
      else Try(i+1,k);
   }
}
main(){
   //freopen("exam.inp","r",stdin);freopen("exam.out","w",stdout);
   int test,kas=0;
   scanf("%d",&test);
   while (test--){
      scanf("%d",&n);
      Sum = 0;
      Ans = -1;
      for (int i=1;i<=n;i++){
         scanf("%d",&a[i]);
         Sum+=a[i];
      }
      x[0] = 0;
      for (int i=1;i<=n-1;i++){
         Try(1,i);
      }
      if (Ans!=-1) printf("Case #%d: %d\n",++kas,Ans);
      else printf("Case #%d: NO\n",++kas);
   }
}
