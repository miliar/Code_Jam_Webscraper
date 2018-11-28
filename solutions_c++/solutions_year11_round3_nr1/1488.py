#include<cstdio>
using namespace std;
int r, c;
char mx[55][55];

bool check(){
    for(int i=0;i<r;i++)for(int j=0;j<c;j++){
        if(mx[i][j]=='#') return false;
    }
    return true;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        printf("Case #%d:\n",cas);
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++){
            scanf("%s",mx[i]);
        }
        for(int i=0;i<r-1;i++)for(int j=0;j<c-1;j++){
            if(mx[i][j]=='#' && mx[i][j+1]=='#' && mx[i+1][j]=='#' && mx[i+1][j+1]=='#'){
                mx[i][j]='/', mx[i][j+1]='\\', mx[i+1][j]='\\', mx[i+1][j+1]='/';
            }
        }

        if(check()){
            for(int i=0;i<r;i++) puts(mx[i]);
        }else puts("Impossible");
    }
}
