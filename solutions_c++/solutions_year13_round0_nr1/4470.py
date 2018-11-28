#include <cstdio>
#include <cstring>

char tttt[10][10];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("hh.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int I=1; I<=T; ++I){
        printf("Case #%d: ", I);
        for (int i=0; i<4; ++i)
            scanf("%s", tttt+i);
        bool xwin = false;
        for (int i=0; i<4; ++i)
        {
            bool xs = true;
            for (int j=0; j<4; ++j)
            {
                if(tttt[i][j]=='.' || tttt[i][j]=='O')xs=false;
            }
            if(xs)xwin=true;
            xs=true;
            for (int j=0; j<4; ++j)
                if(tttt[j][i]=='.' || tttt[j][i]=='O')xs=false;
            if(xs)xwin =true;
        }
        bool xdd = true;
        for (int i=0; i<4; ++i)
            if(tttt[i][i]=='.' || tttt[i][i] == 'O')xdd=false;
        if(xdd)xwin =true;
        xdd = true;
        for (int i=0; i<4; ++i)
            if(tttt[i][3-i]=='.' || tttt[i][3-i] == 'O')xdd=false;
        if(xdd)xwin =true;

        bool owin = false;
        for (int i=0; i<4; ++i)
        {
            bool xs = true;
            for (int j=0; j<4; ++j)
            {
                if(tttt[i][j]=='.' || tttt[i][j]=='X')xs=false;
            }
            if(xs)owin=true;
            xs=true;
            for (int j=0; j<4; ++j)
                if(tttt[j][i]=='.' || tttt[j][i]=='X')xs=false;
            if(xs)owin =true;
        }
        xdd = true;
        for (int i=0; i<4; ++i)
            if(tttt[i][i]=='.' || tttt[i][i] == 'X')xdd=false;
        if(xdd)owin =true;
        xdd = true;
        for (int i=0; i<4; ++i)
            if(tttt[i][3-i]=='.' || tttt[i][3-i] == 'X')xdd=false;
        if(xdd)owin =true;

        if(xwin){
            printf("X won\n");
            continue;
        }
        if(owin){
            printf("O won\n");
            continue;
        }

        bool draw = true;
        for (int i=0; i<4; ++i)
            for (int j=0; j<4; ++j)
                if(tttt[i][j]=='.')draw=false;

        if(draw)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
