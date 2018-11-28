#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<string>
using namespace std;
const int N=10;
char mz[N][N];
bool check_row(int x,char s){
    for (int i=0;i<4;i++){
        if (mz[x][i]!=s && mz[x][i]!='T') return 0;
    }
    return 1;
}

bool check_col(int x,char s){
    for (int i=0;i<4;i++){
        if (mz[i][x]!=s && mz[i][x]!='T') return 0;
    }
    return 1;
}
void work(){
    int f1=0,f2=0;
    for (int i=0;i<4;i++){
        if (check_row(i,'X')) f1=1;
        if (check_row(i,'O')) f2=1;
        if (check_col(i,'X')) f1=1;
        if (check_col(i,'O')) f2=1;
    }
    int x=0,y=0,flag=1;
    for (int i=0;i<4;i++){
        if (mz[x][y]!='X' && mz[x][y]!='T'){
            flag=0;break;
        }
        x++;y++;
    }
    if(flag) f1=1;

    x=0,y=0,flag=1;
    for (int i=0;i<4;i++){
        if (mz[x][y]!='O' && mz[x][y]!='T'){
            flag=0;break;
        }
        x++;y++;
    }
    if(flag) f2=1;

    flag=1;
    x=0;y=3;
    for (int i=0;i<4;i++){
        if (mz[x][y]!='O' && mz[x][y]!='T'){
            flag=0;break;
        }
        x++;y--;
    }
    if (flag) f2=1;
    flag=1;

    x=0;y=3;
    for (int i=0;i<4;i++){
        if (mz[x][y]!='X' && mz[x][y]!='T'){
            flag=0;break;
        }
        x++;y--;
    }
    if (flag) f1=1;

    flag=1;
    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++){
            if (mz[i][j]=='.'){
                flag=0;break;
            }
        }
        if (flag==0) break;
    }
    if (f1 && f2==0) printf("X won\n");
    else if (f1==0 && f2) printf("O won\n");
    else if (flag==0) printf("Game has not completed\n");
    else if (flag) printf("Draw\n");
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while (T--){
        for (int i=0;i<4;i++){
            scanf("%s",mz[i]);
        }
        printf("Case #%d: ",++cas);
        work();
    }
    return 0;
}
