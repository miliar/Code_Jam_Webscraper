#include <stdio.h>
#include <iostream>
#include <string>

char table[4][4];

int won(char x){

    int p;
    for (int i=0;i<4;i++)
    {
        p=0;
        for (int j=0;j<4;j++)
            p+= (table[i][j] == x) + (table[i][j] == 'T');
        if ( p >= 4 ) return 1;
    }

    for (int j=0;j<4;j++)
    {
        p=0;
        for (int i=0;i<4;i++)
            p+= (table[i][j] == x) + (table[i][j] == 'T');
        if ( p >= 4 ) return 1;
    }

    p = 0;
    for (int i=0;i<4;i++)
        p+= (table[i][i] == x) + (table[i][i] == 'T');
    if ( p>= 4 ) return 1;

    p = 0;
    for (int i=0;i<4;i++)
        p+= (table[i][4-i-1] == x) + (table[i][4-i-1] == 'T');
    if ( p>= 4 ) return 1;

    return 0;
}


int main(){
    int t;
    scanf("%d\n",&t);
    for (int l=1;l<=t;l++)
    {
        for (int j=0;j<4;j++)
            scanf("%s",table[j]);
        
        int flag =1 ;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                flag = flag & ( table[i][j] != '.' );

        int xwin = won('X');
        int owin = won('O');
        if ( xwin ) 
           printf("Case #%d: X won\n",l);
        else if ( owin )
           printf("Case #%d: O won\n",l);
        else if ( flag )
          printf("Case #%d: Draw\n",l);
        else 
          printf("Case #%d: Game has not completed\n",l);

    }
    return 0;
}
