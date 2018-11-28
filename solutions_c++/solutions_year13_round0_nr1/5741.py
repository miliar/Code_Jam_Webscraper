#include<stdio.h>
#include<memory.h>

char g_board[4][4];

int main()
{
   // freopen("e.out", "w", stdout);
    int i,j=1,row,col,t,a[15];
    char ch;
    scanf("%d",&t);
    while(t--){
    memset(a,0,sizeof(a));
    for(row=-1;row<4;row++)
    {
        col=0;
        while((ch=getchar())!='\n')
        {
            g_board[row][col++]=ch;
            a[row]+=g_board[row][col-1];
            a[col-1+4]+=g_board[row][col-1];
            if(row==col-1)
            a[8]+=g_board[row][col-1];
            if(row+col-1==3)
            a[9]+=g_board[row][col-1];
        }

    }
    for(i=0;i<10;i++){
        if(a[i]==348||a[i]==352){
            printf("Case #%d: X won\n",j++);break;
        }
        else if(a[i]==321||a[i]==316){
            printf("Case #%d: O won\n",j++);break;
        }
        else if(i==9)
        {
            if(a[2]<=283||a[3]<=283||a[1]<=283||a[0]<=283)
               printf("Case #%d: Game has not completed\n",j++);
            else
               printf("Case #%d: Draw\n",j++);
        }
    }
    }
    return 0;
}

