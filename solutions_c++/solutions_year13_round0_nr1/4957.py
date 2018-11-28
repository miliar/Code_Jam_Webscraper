#include <stdio.h>
char grid[4][4];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,i,j,cc;
    for(cc=1,scanf("%d",&t);cc<=t;++cc){
        bool fin=true;
        for(i=0;i<4;++i) for(j=0;j<4;++j) {scanf(" %c",&grid[i][j]); if(grid[i][j]=='.') fin=false;}
        printf("Case #%d: ",cc);
        for(i=0;i<4;++i){
            for(j=0;j<4;++j) if(grid[i][j]!='X'&&grid[i][j]!='T') break;
            if(j==4) {printf("X won\n");break;}
            for(j=0;j<4;++j) if(grid[j][i]!='X'&&grid[j][i]!='T') break;
            if(j==4) {printf("X won\n");break;}
            for(j=0;j<4;++j) if(grid[i][j]!='O'&&grid[i][j]!='T') break;
            if(j==4) {printf("O won\n");break;}
            for(j=0;j<4;++j) if(grid[j][i]!='O'&&grid[j][i]!='T') break;
            if(j==4) {printf("O won\n");break;}
        }
        if(i<4) continue;
        for(j=0;j<4;++j) if(grid[j][j]!='X'&&grid[j][j]!='T') break;
        if(j==4) {printf("X won\n");continue;}
        for(j=0;j<4;++j) if(grid[j][3-j]!='X'&&grid[j][3-j]!='T') break;
        if(j==4) {printf("X won\n");continue;}
        for(j=0;j<4;++j) if(grid[j][j]!='O'&&grid[j][j]!='T') break;
        if(j==4) {printf("O won\n");continue;}
        for(j=0;j<4;++j) if(grid[j][3-j]!='O'&&grid[j][3-j]!='T') break;
        if(j==4) {printf("O won\n");continue;}
        if(fin) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
