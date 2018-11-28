#include<iostream>
using namespace std;
int t,k;
void solve(){
        int n,d,g,i,j;
        scanf("%d%d%d",&n,&d,&g);
//        if(n>100) n=100;
        if(n<0) n=100;
        if(d!=100 && g==100){
                  printf("Case #%d: Broken\n",k);
                  return;
        }
        if(d!=0 && g==0){
                  printf("Case #%d: Broken\n",k);
                  return;
        }
        for(i=1;i<=n;i++){
                   if(d*i/100.0-(int)(d*i/100.0)==0 ){
                                                  //  for(j=i;g*j/100.0-(int)(g*j/100.0)!=0 ||(int)(g*j/100.0)==0;j++){}
                                                    for(j=i;g*j/100.0-(int)(g*j/100.0)!=0 ||j<100000;j++){}
                                                         if(g*j/100.0-(int)(g*j/100.0)==0){
                                                                           printf("Case #%d: Possible\n",k);
                                                                           return;
                                                         }
                                                     }      
        }
        printf("Case #%d: Broken\n",k);
        return;
}
int main(){
   freopen("A-large.in", "r",stdin);
   freopen("A-large.out", "w",stdout);
   scanf("%d",&t);
   k=1;
   while(k<=t){
               solve();
               k++;
              //printf("Case #%d: %d\n",t);
   

   }
   getchar();
   getchar();
   return 0;
}
