#include<stdio.h>
char table[4][4];
char fre;

void check(int k)
{
    char first;
    for(int i=0;i<4;i++)
    {
        first=table[i][0];
        if(first=='T') first=table[i][1];
        if(first!='.')
        {
            if(first==table[i][1]||table[i][1]=='T')
            {
                if(first==table[i][2]||table[i][2]=='T')
                {
                    if(first==table[i][3]||table[i][3]=='T')
                    {
                        printf("Case #%d: %c won\n",k,first);
                        return;
                    }
                }
            }
        }
    }

    for(int i=0;i<4;i++)
    {
        first=table[0][i];
        if(first=='T') first=table[1][i];
        if(first!='.')
        {
            if(first==table[1][i]||table[1][i]=='T')
            {
                if(first==table[2][i]||table[2][i]=='T')
                {
                    if(first==table[3][i]||table[3][i]=='T')
                    {
                        printf("Case #%d: %c won\n",k,first);
                        return;
                    }
                }
            }
        }
    }

    first=table[0][0];
    if(first=='T') first=table[1][1];
    if(first!='.')
    {
        if(first==table[1][1]||table[1][1]=='T')
        {
            if(first==table[2][2]||table[2][2]=='T')
            {
                if(first==table[3][3]||table[3][3]=='T')
                {
                    printf("Case #%d: %c won\n",k,first);
                    return;
                }
            }
        }
    }


    first=table[0][3];
    if(first=='T') first=table[1][2];
    if(first!='.')
    {
        if(first==table[1][2]||table[1][2]=='T')
        {
            if(first==table[2][1]||table[2][1]=='T')
            {
                if(first==table[3][0]||table[3][0]=='T')
                {
                    printf("Case #%d: %c won\n",k,first);
                    return;
                }
            }
        }
    }


    for(int i=0;i<4;i++) for(int j=0;j<4;j++)
    {
        if(table[i][j]=='.')
        {
            printf("Case #%d: Game has not completed\n",k);
            return;
        }
    }

    printf("Case #%d: Draw\n",k);
}
int main()
{
    int i,j,k,n,t;
    scanf("%d",&t);
    scanf("%c",&fre);
    for(k=1;k<=t;k++)
    {
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            scanf("%c",&table[i][j]);
            scanf("%c",&fre);
        }
        check(k);
        if(k!=t) scanf("%c",&fre);
    }

    return 0;
}
