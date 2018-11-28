#include <cstdio>

void main2()
{
    char grille[4][5];
    for (int i=0; i<4; i++)
        scanf("%s", grille[i]);
    
    bool fini = true;
    
    for (int i=0; i<4; i++)
    {
        int a, b, c;
        a = b = c = 0;
        for (int j=0; j<4; j++)
        {
            if (grille[i][j] == 'X') a++;
            if (grille[i][j] == 'O') b++;
            if (grille[i][j] == 'T') c++;
        }
        
        if (a+c == 4) { printf("X won\n"); return; }
        if (b+c == 4) { printf("O won\n"); return; }
        if (a+b+c < 4) fini = false;
    }
    
    for (int i=0; i<4; i++)
    {
        int a, b, c;
        a = b = c = 0;
        for (int j=0; j<4; j++)
        {
            if (grille[j][i] == 'X') a++;
            if (grille[j][i] == 'O') b++;
            if (grille[j][i] == 'T') c++;
        }
        
        if (a+c == 4) { printf("X won\n"); return; }
        if (b+c == 4) { printf("O won\n"); return; }
        if (a+b+c < 4) fini = false;
    }
    
    {
        int a, b, c;
        a = b = c = 0;
        for (int j=0; j<4; j++)
        {
            if (grille[j][j] == 'X') a++;
            if (grille[j][j] == 'O') b++;
            if (grille[j][j] == 'T') c++;
        }
        
        if (a+c == 4) { printf("X won\n"); return; }
        if (b+c == 4) { printf("O won\n"); return; }
        if (a+b+c < 4) fini = false;
    }
    
    {
        int a, b, c;
        a = b = c = 0;
        for (int j=0; j<4; j++)
        {
            if (grille[j][3-j] == 'X') a++;
            if (grille[j][3-j] == 'O') b++;
            if (grille[j][3-j] == 'T') c++;
        }
        
        if (a+c == 4) { printf("X won\n"); return; }
        if (b+c == 4) { printf("O won\n"); return; }
        if (a+b+c < 4) fini = false;
    }
    
    if (fini) printf("Draw\n");
    else printf("Game has not completed\n");
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int i=0; i<T; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
    }
}
