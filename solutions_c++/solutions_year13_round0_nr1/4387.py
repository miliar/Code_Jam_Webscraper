#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 10 ;

char s[MAXN][MAXN];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;cin>>t;
    int cas=0;
    while (t--){
        for (int i=0;i<4;i++)
            scanf("%s",s[i]);
        bool Xwin=false,Owin=false;

        for (int i=0;i<4;i++){
            int X=0,O=0,T=0;
            for (int j=0;j<4;j++){
                if (s[i][j]=='X') X++;
                if (s[i][j]=='T') T++;

                if (s[i][j]=='O') O++;
            }
            if (X==4 || (X==3 && T==1)) Xwin=true;
            if (O==4 || (O==3 && T==1)) Owin=true;
        }
        for (int i=0;i<4;i++){
            int X=0,O=0,T=0;
            for (int j=0;j<4;j++){
                if (s[j][i]=='X') X++;
                if (s[j][i]=='T') T++;
                if (s[j][i]=='O') O++;
            }
            if (X==4 || (X==3 && T==1)) Xwin=true;
            if (O==4 || (O==3 && T==1)) Owin=true;
        }
        int X=0,O=0,T=0;
        for (int i=0;i<4;i++)
        {
            if (s[i][i]=='X') X++;
            if (s[i][i]=='T') T++;
            if (s[i][i]=='O') O++;
        }
        if (X==4 || (X==3 && T==1)) Xwin=true;
        if (O==4 || (O==3 && T==1)) Owin=true;

        X=0;O=0;T=0;
        for (int i=0;i<4;i++)
        {
            if (s[i][3-i]=='X') X++;
            if (s[i][3-i]=='T') T++;
            if (s[i][3-i]=='O') O++;
        }
        if (X==4 || (X==3 && T==1)) Xwin=true;
        if (O==4 || (O==3 && T==1)) Owin=true;

        printf("Case #%d: ",++cas);
        if (Xwin || Owin){
            if (Xwin)
                printf("X won\n");
            else
                printf("O won\n");
        }else{
            bool cc=false;
            for (int i=0;i<4;i++)
                for (int j=0;j<4;j++)
                    if (s[i][j]=='.') cc = true ;
            if (cc)
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }
    }
    return 0;
}
