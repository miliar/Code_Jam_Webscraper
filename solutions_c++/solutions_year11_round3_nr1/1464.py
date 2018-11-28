#include <stdio.h>


int r, c, t , teste;
char mat[100][100]; 
 
int main()
{
    int i,j;
       
    scanf("%d",&t);
    for(teste=1;teste<=t;teste++){
        scanf("%d %d ",&r,&c);
        
        for(i=0;i<r;i++,getchar()) {    
            for(j=0;j<c;j++){
                mat[i][j] = getchar();
            }
        }

        for(i=0;i<r;i++) for(j=0;j<c;j++){
            if(mat[i][j]=='#'){
                if((i+1>=r)||(j+1>=c))   goto Impossible;
                if(mat[i+1][j]=='.')   goto Impossible;
                if(mat[i][j+1]=='.')   goto Impossible;
                if(mat[i+1][j+1]=='.') goto Impossible;
                
                mat[i][j]    = '/';
                mat[i+1][j]  = '\\';
                mat[i][j+1]  = '\\';
                mat[i+1][j+1]= '/';
            }
        }
        
        printf("Case #%d:\n",teste);
        for(i=0;i<r;i++,printf("\n")) for(j=0;j<c;j++){
            printf("%c",mat[i][j]);
        }
        continue;
        
        Impossible:
        printf("Case #%d:\nImpossible\n",teste);
        
    }
    return 0;
}
