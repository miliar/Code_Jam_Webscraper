#include<stdio.h>
int main()
{
    int t,i,j,k,co,cx,ct,cd,w;
    char a[4][5];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        for(i=0;i<4;i++)
        scanf("%s",a[i]);
        w=0;
            co=cx=ct=0;
        for(i=0;i<4;i++)
        {
            co=cx=ct=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='T')
                ct++;
                else if(a[i][j]=='O')
                co++;
                else if(a[i][j]=='X')
                cx++;
            }
            if(co+ct==4)
            {
                w=1;
                printf("Case #%d: O won\n",k);
                break;
            }
            else if(cx+ct==4)
            {
                w=1;
                printf("Case #%d: X won\n",k);
                break;
            }
        }
        if(w)
        continue;
        for(j=0;j<4;j++)
        {
            co=cx=ct=0;
            for(i=0;i<4;i++)
            {
                if(a[i][j]=='T')
                ct++;
                else if(a[i][j]=='O')
                co++;
                else if(a[i][j]=='X')
                cx++;
            }
            if(co+ct==4)
            {
                w=1;
                printf("Case #%d: O won\n",k);
                break;
            }
            else if(cx+ct==4)
            {
                w=1;
                printf("Case #%d: X won\n",k);
                break;
            }
        }
        if(w)
        continue;
            co=cx=ct=0;
        for(i=0;i<4;i++)
        {
            if(a[i][i]=='T')
                ct++;
                else if(a[i][i]=='O')
                co++;
                else if(a[i][i]=='X')
                cx++;
        }
            if(co+ct==4)
            {
                w=1;
                printf("Case #%d: O won\n",k);
            }
            else if(cx+ct==4)
            {
                w=1;
                printf("Case #%d: X won\n",k);
            }
        if(w)
        continue;
            co=cx=ct=0;
        for(i=0;i<4;i++)
        {
            if(a[i][3-i]=='T')
                ct++;
                else if(a[i][3-i]=='O')
                co++;
                else if(a[i][3-i]=='X')
                cx++;
        }
            if(co+ct==4)
            {
                w=1;
                printf("Case #%d: O won\n",k);
            }
            else if(cx+ct==4)
            {
                w=1;
                printf("Case #%d: X won\n",k);
            }
        if(w)
        continue;
        cd=0;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(a[i][j]=='.')
        cd++;
        if(cd)
        printf("Case #%d: Game has not completed\n",k);
        else
        printf("Case #%d: Draw\n",k);
    }
    return 0;
}
