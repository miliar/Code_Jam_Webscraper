#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
char x[103][103],y[103];
int a[103][103];
main(){
     int t,tt,m,n,i,j,k,s,ans;
     freopen("A-small.in","r",stdin);
     freopen("A-small.out","w",stdout);
     scanf("%d",&t);
     for(tt=1;tt<=t;tt++){
          scanf("%d",&m);
          gets(y);
          for(i=0;i<m;i++){
               gets(x[i]);
               //printf("%s\n",x[i]);
               //fflush(stdout);
          }
          scanf("%d",&n);
          gets(y);
          for(i=0;i<n;i++){
               gets(y);
               //printf("[%s]\n",y);
               //fflush(stdout);
               for(s=0;s<m;s++){
                    if(strcmp(x[s],y)==0){
                         break;
                    }
               }
               for(j=0;j<m;j++){
                    if(j==s){
                         a[i][j]=800;
                    }else if(i==0){
                         a[i][j]=0;
                    }else{
                         a[i][j]=a[i-1][j];
                         for(k=0;k<m;k++){
                              if(k!=j){
                                   a[i][j]<?=a[i-1][k]+1;
                              }
                         }
                    }
                    //printf("%3d ",a[i][j]);
               }
               //printf("\n");
          }
          ans = a[n-1][0];
          for(j=1;j<m;j++){
               ans <?= a[n-1][j];
          }
          printf("Case #%d: %d\n",tt,ans);
     }
     return 0;
}
