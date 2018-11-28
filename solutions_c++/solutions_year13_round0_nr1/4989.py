//COPYPASTA FTW

#include <cstdio>
#include <utility>
using namespace std;
#define PII pair<int, int>
#define MP make_pair
#define ST first
#define ND second
const int n = 4;

char t[7][7];

int winner()
{
    PII wyn;

    for(int i = 0; i < n; ++ i){
        wyn = MP(0, 0);

        for(int j = 0; j < n; ++ j){
            if(t[i][j] == 'X')
                wyn.ST ++;
            else
                if(t[i][j] == 'O')
                    wyn.ND ++;
            else
                if(t[i][j] == 'T'){
                    wyn.ND ++;
                    wyn.ST ++;
                }
        }
        if(wyn.ST == 4) return 1;
        if(wyn.ND == 4) return 2;
    }


    for(int i = 0; i < n; ++ i){
        wyn = MP(0, 0);

        for(int j = 0; j < n; ++ j){
            if(t[j][i] == 'X')
                wyn.ST ++;
            else
                if(t[j][i] == 'O')
                    wyn.ND ++;
            else
                if(t[j][i] == 'T'){
                    wyn.ND ++;
                    wyn.ST ++;
                }
        }
        if(wyn.ST == 4) return 1;
        if(wyn.ND == 4) return 2;
    }

    wyn = MP(0, 0);
    for(int i = 0, j = 0; i < n; ++ i, ++ j){


        if(t[i][j] == 'X')
            wyn.ST ++;
        else
            if(t[i][j] == 'O')
                wyn.ND ++;
        else
            if(t[i][j] == 'T'){
                wyn.ND ++;
                wyn.ST ++;
            }

        if(wyn.ST == 4) return 1;
        if(wyn.ND == 4) return 2;
    }

    wyn = MP(0, 0);
    for(int i = 0, j = 3; i < n; ++ i, -- j){


        if(t[i][j] == 'X')
            wyn.ST ++;
        else
            if(t[i][j] == 'O')
                wyn.ND ++;
        else
            if(t[i][j] == 'T'){
                wyn.ND ++;
                wyn.ST ++;
            }

        if(wyn.ST == 4) return 1;
        if(wyn.ND == 4) return 2;
    }

    return 0;
}

bool fill()
{
    for(int i = 0; i < n; ++ i)
        for(int j = 0; j < n; ++ j)
            if(t[i][j] == '.')
                return 0;
    return 1;
}

int main()
{
    int z;
    scanf("%d", &z);
    int nr = 1;
    while(nr <= z){

        scanf("\n");
        for(int i = 0; i < n; ++ i){
            gets( t[i] );
        }

        int win = winner();
        printf("Case #%d: ", nr);
        if(win == 1) puts("X won");
        else if(win == 2) puts("O won");
        else if( fill() ) puts("Draw");
        else puts("Game has not completed");

        nr ++;
    }
}
