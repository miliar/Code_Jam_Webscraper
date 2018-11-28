#include<stdio.h>
#include<string.h>

int main()
{
    int i,j,t,co=1,x,o,ans,fill;
    char s[10][10],w[10];
    scanf("%d",&t);
    gets(s[0]);
    while(t--)
    {
        ans=fill=0;
        for(i=0;i<4;i++)
            gets(s[i]);
        gets(w);
        x=o=0;
        for(i=0;i<4;i++)
        {
            x=o=0;
            for(j=0;j<4;j++)
            {
                if(s[i][j]=='X' || s[i][j]=='T')
                    x++;
                if(s[i][j]=='O' || s[i][j]=='T')
                    o++;
                if(s[i][j]=='.')
                    fill=1;
            }
            if(x==4)
            {
                ans=1;
                break;
            }
            if(o==4)
            {
                ans=2;
                break;
            }
        }
        if(!ans)
        {
            x=o=0;
            for(i=0;i<4;i++)
            {
                x=o=0;
                for(j=0;j<4;j++)
                {
                    if(s[j][i]=='X' || s[j][i]=='T')
                        x++;
                    if(s[j][i]=='O' || s[j][i]=='T')
                        o++;
                }
                if(x==4)
                {
                    ans=1;
                    break;
                }
                if(o==4)
                {
                    ans=2;
                    break;
                }
            }
        }
        if(!ans)
        {
            x=o=0;
            for(i=0,j=0;i<4;i++,j++)
            {
                if(s[i][j]=='X' || s[i][j]=='T')
                    x++;
                if(s[i][j]=='O' || s[i][j]=='T')
                    o++;
            }
            if(x==4)
                ans=1;
            if(o==4)
                ans=2;
        }
        if(!ans)
        {
            x=o=0;
            for(i=0,j=3;i<4;i++,j--)
            {
                if(s[i][j]=='X' || s[i][j]=='T')
                    x++;
                if(s[i][j]=='O' || s[i][j]=='T')
                    o++;
            }
            if(x==4)
                ans=1;
            if(o==4)
                ans=2;
        }
        printf("Case #%d: ",co++);
        if(ans==1)
            printf("X won\n");
        else if(ans==2)
            printf("O won\n");
        else
        {
            if(!fill)
                printf("Draw\n");
            else
                printf("Game has not completed\n");
        }
    }
    return 0;
}
