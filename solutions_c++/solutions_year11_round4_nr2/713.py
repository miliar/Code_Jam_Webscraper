#define eps 1e-8
#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
int arr[505][505];
int min(int a,int b){return a<b?a:b;}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,cs,r,c,d,i,j,ii,jj,k;
    char ch;
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        scanf("%d%d%d",&r,&c,&d);
        for(i=0;i<r;++i){
            for(j=0;j<c;++j){
                cin>>ch;
                arr[i][j]=d+ch-48;
            }
        }
        for(k=min(r,c);k>=3;--k){
            for(i=0;i<r;++i){
                for(j=0;j<c;++j){
                    if(!(i+k<=r&&j+k<=c)) continue;
                    double mx=0,my=0,xx,yy;
                    xx=yy=(double)k/2.0;
                    for(ii=i;ii<i+k;++ii){
                        for(jj=j;jj<j+k;++jj){
                            if(ii==i&&jj==j) continue;
                            if(ii==i+k-1&&jj==j+k-1) continue;
							if(ii==i&&jj==j+k-1) continue;
							if(ii==i+k-1&&jj==j) continue;
                            mx+=((ii-i+0.5)-xx)*arr[ii][jj];
                            my+=((jj-j+0.5)-yy)*arr[ii][jj];
                        }
                    }
                    if(fabs(mx)<eps&&fabs(my)<eps) goto hell;
                }
            }
        }
        hell:
        printf("Case #%d: ",cs);
        if(k<3) printf("IMPOSSIBLE\n");
        else printf("%d\n",k);
    }
    return 0;
}
