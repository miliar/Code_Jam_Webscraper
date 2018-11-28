#include<cstdio>
#include<cstring>
#include<cstdlib>

const int MAXN=100+1;

int a[MAXN];
int f[MAXN][256];

int D,I,M,N;

void load(){
    scanf("%d%d%d%d",&D,&I,&M,&N);
    for (int i=1;i<=N;++i){
        scanf("%d",&a[i]);
    }
}

void solve(){
    memset(f,0,sizeof(f));
    int i,j,k,tmp;
    for (j=0;j<=255;++j)
        f[1][j]=abs(j-a[1]);
    for (i=2;i<=N;++i){
        for (j=0;j<=255;++j){
            f[i][j]=f[i-1][j]+D;
            for (k=0;k<=255;++k)if (M==0){
                    if (j!=k) continue;
                    if (f[i][j]>f[i-1][k]+int(abs(a[i]-k)))
                        f[i][j]=f[i-1][k]+int(abs(a[i]-k));
                    if (f[i-1][k]+D<f[i][j])
                        f[i][j]=f[i-1][k]+D;
            }else{
                tmp=abs(j-a[i])+f[i-1][k];
                tmp+=(int(abs(j-k))-1)/M*I;
                if (tmp<f[i][j]) f[i][j]=tmp;
            }
        }
    }
    tmp=999999999;
    for (j=0;j<=255;++j) if (tmp>f[N][j]) tmp=f[N][j];
    printf("%d\n",tmp);
}

int main(){
    int CN;
    scanf("%d",&CN);
    for (int ct=1;ct<=CN;++ct){
        load();
        printf("Case #%d: ",ct);
        solve();
    }
    return 0;
}
