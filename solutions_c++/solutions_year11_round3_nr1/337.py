#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
using namespace std;

char mas[128][128];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    int r,c;
    scanf("%d",&cases);
    char in;
    bool broke;
    for(int ic=1;ic<cases+1;ic++)
    {
        broke=false;
        scanf("%d%d",&r,&c);
        scanf("%c",&in);
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                scanf("%c",&mas[i][j]);
            }
            scanf("%c",&in);
        }

        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(mas[i][j]=='#')
                {
                    if(i<r-1)
                    {
                        if(j<c-1&&mas[i][j]=='#'&&
                               mas[i][j+1]=='#'&&
                               mas[i+1][j]=='#'&&
                               mas[i+1][j+1]=='#'){
                            mas[i][j]='/';
                            mas[i][j+1]='\\';
                            mas[i+1][j]='\\';
                            mas[i+1][j+1]='/';
                        }
                        else{
                            broke=true;
                            break;
                        }
                    }
                    else
                    {
                        broke=true;
                        break;
                    }
                }
            }
            if(broke)break;
        }
        printf("Case #%d:\n",ic);
        if(broke)
        {
            printf("Impossible\n");
        }
        else
        {
            for(int i=0;i<r;i++)
            {
                for(int j=0;j<c;j++)
                {
                    printf("%c",mas[i][j]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}
