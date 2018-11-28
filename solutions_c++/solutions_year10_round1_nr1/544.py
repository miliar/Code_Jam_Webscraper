#include<cstdio>

const int MAXN=50+5;
const int dx[4]={0,1,1,1};
const int dy[4]={1,0,1,-1};

char a[MAXN][MAXN];
int N,K;

void load(){
    scanf("%d%d",&N,&K);
    for (int i=0;i<N;++i) scanf("%s",a[i]);
}

void solve(){
    int i,j,k,l;
    for (i=0;i<N;++i){
        k=N-1;
        for (j=N-1;j>=0;--j)if (a[i][j]!='.'){
            a[i][k]=a[i][j];
            if (j!=k) a[i][j]='.';
            --k;
        }
    }
    bool red=false,blue=false,can;
    for (i=0;i<N;++i)
        for (j=0;j<N;++j) if (a[i][j]!='.'){
            for (k=0;k<4;++k){
                can=true;
                for (l=1;l<K;++l){
                    if (i+dx[k]*l<0||i+dx[k]*l>=N||j+dy[k]*l<0||j+dy[k]*l>=N){
                        can=false;
                        break;
                    }
                    if (a[i+dx[k]*l][j+dy[k]*l]!=a[i][j]){
                        can=false;
                        break;
                    }
                }
                if (can){
                    if (a[i][j]=='B'){
                        blue=true;
                    }else{
                        red=true;
                    }
                }
            }
        }
    if (blue){
        if (red){
            printf("Both\n");
        }else{
            printf("Blue\n");
        }
    }else{
        if (red){
            printf("Red\n");
        }else{
            printf("Neither\n");
        }
    }
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
