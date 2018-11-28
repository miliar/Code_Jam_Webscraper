#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
#define eps 1e-8
char ss[500][501];
double Abs(double x){
    if(x<0)x=-x;
    return x;       
}
bool zero(double x){
    return Abs(x)<eps;     
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T,r,c,d,i,j,k;
    scanf("%d",&T);
    for(int test=0;test<T;test++){
        scanf("%d%d%d",&r,&c,&d);
        for(i=0;i<r;i++){
            scanf("%s",ss[i]);                 
        }bool ok=0;
        printf("Case #%d: ",test+1);
        for(k=min(r,c);k>=3;k--){
           for(i=0;i<r;i++){
               for(j=0;j<c;j++){
                   if(i+k-1<r&&j+k-1<c){
                       double cx,cy,xx=j+k*0.5,yy=r-1-i+1-k*0.5;
                       double sx=0,sy=0;
                       for(int ii=i;ii<i+k;ii++){
                               for(int jj=j;jj<j+k;jj++){
                                   if(ii==i&&jj==j+k-1)continue;
                                   if(ii==i&&jj==j)continue;
                                   if(ii==i+k-1&&jj==j+k-1)continue;
                                   if(ii==i+k-1&&jj==j)continue;
                                   cx=jj+0.5;cy=r-1-ii+0.5;
                                   sx+=(cx-xx)*(d+ss[ii][jj]-'0');
                                   sy+=(cy-yy)*(d+ss[ii][jj]-'0');
                               }
                       }
                       if(zero(sx)&&zero(sy)){
                           ok=1;
                           printf("%d\n",k);
                           break;
                                                  
                       }
                                            
                   } 
                   if(ok)break;              
               } 
               if(ok)break;                
        }
        if(ok)break;}
        if(k<3)puts("IMPOSSIBLE");
        //printf("Case #%d: %.8lf\n",test+1,sum);
                
    }
}
