#include <stdio.h>
#include <string.h>
char map[5][5];
char mapT[5][5];
int tx,ty,flag=0;

void trans()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
             mapT[j][i]=map[i][j];
             if(map[i][j] =='T')
             {
                    tx=i;
                    ty=j;
             }
             if(map[i][j] =='.')
                flag=1;
        }


}

int whoWin()
{
        int n=2;
        char vec[2][5]={"OOOO","XXXX"};
        while(n--)
        {
             if(tx!=-1)
             {
                 if(n==1)
                 {
                     map[tx][ty]='X';
                     mapT[ty][tx]='X';
                 }
                 else
                 {
                     map[tx][ty]='O';
                     mapT[ty][tx]='O';
                 }
             }
             for(int i=0;i<4;i++)
             {
                if( strcmp(map[i],vec[n])==0 || strcmp(mapT[i],vec[n])==0 )
                {
                    if(n==1)
                        return 1;
                    else
                        return -1;
                }
            }
            if(map[0][0]==map[1][1] && map[1][1]==map[2][2] && map[2][2]==map[3][3])
            {
                if(map[0][0] == 'X')
                    return 1;
                else if(map[0][0] == 'O')
                    return -1;
            }
            if(map[0][3]==map[1][2] && map[1][2]==map[2][1] && map[2][1]==map[3][0])
            {
                if(map[0][3] == 'X')
                    return 1;
                else if(map[0][3] == 'O')
                    return -1;
            }
        }
        return 0;

}



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,t;

    scanf("%d",&T);
    t=T;
    while(T--)
    {
        tx=-1;
        ty=-1;
        flag=0;
        for(int i=0;i<4;i++)
        {
            scanf("%s",map[i]);
        }

        trans();
        getchar();
        getchar();
        int x=whoWin();
        if(x==1)
            printf("Case #%d: X won\n",t-T);
        else if(x==-1)
            printf("Case #%d: O won\n",t-T);
        else if(x==0 && flag==0)
             printf("Case #%d: Draw\n",t-T);
        else if(x==0 && flag==1)
             printf("Case #%d: Game has not completed\n",t-T);
    }
    return 0;
}
