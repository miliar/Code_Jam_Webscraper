#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define max(a,b)    a>b?a:b;
#define INF 0x3fffffff
#define eps 1e-6
int min(int a,int b)
{
    return a<b?a:b;
}
int check(double a,double b)
{
    if(a>-eps&&b>-eps&&a<eps&&b<eps)    return 1;
    else                                return 0;
}
int map[15][15];
char str[15];
int main()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,n,r,c,d;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d%d%d",&r,&c,&d);
        for(int i=1;i<=r;i++)
        {
            scanf("%s",&str[1]);
            for(int j=1;j<=c;j++)
            {
                map[i][j]=str[j]-'0'+d;
            }
        }
        int mark=0,ans;
        for(ans=min(r,c);ans>=3;ans--)
        {
            for(int i=1;i<=r;i++)
            {
                for(int j=1;j<=c;j++)
                {
                    if(i+ans-1<=r&&j+ans-1<=c)
                    {
                        double xsum=0,ysum=0,sum=0;
                        for(int x=i;x<=i+ans-1;x++)
                        {
                            for(int y=j;y<=j+ans-1;y++)
                            {
                                sum+=map[x][y];
                                xsum+=x*map[x][y];
                                ysum+=y*map[x][y];
                            }
                        }
                        sum=sum-map[i][j]-map[i][j+ans-1]-map[i+ans-1][j]-map[i+ans-1][j+ans-1];
                        xsum=xsum-i*map[i][j]-i*map[i][j+ans-1]-(i+ans-1)*map[i+ans-1][j]-(i+ans-1)*map[i+ans-1][j+ans-1];
                        ysum=ysum-j*map[i][j]-(j+ans-1)*map[i][j+ans-1]-j*map[i+ans-1][j]-(j+ans-1)*map[i+ans-1][j+ans-1];
                        if(check(xsum*1.0/sum-(2*i+ans-1)*1.0/2,ysum*1.0/sum-(2*j+ans-1)*1.0/2))
                        {
                            mark=1;
                            break;
                        }
                    }
                }
                if(mark)    break;
            }
            if(mark)    break;
        }
        printf("Case #%d: ",cas);
        if(mark)    printf("%d\n",ans);
        else        printf("IMPOSSIBLE\n");
    }
    return 0;
}
