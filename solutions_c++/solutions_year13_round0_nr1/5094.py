/*  Google Codejam Qualification Round 2013
 *  A Tic-Tac-Toe-Tomek 
 *  Varot Premtoon 13 Apr 2556
 */

#include <cstdio>

int sol(int cse)
{
    int i,j,k;
    int f = 1;
    int xr[] = {0,0,0,0};
    int xc[] = {0,0,0,0};
    int yr[] = {0,0,0,0};
    int yc[] = {0,0,0,0};
    int x1=0,x2=0,y1=0,y2=0;
    char tab[5][5];
    for(i=0;i<4;i++) scanf("%s",tab[i]);
    for(i=0;i<4;i++) for(j=0;j<4;j++) {
        if(tab[i][j]=='X' or tab[i][j]=='T') {
            xr[i]++;
            xc[j]++;
            if(i==j) x1++;
            if(i+j==3) x2++;
        } 
        if(tab[i][j]=='O' or tab[i][j]=='T') {
            yr[i]++;
            yc[j]++;
            if(i==j) y1++;
            if(i+j==3) y2++;
        } 
        if(tab[i][j]=='.') f = 0;
    }
    for(i=0;i<4;i++) {
        if(xr[i]==4 or xc[i]==4 or x1==4 or x2==4) {
            printf("Case #%d: X won\n",cse);
            return 0;
        }
        if(yr[i]==4 or yc[i]==4 or y1==4 or y2==4) {
            printf("Case #%d: O won\n",cse);
            return 0;
        }
    }

    if(f==1) printf("Case #%d: Draw\n",cse);
    else printf("Case #%d: Game has not completed\n",cse);
    return 0;
}

           
int main()
{
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++) sol(i);
    return 0;
}

