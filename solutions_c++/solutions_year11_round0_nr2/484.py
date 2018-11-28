#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char cs[100][10],ds[100][10],s[1111],st[1111],ccc;
int c,d,ls;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,k,tot,minn,tt,ll;
    scanf("%d",&t);
    for (k=1;k<=t;k++){
      scanf("%d",&c);
      ls=0;
      for (i=0;i<c;i++)
          scanf("%s",cs[i]);
      scanf("%d",&d);
      for (i=0;i<d;i++)
          scanf("%s",ds[i]);
           
      scanf("%d",&n);   
      scanf("%s",st);
      for (i=0;i<n;i++){
         s[ls++]=st[i];
         
         if (ls>=2)
         for (j=0;j<c;j++)
           if ((s[ls-1]==cs[j][1]&&s[ls-2]==cs[j][0])||(s[ls-1]==cs[j][0]&&s[ls-2]==cs[j][1])){
              ls--;
              s[ls-1] = cs[j][2];
              break;                                                                                    
           }   
                                                                                                     
         if (ls>=2)
         for (j=0;j<d;j++)
           if (s[ls-1]==ds[j][1]||s[ls-1]==ds[j][0]){
              if (s[ls-1]==ds[j][1])   
                ccc = ds[j][0];
              else ccc = ds[j][1];
              for (ll =0;ll<ls;ll++)
                  if (s[ll]==ccc) break;                                    
              if (ll<ls){
                ls = 0;
                break;           
              }                                                                                                                
           }                
      }
      printf("Case #%d: [",k);
      for (i=0;i<ls;i++){
          if (i<ls-1) printf("%c, ",s[i]);
          else printf("%c",s[i]);
      }
      printf("]\n");
    }
    return 0;   
}
