#include<stdio.h>
#include<string.h>
char tile[55][55],ans[55][55];
int flag[55][55];
int main()
{
    int kcase=0,i,j,cnt,t,n,m,f;
    freopen("A-large.in","r",stdin);
    freopen("tile.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        kcase++;
        memset(flag,0,sizeof(flag));
        scanf("%d%d",&n,&m);
        cnt=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf(" %c",&tile[i][j]);
                if(tile[i][j]=='#')
                    cnt++;
            }
        }
        printf("Case #%d:\n",kcase);
//        for(i=0;i<n;i++)
//        {
//            for(j=0;j<m;j++)
//                printf("%c",tile[i][j]);
//            printf("\n");
//
//        }
//        printf("\n");
        if(cnt%4!=0)
        {
            printf("Impossible\n");
            continue;
        }
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                ans[i][j]='.';

                f=0;
        for(i=0;i<n-1;i++)
        {
            for(j=0;j<m-1;j++)
            {
                if(tile[i][j]=='#'&&flag[i][j]==0)
                {
                    if(flag[i][j+1]==0&&flag[i+1][j]==0&&flag[i+1][j+1]==0)
                    {
                        if(tile[i][j+1]!='#'||tile[i+1][j]!='#'||tile[i+1][j+1]!='#')
                        {
                            f=1;
                            break;
                        }
                        ans[i][j]='/';
                        ans[i][j+1]='\\';
                        ans[i+1][j]='\\';
                        ans[i+1][j+1]='/';


                        flag[i][j]=1;
                        flag[i][j+1]=1;
                        flag[i+1][j]=1;
                        flag[i+1][j+1]=1;
                    }
                }
            }
            if(f==1)    break;
        }

        if(f==1)
         {
            printf("Impossible\n");
            continue;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
                printf("%c",ans[i][j]);
            printf("\n");
        }
    }
    return 0;
}





