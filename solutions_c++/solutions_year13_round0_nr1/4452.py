#include <cstdio>
#include <cstring>


char tt[10][10];
int main()
{
    freopen("1aa.in", "r", stdin);
    freopen("1a.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int I=1; I<=T; ++I){
        for (int i=0; i<4; ++i)
            scanf("%s", tt+i);
        printf("Case #%d: ", I);
        bool xwin = false;
        bool owin = false;
        for (int i=0; i<4; ++i)
        {
            bool xs = true;
            for (int j=0; j<4; ++j)
            {
                if(tt[i][j]=='.' || tt[i][j]=='O')xs=false;
            }
            if(xs)xwin=true;
            xs=true;
            for (int j=0; j<4; ++j)
                if(tt[j][i]=='.' || tt[j][i]=='O')xs=false;
            if(xs)xwin =true;
        }
        bool xd = true;
        for (int i=0; i<4; ++i)
            if(tt[i][i]=='.' || tt[i][i] == 'O')xd=false;
        if(xd)xwin =true;
        xd = true;
        for (int i=0; i<4; ++i)
            if(tt[i][3-i]=='.' || tt[i][3-i] == 'O')xd=false;
        if(xd)xwin =true;
        
        for (int i=0; i<4; ++i)
        {
            bool xs = true;
            for (int j=0; j<4; ++j)
            {
                if(tt[i][j]=='.' || tt[i][j]=='X')xs=false;
            }
            if(xs)owin=true;
            xs=true;
            for (int j=0; j<4; ++j)
                if(tt[j][i]=='.' || tt[j][i]=='X')xs=false;
            if(xs)owin =true;
        }
        xd = true;
        for (int i=0; i<4; ++i)
            if(tt[i][i]=='.' || tt[i][i] == 'X')xd=false;
        if(xd)owin =true;
        xd = true;
        for (int i=0; i<4; ++i)
            if(tt[i][3-i]=='.' || tt[i][3-i] == 'X')xd=false;
        if(xd)owin =true;
        
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
                if(tt[i][j]=='.')draw=false;
        if(draw)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
