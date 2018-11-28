#include <iostream>
#include <string>
using namespace std;
const int mo[4][2] = {-1,0,0,-1,0,1,1,0};
int a[110][110],f[110][110];
char ans[110][110];
bool vi[110][110];
int n,m,color;
int ch(int x,int y){
    int i,res(999999),k(4);
    for(i = 0;i < 4;++i){
        x += mo[i][0]; y += mo[i][1];
        if(x >= 0 && x < n && y >= 0 && y < m && a[x][y] < a[x-mo[i][0]][y-mo[i][1]])
            if(a[x][y] < res){
                res = a[x][y];
                k = i;
            }
        x -= mo[i][0]; y -= mo[i][1];
    }
    return k;
}
void dfs(int x,int y){
    ans[x][y] = color + 'a';
    for(int i = 0;i < 4;++i){
        x += mo[i][0]; y += mo[i][1];
        if(x >= 0 && x < n && y >= 0 && y < m && !vi[x][y] && f[x][y] == 3 - i || f[x-mo[i][0]][y-mo[i][1]] == i){
            vi[x][y] = 1;
            dfs(x,y);
        }
        x -= mo[i][0]; y -= mo[i][1];
    }
}
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I = 1;I <= N;++I){
        scanf("%d%d",&n,&m);
        for(int i = 0;i < n;++i)
            for(int j = 0;j < m;++j)
                scanf("%d",&a[i][j]);
        for(int i = 0;i < n;++i)
            for(int j = 0;j < m;++j)
                f[i][j] = ch(i,j);
        memset(vi,0,sizeof(vi));
        color = 0;
        for(int i = 0;i < n;++i)
            for(int j = 0;j < m;++j)
                if(!vi[i][j]){
                    vi[i][j] = 1;
                    dfs(i,j);
                    ++color;
                }
        printf("Case #%d:\n",I);
        for(int i = 0;i < n;++i)
            for(int j = 0;j < m;++j)
                printf("%c%c",ans[i][j],j < m-1?' ':'\n');
    }
}
