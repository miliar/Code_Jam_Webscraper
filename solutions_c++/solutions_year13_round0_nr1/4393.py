#include<stdio.h>
int main()
{
    int t,state,i,j,X_win,O_win,count,K=1,S;
    char s[5][5];
    scanf("%d",&t);
    while(t--)
    {
            printf("Case #%d: ",K);
            K++;
            state=1,X_win=0,O_win=0;
            for(i=0;i<4;i++)
                    scanf("%s",s[i]);
            count=0;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(s[i][j]=='.')
                        count++;
                }
            }
            if(count>0)
                state=0;
            //horizontally//
            for(i=0;i<4;i++)
            {
                S=0;
                for(j=0;j<4;j++)
                {
                      S+=s[i][j];
                }
                if(S==348||S==352){
                    X_win=1;
                    goto last;
                }
                if(S==321||S==316)
                {
                    O_win=1;
                    goto last;
                }
            }
            //vertically//
            for(i=0;i<4;i++)
            {
                S=0;
                for(j=0;j<4;j++)
                {
                    S+=s[j][i];
                }
                if(S==348||S==352){
                    X_win=1;
                    goto last;
                }
                if(S==321||S==316)
                {
                    O_win=1;
                    goto last;
                }
            }
            S=0;
            //diagonally//
            S=s[0][0]+s[1][1]+s[2][2]+s[3][3];
            if(S==348||S==352)
                X_win=1;
            if(S==321||S==316)
                O_win=1;
            S=0;
            S=s[3][0]+s[2][1]+s[1][2]+s[0][3];
             if(S==348||S==352)
                X_win=1;
            if(S==321||S==316)
                O_win=1;
            last:
            if(state)
            {
                if(X_win)
                    printf("X won\n");
                else if(O_win)
                    printf("O won\n");
                else
                    printf("Draw\n");
            }
            else
            {
                if(X_win)
                    printf("X won\n");
                else if(O_win)
                    printf("O won\n");
                else
                    printf("Game has not completed\n");
            }
    }
    return 0;
}
