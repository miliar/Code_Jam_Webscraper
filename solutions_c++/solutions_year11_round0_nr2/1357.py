#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int bas[30];
char str[110], cb[50][3], op[30][2], stack[110];
int T, C, D, N, t = 0, top;

int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int i, j ,k;
    
    for ( scanf("%d",&T); T; T-- ) {
        for ( scanf("%d",&C), i = 0; i < C; i++ ) {
            scanf("%s",str);
            cb[i][0] = str[0];
            cb[i][1] = str[1];
            cb[i][2] = str[2];
        }        
        for ( scanf("%d",&D), i = 0; i < D; i++ ) {
            scanf("%s",str);
            op[i][0] = str[0];
            op[i][1] = str[1];
        }
        
        
        
        
        memset(bas,0,sizeof(bas));
        scanf("%d%s",&N,str);
        top = -1;
        
        
        
        for ( i = 0; str[i]; i++ ) {
            stack[++top] = str[i];
            if ( top ) {
                for ( j = 0; j < C; j++ )
                    if ( (cb[j][0]==stack[top]&&cb[j][1]==stack[top-1]) ||
                        (cb[j][1]==stack[top]&&cb[j][0]==stack[top-1]) ) {
                        bas[stack[top-1]-'A']--;
                        stack[--top] = cb[j][2];
                        break;
                    }
            }
                
            if ( stack[top] == 'Q' || stack[top] == 'W' || 
                 stack[top] == 'E' || stack[top] == 'R' || 
                 stack[top] == 'A' || stack[top] == 'S' ||
                 stack[top] == 'D' || stack[top] == 'F' ) {
                
                bas[stack[top]-'A']++;
                for ( j = 0; j < D; j++ )
                    if ( (op[j][0]==stack[top]&&bas[op[j][1]-'A'] ) ||
                        (op[j][1]==stack[top]&&bas[op[j][0]-'A']) ) {
                        top = -1;
                        memset(bas,0,sizeof(bas));
                        break;
                    }
            }
        }
        
        printf("Case #%d: [",++t);
        if ( top < 0 )
            printf("]\n");
        else {
            putchar(stack[0]);
            for ( i = 1; i <= top; i++ )
                printf(", %c",stack[i]);
            printf("]\n");
        }
    }
    
    return 0;
}
