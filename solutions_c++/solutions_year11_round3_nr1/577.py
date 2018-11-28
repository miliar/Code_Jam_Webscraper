#include<stdio.h>

int R, C;
char a[55][55];

int check(int i, int k){
    if(i+1 >=R) return 0;
    if(k+1 >=C) return 0;
    if(a[i+1][k]!='#') return 0;
    if(a[i][k+1]!='#') return 0;
    if(a[i+1][k+1]!='#') return 0;

    a[i][k]='/';
    a[i][k+1]='\\';
    a[i+1][k]='\\';
    a[i+1][k+1]='/';
    return 1;
}

int main(){
    int T ;
    int g, i, k;

    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d ", &R, &C);
        for(i=0; i<R; i++)
            for(k=0; k<C; k++)
                scanf("%c ", &a[i][k]);
        
        int t=1;
        for(i=0; i<R; i++)
            for(k=0; k<C; k++){
                if(a[i][k]=='#'){
                    t=check(i, k);
                    if(t==0) goto aqui;
                }
            }
        aqui:
        printf("Case #%d:\n", g);
        if(t==0)
            printf("Impossible\n");

        else{
            for(i=0; i<R; i++){
                for(k=0; k<C; k++){
                    printf("%c", a[i][k]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}
