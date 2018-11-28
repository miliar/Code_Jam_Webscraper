#include <iostream>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
#define Si size()
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;
char a[10][10];
//int b[10][10];
int n;

bool check_x_win(){
    int b[5][5];
    for (int i=0;i<4;++i)
        for (int j=0;j<4;++j)
            if (a[i][j]=='X' || a[i][j]=='T')
                b[i][j]=1;
            else
                b[i][j]=0;
    for (int i=0;i<4;++i){
        if (b[i][1]+b[i][2]+b[i][3]+b[i][0]==4) return 1;
        if (b[1][i]+b[2][i]+b[3][i]+b[0][i]==4) return 1;
    }
    if (b[1][1]+b[2][2]+b[3][3]+b[0][0]==4) return 1;
    if (b[0][3]+b[1][2]+b[2][1]+b[3][0]==4) return 1;
    return 0;
}

bool check_o_win(){
    int b[5][5];
    for (int i=0;i<4;++i)
        for (int j=0;j<4;++j)
            if (a[i][j]=='O' || a[i][j]=='T')
                b[i][j]=1;
            else
                b[i][j]=0;
    for (int i=0;i<4;++i){
        if (b[i][1]+b[i][2]+b[i][3]+b[i][0]==4) return 1;
        if (b[1][i]+b[2][i]+b[3][i]+b[0][i]==4) return 1;
    }
    if (b[1][1]+b[2][2]+b[3][3]+b[0][0]==4) return 1;
    if (b[0][3]+b[1][2]+b[2][1]+b[3][0]==4) return 1;
    return 0;
}

bool check_draw(){
    for (int i=1;i<=4;++i)
        for (int j=1;j<=4;++j)
            if (a[i][j]=='.') return 0;
    return 1;
}

int main(){
    freopen("aa.in","r",stdin);
    freopen("aa.out","w",stdout);
    scanf("%d\n",&n);
    for (int T=1;T<=n;++T){
        printf("Case #%d: ",T);
        for (int i=0;i<4;++i){
            gets(a[i]);
            //puts(a[i]);
        }
        for (int i=0;i<4;++i){
            //puts(a[i]);
        }
        if (check_x_win()){
            printf("X won\n");
            getchar();
            continue;
        }
        if (check_o_win()){
            printf("O won\n");
            getchar();
            continue;
        }
        if (check_draw()){
            printf("Draw\n");
            getchar();
            continue;
        }
        else{
            printf("Game has not completed\n");
            getchar();
            continue;
        }
    }
    return 0;
}
