#include <cstdio>
#define isX(x) (x==2 || x==8)
#define isO(x) (x==4 || x==8)


int n;
int t[4][4];
char c;

void alg(int i){

    bool allFilled = 1, allX, allO;
    bool xWon = 0, oWon = 0;
    for(int j=0; j<4; j++){
        for(int k=0; k<4; k++){
            scanf("%c ", &c);
            switch(c){
                case '.' : t[j][k] = 1; break;
                case 'X' : t[j][k] = 2; break;
                case 'O' : t[j][k] = 4; break;
                case 'T' : t[j][k] = 8; break;
            }
            allFilled &= t[j][k]!=1;
        }
    }
    for(int j=0; j<4; j++){
        allX = 1;
        allO = 1;
        for(int k=0; k<4; k++){
            allO &= isO(t[j][k]);
            allX &= isX(t[j][k]);
        }
        xWon |= allX; oWon |= allO;
        allX = 1;
        allO = 1;
        for(int k=0; k<4; k++){
            allO &= isO(t[k][j]);
            allX &= isX(t[k][j]);
        }
        xWon |= allX; oWon |= allO;
    }
    allX = 1, allO = 1;
    for(int j=0; j<4; j++){
        allX &= isX(t[j][j]);
        allO &= isO(t[j][j]);
    }
    xWon |= allX; oWon |= allO;
    allX = 1, allO = 1;
    for(int j=0; j<4; j++){
        allX &= isX(t[j][3-j]);
        allO &= isO(t[j][3-j]);
    }
    xWon |= allX; oWon |= allO;
    printf("Case #%d: ", i+1);
    if(xWon) printf ("X won\n");
    if(oWon) printf ("O won\n");
    if(allFilled && !xWon && !oWon) printf("Draw\n"); 
    if(!xWon && !oWon && !allFilled) printf("Game has not completed\n");
    return;
}

int main(){
    scanf("%d ", &n);
    for(int i=0; i<n; i++){
        
        alg(i);

    }
    return 0;
}
