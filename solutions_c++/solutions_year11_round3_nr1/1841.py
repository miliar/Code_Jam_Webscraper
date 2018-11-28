/*  Google Code Jam Round 1B 2011
    Problem A. Square Tiles
    Varot Premtoon 22 May 2554 */

#include <cstdio>

int r,c;
char tab[100][100];

int rep()
{
    int i,j;
    for(i=0;i<r-1;i++) {
        for(j=0;j<c-1;j++) {
            if(tab[i][j]=='#'&&tab[i+1][j]=='#'&&tab[i][j+1]=='#'&&tab[i+1][j+1]=='#') {
                tab[i][j] = '/';
                tab[i+1][j] = '\\';
                tab[i][j+1] = '\\';
                tab[i+1][j+1] = '/';
                return 1;
            }
        }
    }
    return 0;
}

int sol(int cse)
{
    int i,j;
    printf("Case #%d:\n",cse);
    scanf("%d %d",&r,&c);
    for(i=0;i<r;i++) scanf("%s",tab[i]);
    while(rep());
    for(i=0;i<r;i++) {
        for(j=0;j<c;j++) {
            if(tab[i][j]=='#') {
                printf("Impossible\n");
                return 0;
            }
        }
    }
    for(i=0;i<r;i++) {
        for(j=0;j<c;j++) printf("%c",tab[i][j]);
        printf("\n");
    }
    return 0;
}


int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=0;i<t;i++) sol(i+1);
    return 0;
}
