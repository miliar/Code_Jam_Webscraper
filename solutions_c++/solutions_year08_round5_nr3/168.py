#include<iostream>
char s[100][100];
int cmp[1100][1100],n,x[100][1100];
int ct(int p,int q){
     int a[110],b[110],i,pp=p,qq=q;
     for(i=0;i<n;i++){
          a[i]=p%2;p/=2;
     }
     for(i=0;i<n;i++){
          b[i]=q%2;q/=2;
     }
     for(i=0;i<n;i++){
          if(b[i]&&((i>0&&a[i-1])||(i<n-1&&a[i+1])||(i>0&&b[i-1])||(i<n-1&&b[i+1]))){
               return 0;
          }
     }
     //printf("CMP! %d %d\n",pp,qq);
     return 1;
}
main(){
     int tt,t,m,i,j,b[110],p,k,mx;
     freopen("c0.in","r",stdin);
     freopen("c0.out","w",stdout);
     scanf("%d",&t);
     n = 10;
     for(i=0;i<(1<<n);i++){
          for(j=0;j<(1<<n);j++){
               cmp[i][j]=ct(i,j);
          }
     }
     for(tt=1;tt<=t;tt++){
          scanf("%d",&m);
          scanf("%d",&n);
          for(i=0;i<m;i++){
               scanf("%s",s[i]);
          }
          for(i=0;i<m;i++){
               for(j=0;j<(1<<n);j++){
                    x[i][j]=0;
               }
          }
          for(i=0;i<m;i++){
               for(j=0;j<(1<<n);j++){
                    p = j;
                    int fl=0,nb=0;
                    for(k=0;k<n;k++){
                         b[k]=p%2;p/=2;
                         if(b[k]==1){nb++;}
                         if(b[k]==1&&((k>0&&b[k-1]==1)||s[i][k]=='x')){fl=1;}
                    }
                    if(!fl){
                         if(i==0){
                              x[i][j]=nb;
                         }else{
                              for(k=0;k<(1<<n);k++){
                                   if(cmp[j][k]){
                                        x[i][j]>?=x[i-1][k]+nb;
                                   }
                              }
                         }
                    }
               }
          }
          mx=0;
          for(j=0;j<(1<<n);j++){
               mx >?= x[m-1][j];
          }
          printf("Case #%d: %d\n",tt,mx);
     }
     return 0;
}
