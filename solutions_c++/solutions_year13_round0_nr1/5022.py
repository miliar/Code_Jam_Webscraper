#include <stdio.h>
#include <stdlib.h>
    int T;
    char a[4][10];
    
int check(char c) {
    
    int j;
    for (int i = 0 ; i < 4 ; i++){
        for (j = 0 ;j < 4; j++){
            if (a[i][j] != c && a[i][j] != 'T') {
                break;
            }
        }
        if (j >= 4) {
            return 1;
        }
        for (j = 0; j < 4; j++){
            if (a[j][i] != c && a[j][i] != 'T') {
                break;
            }
        }
        if (j >= 4) {
            return 1;
        }
    }
    
        for (j = 0 ;j < 4; j++){
            int i = 3-j;
            if (a[i][j] != c && a[i][j] != 'T') {
                break;
            }
        }
        if (j >= 4) {
            return 1;
        }
        for (j = 0; j < 4; j++){
            if (a[j][j] != c && a[j][j] != 'T') {
                break;
            }
        }
        if (j >= 4) {
            return 1;
        }
    return 0;
}

int find(){
    for (int i = 0 ; i< 4 ; i++){
        for (int j = 0 ; j < 4; j++){
            if (a[i][j] == '.') return 1;
        }
    }
    return 0;
}
int main(char** arg) {
    freopen("in1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    

    scanf("%d",&T);
    for (int t = 1 ; t <= T ; t++){
        for (int i = 0 ; i < 4;  i++){
            scanf("%s",a[i]);
        }
     /*   
        for (int i = 0 ; i < 4 ; i++){
            for (int j = 0 ; j < 4; j++){
                printf("%c",a[i][j]);
            }
            printf("\n");
        }
        //*/
        int x = check('X');
        int o = check('O');
        int k = find();
        printf("Case #%d: ",t);
        if (x == 1) {
            printf("X won");
        } else if (o == 1) {
            printf("O won");
        } else if (k == 1) {
            printf("Game has not completed");
        } else {
            printf("Draw");
        }
        printf("\n");
        
        //scanf("%s",a[0]);
    }
    
   // for(;;);
}
