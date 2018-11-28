#include <stdio.h>
int main()
{
    int T;
    char board[4][4];
    char eline;
    scanf("%d",&T);

    for(int i=1;i<=T;i++){
        scanf("%s",board[0]);
        scanf("%s",board[1]);
        scanf("%s",board[2]);
        scanf("%s",board[3]);
        scanf("%c",&eline);

        bool isblank = false;
        int a[10];

        for(int j=0;j<10;j++)
            a[j]=0;

        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                int p;

                if(board[j][k]=='O')
                    p = 10;
                else if(board[j][k]=='X')
                    p=1;
                else if(board[j][k]=='T')
                    p=0;
                else {
                    p=-40;
                    isblank = true;
                }

                if(j==k){
                    a[0] += p;
                }
                if(j+k==3){
                    a[1] += p;
                }

                a[k+2] += p;
                a[j+6] += p;
            }
        }

        char w = 'N';
        for(int j=0;j<10;j++){
            if(a[j]==3 || a[j] == 4){
                w='X';
                break;
            }
            if(a[j]==30 || a[j] == 40){
                w='O';
                break;
            }
        }

        switch(w){
            case 'X':
            case 'O':
                printf("Case #%d: %c won\n",i,w);
                break;
            case 'N':
                if(isblank)
                    printf("Case #%d: Game has not completed\n",i);
                else
                    printf("Case #%d: Draw\n",i);
                break;
        }
    }
}
