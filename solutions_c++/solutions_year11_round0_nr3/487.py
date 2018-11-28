#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,k,tot,minn,tt;
    scanf("%d",&t);
    for (k=1;k<=t;k++){
      tt = 0; minn = 2000000000; tot=0;
      scanf("%d",&n);    
      while (n--){
        scanf("%d",&i);
        tot+=i;
        tt = (tt^i);      
        if (minn>i) minn=i;
      }        
      if (tt==0) printf("Case #%d: %d\n",k,tot-minn);
      else printf("Case #%d: NO\n",k);
    }
    return 0;   
}
