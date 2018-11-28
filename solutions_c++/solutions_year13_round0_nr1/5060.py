#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        char bd[5][5];
        for(int i=0;i<4;i++)
        {
            scanf("%s",bd[i]);
        }
        int ans=3;
        for(int i=0;i<4;i++)
        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[i][j]=='X'||bd[i][j]=='T')
                    x++;
            if(x==4) ans=1;
        }

        for(int i=0;i<4;i++)
        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][i]=='X'||bd[j][i]=='T')
                    x++;
            if(x==4) ans=1;
        }

        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][j]=='X'||bd[j][j]=='T')
                    x++;
            if(x==4) ans=1;
        }

        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][3-j]=='X'||bd[j][3-j]=='T')
                    x++;
            if(x==4) ans=1;
        }

        for(int i=0;i<4;i++)
        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[i][j]=='O'||bd[i][j]=='T')
                    x++;
            if(x==4) ans=2;
        }

        for(int i=0;i<4;i++)
        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][i]=='O'||bd[j][i]=='T')
                    x++;
            if(x==4) ans=2;
        }

        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][j]=='O'||bd[j][j]=='T')
                    x++;
            if(x==4) ans=2;
        }

        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[j][3-j]=='O'||bd[j][3-j]=='T')
                    x++;
            if(x==4) ans=2;
        }
        if(ans!=1&&ans!=2)
        for(int i=0;i<4;i++)
        {
            int x=0;
            for(int j=0;j<4;j++)
                if(bd[i][j]=='.')
                    x++;
            if(x) ans=4;
        }

        if(ans==1)
            printf("Case #%d: X won\n",c);
        if(ans==2)
            printf("Case #%d: O won\n",c);
        if(ans==4)
            printf("Case #%d: Game has not completed\n",c);
        if(ans==3)
            printf("Case #%d: Draw\n",c);

    }
    return 0;
}
