#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

int B[101],O[101];
int n,t;
int a[101];
char c[101][2];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int i,k,on,bn,oi,bi,step;
    int o,b,ans;
    scanf("%d",&t);
    for(k=1;k<=t;++k){
        scanf("%d",&n);
        on=bn=oi=bi=0;
        for(i=0;i<n;++i){
            scanf("%s%d",c[i],&a[i]);
            if(strcmp(c[i],"O")==0)
                O[on++]=a[i];
            else
                B[bn++]=a[i];
        }
        o=b=1;
        ans=0;
        for(i=0;i<n;++i){
            if(strcmp(c[i],"O")==0){
                step=abs(a[i]-o)+1;
                ans+=step;
                o=a[i];
                if(step<abs(B[bi]-b)){
                    if(B[bi]>b)
                        b+=step;
                    else
                        b-=step;
                }else
                    b=B[bi];
                oi++;
            }else{
                step=abs(a[i]-b)+1;
                ans+=step;
                b=a[i];
                if(step<abs(O[oi]-o)){
                    if(O[oi]>o)
                        o+=step;
                    else
                        o-=step;
                }
                else
                    o=O[oi];
                bi++;
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
}
