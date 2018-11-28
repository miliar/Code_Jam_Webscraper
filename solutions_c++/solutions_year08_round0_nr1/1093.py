#include <stdio.h>
#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

long i,j,n,m,t,p,k;
map <string,long> a[101];
char s[200][200],c[200];

main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d\n",&t);
  for(p=0;p<t;p++){
    scanf("%d\n",&n);
    for(i=0;i<n;i++)
      gets(s[i]);
    scanf("%d\n",&m);
    k=1; j=0;
    for(i=0;i<m;i++){
      gets(c);
      if(a[p][c]!=k){
        a[p][c]=k;
        j++;
      }
      if(j==n){
        j=1;
        k++;
        a[p][c]=k;
      }
    }
    printf("Case #%d: %d\n",p+1,k-1);
  }
}
