#include<iostream>
int a[110][110],b[110][110];
int countcell()
{
    int countt=0;
    int i,j;
    for(i=0;i<100;i++)
    {
        for(j=0;j<100;j++)
        countt+=a[i][j];
        }
    return countt;
    }
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    int t,r;
    int x1,x2,y1,y2;
    int x,ii,i,j;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
        scanf("%d",&r);
        for(ii=0;ii<r;ii++)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            x1--;
            y1--;
            x2--;
            y2--;
            for(i=x1;i<=x2;i++)
            {
                for(j=y1;j<=y2;j++)
                a[i][j]=1;
                }
            }
        
        int countt=0;
        for(;;)
        {
            /*for(i=0;i<10;i++)
            {
                for(j=0;j<10;j++)
                printf("%d ",a[i][j]);
                printf("\n");
                }
            printf("%d\n\n",countcell());
            system("pause");*/
            
            if(countcell()==0)
            break;
            
            countt++;
            for(i=0;i<100;i++)
            {
                for(j=0;j<100;j++)
                b[i][j]=a[i][j];
                }
            
            for(j=0;j<100;j++)
            a[0][j]=0;
            for(i=0;i<100;i++)
            a[i][0]=0;
            for(i=1;i<100;i++)
            {
                for(j=1;j<100;j++)
                {
                    if(a[i][j]==0)
                    {
                        if(b[i-1][j]&&b[i][j-1])
                        a[i][j]=1;
                        }
                    else
                    {
                        if(!b[i-1][j]&&!b[i][j-1])
                        a[i][j]=0;
                        }
                    }
                }
            }
            
        printf("Case #%d: %d\n",x+1,countt);
        }
    scanf(" ");
    return 0;
    }
