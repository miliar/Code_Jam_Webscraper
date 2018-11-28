#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
char a[100][100];
int main()
{
    int i,j,k,t,T;
    scanf("%d",&T);
    int n,m;
    for(t=1;t<=T;t++)
    {
        scanf("%d %d\n",&n,&m);
        for(i=0;i<n;i++)
        {
                scanf("%s",a[i]);
                //printf("%s\n",a[i]);
        }
        bool possible=true;
        for(i=0;i<n && possible;i++)
            for(j=0;j<m && possible;j++)
            {
                if(a[i][j]=='#')
                {
                    a[i][j]='/';
                    if( (i+1)<n && a[i+1][j]=='#')
                        a[i+1][j]='\\';
                    else
                    {
                        //printf("here1 %d %d\n",i,j);
                        possible=false;
                        break;
                    }
                    if( (i+1)<n && (j+1) <m && a[i+1][j+1]=='#')
                        a[i+1][j+1]='/';
                    else
                    {
                        possible=false;
                        //printf("here2 %d %d\n",i,j);
                        break;
                    }
                    if( (j+1)<m && a[i][j+1]=='#')
                        a[i][j+1]='\\';
                    else
                    {
                        possible=false;
                        //printf("here3 %d %d\n",i,j);
                        break;
                    }
                }
            }
        printf("Case #%d: \n",t);
        if(possible)
        {
            for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                    printf("%c",a[i][j]);
                printf("\n");
            }
        }
        else
            printf("Impossible\n");
    }
    return 0;
}
