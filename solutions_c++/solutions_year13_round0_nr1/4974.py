#include <cstdio>

int main()
{
    //freopen ("input.txt","r",stdin);
    //freopen ("output.txt","w",stdout);
    int t,T;
    scanf ("%d",&T);
    for (t=1; t<=T; t++){
        int i, j;
        char s[4][4];
        bool point = false;
        bool player1 = false, player2 = false;
        bool flag1, flag2;
        scanf ("%s", &s[0]);
        scanf ("%s", &s[1]);
        scanf ("%s", &s[2]);
        scanf ("%s", &s[3]);
        for (i=0; i<4; i++)
        for (j=0; j<4; j++)
            if (s[i][j] == '.')
                point = true;
        
        for (i=0; i<4; i++){
            flag1 = true, flag2 = true;
            for (j=0; j<4; j++){
                if (s[i][j] != 'X' && s[i][j] != 'T')
                    flag1 = false;
                if (s[i][j] != 'O' && s[i][j] != 'T')
                    flag2 = false;
            }
            if (flag1) player1 = true;
            if (flag2) player2 = true;
            
            flag1 = true, flag2 = true;
            for (j=0; j<4; j++){
                if (s[j][i] != 'X' && s[j][i] != 'T')
                    flag1 = false;
                if (s[j][i] != 'O' && s[j][i] != 'T')
                    flag2 = false;
            }
            if (flag1) player1 = true;
            if (flag2) player2 = true;
        }
        flag1 = true, flag2 = true;
        for (i=0; i<4; i++){
            if (s[i][i] != 'X' && s[i][i] != 'T')
                flag1 = false;
            if (s[i][i] != 'O' && s[i][i] != 'T')
                flag2 = false;    
        }
        if (flag1) player1 = true;
        if (flag2) player2 = true;
        
        flag1 = true, flag2 = true;
        for (i=0; i<4; i++){
            if (s[i][3-i] != 'X' && s[i][3-i] != 'T')
                flag1 = false;
            if (s[i][3-i] != 'O' && s[i][3-i] != 'T')
                flag2 = false;    
        }
        if (flag1) player1 = true;
        if (flag2) player2 = true;
        
        if (player1)
            printf ("Case #%d: X won\n", t);
        else if (player2)
            printf ("Case #%d: O won\n", t);
        else if (point)
            printf ("Case #%d: Game has not completed\n", t);
        else
            printf ("Case #%d: Draw\n", t);
    }
}
