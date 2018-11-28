#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int a[110],f[110][256],del,ins,m,n;

void solve(){
    scanf("%d%d%d%d",&del,&ins,&m,&n);
    int i,j,k,cost,temp;
    for(i=1;i<=n;++i){
        scanf("%d",&a[i]);
        for(j=0;j<=255;++j){
            f[i][j]=f[i-1][j]+del;
            cost=abs(a[i]-j);
            for(k=0;k<=255;++k){
                temp=abs(j-k);
                if(temp<=m)f[i][j]=min(f[i][j],f[i-1][k]+cost);else {
                    if(m>0)
                        f[i][j]=min(f[i][j],(temp-1)/m*ins+f[i-1][k]+cost);
                }
            }
        }
    }
    for(i=1;i<=255;++i)f[n][0]=min(f[n][i],f[n][0]);
    printf("%d\n",f[n][0]);
}


int main(){
    freopen("gcjb.in","r",stdin);
    freopen("gcjb.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        solve();
    }

}

