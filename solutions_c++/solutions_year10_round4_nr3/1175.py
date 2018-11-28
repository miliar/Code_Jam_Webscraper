#include<stdio.h>
int main()
{
    freopen("c.txt","r",stdin);
    freopen("cout.txt","w",stdout);
    int test,cas,i,j,x1,x2,y1,y2,n,c1,k;
    bool d1;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        bool arr[103][103]={0},arr1[103][103];
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (j=y1;j<=y2;j++)
            {
                for (k=x1;k<=x2;k++) arr[j][k]=1;
            }
        }
        c1=0;
        while (true)
        {
            for (i=1;i<=100;i++)
            {
                for (j=1;j<=100;j++)
                {
                    if (arr[i][j]&&!((j-1>=0&&arr[i][j-1])||(i-1>=0&&arr[i-1][j]))) arr1[i][j]=0;
                    else if (!arr[i][j]&&((j-1>=0&&arr[i][j-1])&&(i-1>=0&&arr[i-1][j]))) arr1[i][j]=1;
                    else arr1[i][j]=arr[i][j];
                }
            }
            d1=0;
            for (i=1;i<=100;i++)
            {
                for (j=1;j<=100;j++)
                {
                    arr[i][j]=arr1[i][j];
                    if (arr[i][j]) d1=1;
                }
            }
            c1++;
            if (!d1) break;
        }
        printf("Case #%d: %d\n",cas,c1);
    }
    return 0;
}
