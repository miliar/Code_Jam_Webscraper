#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
char map[6][6];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cases,id=1;
    scanf("%d",&cases);
    while(cases--)
    {
        printf("Case #%d: ",id++);
        for(int i=0;i<4;i++)
            scanf("%s",map[i]);
        int ans=0;
        for(int i=0;i<4;i++)
        {
            int numx=0,numo=0;
            for(int j=0;j<4;j++)
            {
                if(map[i][j]=='X'||map[i][j]=='T')
                    numx++;
                if(map[i][j]=='O'||map[i][j]=='T')
                    numo++;
            }
            if(numx==4)
            {
                ans=1;
                break;
            }
            else if(numo==4)
            {
                ans=2;
                break;
            }
        }
        for(int i=0;ans==0&&i<4;i++)
        {
            int numx=0,numo=0;
            for(int j=0;j<4;j++)
            {
                if(map[j][i]=='X'||map[j][i]=='T')
                    numx++;
                if(map[j][i]=='O'||map[j][i]=='T')
                    numo++;
            }
            if(numx==4)
            {
                ans=1;
                break;
            }
            else if(numo==4)
            {
                ans=2;
                break;
            }
        }
        int numx=0,numo=0;
        for(int i=0;ans==0&&i<4;i++)
        {
            if(map[i][i]=='X'||map[i][i]=='T')
                numx++;
            if(map[i][i]=='O'||map[i][i]=='T')
                numo++;
        }
        if(numx==4)
        {
            ans=1;
        }
        else if(numo==4)
        {
            ans=2;
        }
        numx=0,numo=0;
        for(int i=0;ans==0&&i<4;i++)
        {
            if(map[i][3-i]=='X'||map[i][3-i]=='T')
                numx++;
            if(map[i][3-i]=='O'||map[i][3-i]=='T')
                numo++;
        }
        if(numx==4)
        {
            ans=1;
        }
        else if(numo==4)
        {
            ans=2;
        }
        if(ans==1)
        {
            printf("X won\n");
        }
        else if(ans==2)
        {
            printf("O won\n");
        }
        else
        {
            int f=0;
            for(int i=0;f==0&&i<4;i++)
                for(int j=0;f==0&&j<4;j++)
                    if(map[i][j]=='.')
                        f=1;
            if(f==1)
            {
                printf("Game has not completed\n");
            }
            else
            {
                printf("Draw\n");
            }
        }
    }
    return 0;
}
