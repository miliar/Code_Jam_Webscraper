#include <stdio.h>
#include <string.h>
int main()
{
    int n,r,ans,t,sum;
    bool a[102][102];
    int x[2],y[2];
    
    freopen("D:\\ACM\\Google\\C-small-attempt1.in","r",stdin);
    freopen("D:\\ACM\\Google\\C-small-attempt1.out","w",stdout);
    
    scanf("%d",&t);
    for(int ll=1;ll<=t;ll++)
    {
        scanf("%d",&r);
        memset(a,0,sizeof(a));
        for(int i=0;i<r;i++)
        {
            scanf("%d %d %d %d",&x[0],&y[0],&x[1],&y[1]);
            for(int j=y[0];j<=y[1];j++)
             for(int k=x[0];k<=x[1];k++) a[j][k]=1;
        }
        ans=0;
        int nowx=100,nowy=100;
        int maxx,maxy;
        while(1)
        {           
            sum=0;maxx=nowx;maxy=nowy;
            nowx=0;nowy=0;           
            for(int i=maxx;i>0;i--)
             for(int j=maxy;j>0;j--)
             {                    
                  if (a[i][j])
                  {
                        sum++;
                        if (!(a[i-1][j]||a[i][j-1])) a[i][j]=0;
                        else
                        {
                            if (i>nowx) nowx=i;
                            if (j>nowy) nowy=j;
                        }
                   }
                   else
                   {
                        if ((a[i-1][j]&&a[i][j-1]))
                        {
                             a[i][j]=1;
                             if (i>nowx) nowx=i;
                             if (j>nowy) nowy=j;
                        }
                   }
             }            
            if (sum)  ans++; 
            else break;             
        }
        printf("Case #%d: %d\n",ll,ans);       
    }
    return 0;
}
