#include<stdio.h>
char map[100][100];

int main()
{
    freopen("in.in","r",stdin);
    freopen("result.out","w",stdout);
    int t, r, c;
    int fault = 0;
    scanf("%d", &t);
    for(int tcase=1 ; tcase <= t; tcase++)
    {
        scanf("%d%d", &r, &c);
        for(int i=0; i<r ;i++)
            scanf("%s", map[i]);
        printf("Case #%d:\n", tcase);

        int cblue=0;
        for(int i=0; i<r ; i++)
            for(int j=0; j<c ; j++)
                if(map[i][j]=='#')
                    cblue++;
        if(cblue%4 != 0)
        {
            printf("Impossible\n");
            continue;
        }
        else
        {
            fault = 0;
            for(int i=0; i<r ; i++)
            {
                if(!fault)
                    for(int j=0; j<c ; j++)
                    {
                        if(map[i][j]=='#')
                        {
                            if(map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#')
                            {
                                map[i][j] = '/';
                                map[i][j+1] = '\\';
                                map[i+1][j] = '\\';
                                map[i+1][j+1] = '/';
                            }
                            else
                            {
                                fault =1;
                                break;
                            }
                        }
                    }
                else
                    break;
            }
            if(!fault)
                for(int i=0; i<r ; i++)
                    printf("%s\n", map[i]);
            else
                printf("Impossible\n");
        }
    }
    fclose(stdout);
    return 0;
}
