#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;

int main(int argc, char *argv[]) {
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        char str[4][5];
        for(int j=0;j<4;j++)
        {
            scanf("%s",str[j]);
        }
        
        char winner = ' ';
        for(int j=0;j<4;j++)
        {
            char now = str[j][0];
            if(now=='T')now = str[j][1];
            for(int k=0;k<4;k++)
            {
                if(str[j][k]=='.')break;
                if(str[j][k]!='T' && str[j][k]!=now)
                {
                    break;
                }
                if(k==3)
                {
                    winner = now;
                }
            }
            now = str[0][j];
            if(now=='T')now = str[1][j];
            for(int k=0;k<4;k++)
            {
                if(str[k][j]=='.')break;
                if(str[k][j]!='T' && str[k][j]!=now)
                {
                    break;
                }
                if(k==3)
                {
                    winner = now;
                }
            }
        }
        char now = str[0][0];
        if(now=='T')now = str[1][1];
        for(int j=0;j<4;j++)
        {
            if(str[j][j]=='.')break;
            if(str[j][j]!='T' && str[j][j]!=now)
            {
                break;
            }
            if(j==3)
            {
                winner = now;
            }
        }
        now = str[3][0];
        if(now=='T')now = str[2][1];
        for(int j=0;j<4;j++)
        {
            if(str[3-j][j]=='.')break;
            if(str[3-j][j]!='T' && str[3-j][j]!=now)
            {
                break;
            }
            if(j==3)
            {
                winner = now;
            }
        }
        if(winner==' ')
        {
            bool draw = 1;
            for(int j=0;j<4;j++)
            {
                for(int k=0;k<4;k++)
                {
                    if(str[j][k]=='.')draw = 0;
                }
            }
            if(draw)printf("Case #%d: Draw\n",i+1);
            else printf("Case #%d: Game has not completed\n",i+1);
        }
        else printf("Case #%d: %c won\n",i+1,winner);
    }
}