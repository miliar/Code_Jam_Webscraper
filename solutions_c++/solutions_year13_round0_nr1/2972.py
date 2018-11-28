#include<cstdio>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<math.h>
#include<iostream>
#include<ctype.h>
#define ll long long
using namespace std;
double pi=acos(-1.0);
char maps[5][5];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,ok,X,T,O,k=1,cnt;
    scanf("%d",&cas);
    while(cas--)
    {
        cnt=0;
        memset(maps,0,sizeof(maps));
    getchar();
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            scanf("%c",&maps[i][j]);
            if(maps[i][j]!='.') cnt++;
        }
        getchar();
    }
    ok=0;
    printf("Case #%d: ",k++);
    for(int i=0;i<4;i++)
    {
        X=T=O=0;
        for(int j=0;j<4;j++)
        {
            if(maps[i][j]=='O') O++;
            else if(maps[i][j]=='X') X++;
            else if(maps[i][j]=='T') T++;
        }
        if(X==4||X==3&&T==1) {ok=1;printf("X won\n");break;}
        else if(O==4||O==3&&T==1) {ok=1;printf("O won\n");break;}
    }
    if(!ok)
    {
        for(int i=0;i<4;i++)
        {
            X=T=O=0;
            for(int j=0;j<4;j++)
            {
                if(maps[j][i]=='O') O++;
                else if(maps[j][i]=='X') X++;
                else if(maps[j][i]=='T') T++;
            }
            if(X==4||X==3&&T==1) {ok=1;printf("X won\n");break;}
            else if(O==4||O==3&&T==1) {ok=1;printf("O won\n");break;}
        }
    }
    if(!ok)
    {
        X=T=O=0;
        for(int i=0;i<4;i++)
        {
            if(maps[i][i]=='O') O++;
            else if(maps[i][i]=='X') X++;
            else if(maps[i][i]=='T') T++;
        }
        if(X==4||X==3&&T==1) {ok=1;printf("X won\n");}
        else if(O==4||O==3&&T==1) {ok=1;printf("O won\n");}
    }
    if(!ok)
    {
        X=T=O=0;
        for(int i=0;i<4;i++)
        {
            if(maps[i][3-i]=='O') O++;
            else if(maps[i][3-i]=='X') X++;
            else if(maps[i][3-i]=='T') T++;
        }
        if(X==4||X==3&&T==1) {ok=1;printf("X won\n");}
        else if(O==4||O==3&&T==1) {ok=1;printf("O won\n");}
    }
    if(!ok&&cnt==16) printf("Draw\n");
    else if(!ok) printf("Game has not completed\n");
    }
    return 0;
}
