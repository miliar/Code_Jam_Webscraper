#include <stdio.h>
#include <stdlib.h>
int main(void){
    char b[8][8];
    int T, i,j,k,z,ans,spi,spj;
    scanf("%d",&T);
    FILE* bob;
    bob=fopen("a.txt","w");
    for(z=0;z<T;z++)
    {
        ans=-1; 
        for(j=0;j<4;j++) scanf("%s",&b[j]);
        // O
        for(i=0;i<4;i++){
           for(j=0;j<4;j++){
             if(b[i][j]=='T') {
               b[i][j]='O';
               spi=i;
               spj=j;
             }            
           }
        }  
        ////////////
        for(i=0;i<4;i++){
           if(b[i][0]=='O' && b[i][1]=='O' && b[i][2]=='O' && b[i][3]=='O') {
               ans=0;
           }  
        }
        for(i=0;i<4;i++){
           if(b[0][i]=='O' && b[1][i]=='O' && b[2][i]=='O' && b[3][i]=='O') {
               ans=0;
           }  
        }
        if(b[0][0]=='O' && b[1][1]=='O' && b[2][2]=='O' && b[3][3]=='O') {
               ans=0;
        }
        if(b[3][0]=='O' && b[2][1]=='O' && b[1][2]=='O' && b[0][3]=='O') {
               ans=0;
        }
        ////////////////
        b[spi][spj]='X';
        ////////////
        for(i=0;i<4;i++){
           if(b[i][0]=='X' && b[i][1]=='X' && b[i][2]=='X' && b[i][3]=='X') {
               ans=1;
           }  
        }
        for(i=0;i<4;i++){
           if(b[0][i]=='X' && b[1][i]=='X' && b[2][i]=='X' && b[3][i]=='X') {
               ans=1;
           }  
        }
        if(b[0][0]=='X' && b[1][1]=='X' && b[2][2]=='X' && b[3][3]=='X') {
               ans=1;
        }
        if(b[3][0]=='X' && b[2][1]=='X' && b[1][2]=='X' && b[0][3]=='X') {
               ans=1;
        }
        ////////////////
        // .
        for(i=0;i<4;i++){
           for(j=0;j<4;j++){
             if(b[i][j]=='.' && ans==-1) {
               fprintf(bob,"Case #%d: Game has not completed\n",z+1);
               i=8;
               break;
             }
           }
        } 
        if(ans==-1 && i!=9) {
           fprintf(bob,"Case #%d: Draw\n",z+1);
        }
        else if(ans==0) {
           fprintf(bob,"Case #%d: O won\n",z+1);

        }  
        else if(ans==1) {
            fprintf(bob,"Case #%d: X won\n",z+1);

        }              
           

    }
    fclose(bob);
    system("pause");
    return 0;
}
