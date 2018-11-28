#include <stdio.h>

int points, it, jt;

char A[4][4];

void read_data() {
    points = 0;
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%c", &A[i][j]);
            if (A[i][j] == '.')
                points = 1;
            if (A[i][j] == 'T') {
                it = i;
                jt = j;
            }
        }
        scanf("\n");
    }
    scanf("\n");
}

bool check(char c) {
    A[it][jt] = c;
    
    bool ret = false;
    
    //diagonala principala
    bool current = true;
    for (int i = 0; i < 4; i++)
        if (A[i][i] != c)
            current = false;
    if (current)
        ret = true;
        
    //diagonala secundara
    current = true;
    for (int i = 0; i < 4; i++)
        if (A[i][3 - i] != c)
            current = false;
    if (current)
        ret = true;
        
    //liniile
    for (int i = 0; i < 4; i++) {
        current = true;
        for (int j = 0; j < 4; j++)
            if (A[i][j] != c)
                current = false;
        if (current)
            ret = true;
    }
    
    //coloanele
    for (int i = 0; i < 4; i++) {
        current = true;
        for (int j = 0; j < 4; j++)
            if (A[j][i] != c)
                current = false;
        if (current)
            ret = true;
    }
    
    A[it][jt] = 'T';
    
    return ret;
}

int main() {
    
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    
    int T;
    scanf("%d\n", &T);
    
    for (int i = 0; i < T; i++) {
        read_data();
        
        /*for (int p = 0; p < 4; p++) {
            for (int q = 0; q < 4; q++)
                printf("%c", A[p][q]);    
            printf("\n");
        }
        printf("\n");*/
        
        printf("Case #%d: ", i + 1);
        
        if (check('X'))
            printf("X won\n");
        else {
            if (check('O'))
                printf("O won\n");
            else {
                if (points)
                    printf("Game has not completed\n");
                else
                    printf("Draw\n");
            }
        }
    }
    
    return 0;    
}
