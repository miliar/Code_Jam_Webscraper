#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>

using namespace std;

int del,insert,m,n;
int a[200],f[200][300];

int calc(int x){
    if(x==0) return 0;
    if(m==0) return 1000000;
    else return abs(x-1)/m*insert;
}
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int casenum;
    scanf("%d",&casenum);
    for(int t=1;t<=casenum;++t){
        scanf("%d%d%d%d",&del,&insert,&m,&n);
        for(int i=1;i<=n;++i) scanf("%d",&a[i]);
        for(int i=0;i<=255;++i) f[1][i]=min(abs(i-a[1]),insert+del);
        for(int i=2;i<=n;++i)
            for(int j=0;j<=255;++j){
                f[i][j]=del*(i-1);
                for(int k=i-1;k>=1;--k)
                    for(int t=0;t<=255;++t)
                        f[i][j]=min(f[i][j],f[k][t]+(i-k-1)*del+calc(abs(j-t)));
                f[i][j]+=min(abs(j-a[i]),insert+del);
            }
        int ans=f[n][0];
        for(int i=1;i<=255;++i) ans=min(ans,f[n][i]);
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
