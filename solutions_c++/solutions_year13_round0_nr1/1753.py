#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;
#define L(x) tree[x].ch[0]
#define R(x) tree[x].ch[1]
#define INF 0x7fffffff
#define inf 99999999.9
#define eps 1e-9
#define MAXN 100015
#define db double
#define op operator
#define cp const P&
#define cs const
//typedef __int64 ll;
char s[5][5];
int Xr[4],Xl[4],Or[4],Ol[4],X1,O1,X2,O2;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas = 1;
    int i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        for(i = 0; i < 4; i ++){
            scanf("%s",s[i]);
        }
        memset(Xr,0,sizeof(Xr));
        memset(Xl,0,sizeof(Xl));
        memset(Or,0,sizeof(Or));
        memset(Ol,0,sizeof(Ol));
        X1 = X2 = O1 = O2 = 0;
        bool kong = false;
        for(i = 0; i < 4; i ++){
            for(j = 0; j < 4; j ++){
                if(s[i][j] == 'X'){
                    Xr[i] ++,Xl[j] ++;
                    if(i == j) X1 ++;
                    else if(i + j == 3) X2 ++;
                }
                else if(s[i][j] == 'O'){
                    Or[i] ++,Ol[j] ++;
                    if(i == j) O1 ++;
                    else if(i + j == 3) O2 ++;
                }
                else if(s[i][j] == 'T'){
                    Xr[i] ++,Xl[j] ++,Or[i] ++,Ol[j] ++;
                    if(i == j) X1 ++,O1 ++;
                    else if(i + j == 3) X2 ++,O2 ++;
                }
                else kong = true;
            }
        }
        char win = 'D';
        for(i = 0; i < 4; i ++){
            if(Xr[i] == 4||Xl[i] == 4) win = 'X';
        }
        if(X1 == 4||X2 == 4) win = 'X';
        char win2 = 'D';
        for(i = 0; i < 4; i ++){
            if(Or[i] == 4||Ol[i] == 4) win2 = 'O';
        }
        if(O1 == 4||O2 == 4) win2 = 'O';
        printf("Case #%d: ",cas ++);
        if(win == win2){
            if(kong) puts("Game has not completed");
            else puts("Draw");
        }
        else if(win == 'X'&&win2 == 'O') puts("Draw");
        else if(win == 'X') puts("X won");
        else puts("O won");
    }
return 0;
}
