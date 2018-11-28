#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int CAS;
int r,c;
char map[60][60];
char s[60];
int main()
{
    bool f;
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas<=CAS;cas++)
    {
        for(int i = 0;i < 60;i++)
            for(int j = 0;j < 60;j++)
                map[i][j] = '-';
        scanf("%d%d",&r,&c);
        for(int i = 0;i < r;i++)
        {
            scanf("%s",map[i]);
            //for(int j = 1;j <= c;j++)
            //     map[i][j] = s[j-1];
        }
        for(int i = 0;i < r;i++)
            for(int j = 0;j < c;j++)
            {
                if(i+1 < r && j+1 < c)
                    if(map[i][j] == '#' && map[i+1][j+1] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#')
                    {
                        map[i][j] = '/';
                        map[i][j+1] = '\\';
                        map[i+1][j] = '\\';
                        map[i+1][j+1]= '/';
                    }
            }
        f = true;
        for(int i = 0;i < r;i++)
            for(int j = 0;j < c;j++)
                if(map[i][j] == '#')
                    f = false;
        printf("Case #%d:\n",cas);
        if(f==true)
        {
            for(int i = 0;i < r;i++)
            {
                for(int j = 0;j < c;j++)
                    printf("%c",map[i][j]);
                printf("\n");
            }
        }
        else printf("Impossible\n");
    }
    fclose(stdin);
    fclose(stdout);
}
