#include <stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,T;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        char str[5][5];
        int winner=-1;
        int i,j;
        for(i=0;i<4;i++) scanf("%s",str[i]);
        for(i=0;i<4;i++)
        {
            int cnt[3] = {0};
            for(j=0;j<4;j++)
            {
                switch(str[i][j])
                {
                case 'O':
                    cnt[0]++;
                    break;
                case 'X':
                    cnt[1]++;
                    break;
                case 'T':
                    cnt[2]++;
                    break;
                }
            }
            if(cnt[0]+cnt[2]==4) winner = 0;
            else if(cnt[1]+cnt[2]==4) winner = 1;
        }
        for(i=0;i<4;i++)
        {
            int cnt[3] = {0};
            for(j=0;j<4;j++)
            {
                switch(str[j][i])
                {
                case 'O':
                    cnt[0]++;
                    break;
                case 'X':
                    cnt[1]++;
                    break;
                case 'T':
                    cnt[2]++;
                    break;
                }
            }
            if(cnt[0]+cnt[2]==4) winner = 0;
            else if(cnt[1]+cnt[2]==4) winner = 1;
        }
        if(winner==-1)
        {
            int cnt[3] = {0};
            for(j=0;j<4;j++)
            {
                switch(str[j][j])
                {
                case 'O':
                    cnt[0]++;
                    break;
                case 'X':
                    cnt[1]++;
                    break;
                case 'T':
                    cnt[2]++;
                    break;
                }
            }
            if(cnt[0]+cnt[2]==4) winner = 0;
            else if(cnt[1]+cnt[2]==4) winner = 1;

            cnt[0] = cnt[1] = cnt[2] = 0;
            for(j=0;j<4;j++)
            {
                switch(str[j][3-j])
                {
                case 'O':
                    cnt[0]++;
                    break;
                case 'X':
                    cnt[1]++;
                    break;
                case 'T':
                    cnt[2]++;
                    break;
                }
            }
            if(cnt[0]+cnt[2]==4) winner = 0;
            else if(cnt[1]+cnt[2]==4) winner = 1;
        }
        if(winner == -1)
        {
            bool chk=0;
            for(i=0;i<4;i++)
                for(j=0;j<4;j++)
                if(str[i][j] == '.') chk = 1;
            if(!chk) winner = 3;
        }
        printf("Case #%d: ",t);
        if(winner==-1) printf("Game has not completed\n");
        else if(winner == 0) printf("O won\n");
        else if(winner == 1) printf("X won\n");
        else printf("Draw\n");
    }
}
