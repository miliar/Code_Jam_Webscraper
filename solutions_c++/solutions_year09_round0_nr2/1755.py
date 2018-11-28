#include <iostream>

using namespace std;
int a[101][101]={0};
int b[101][101]={0};
char c[10005]={'\0'};
int h,w;

int dfs(int x,int y)
{
    int t=a[x][y],x1,y1;
    if(x-1>=0&&a[x-1][y]<t)
    {
        t=a[x-1][y];
        x1=x-1;y1=y;
    }
    if(y-1>=0&&a[x][y-1]<t)
    {
        t=a[x][y-1];
        x1=x;y1=y-1;
    }
    if(y+1<w&&a[x][y+1]<t)
    {
        t=a[x][y+1];
        x1=x;y1=y+1;
    }
    if(x+1<h&&a[x+1][y]<t)
    {
        t=a[x+1][y];
        x1=x+1;y1=y;
    }
    if(t==a[x][y])
        return (x*w+y);
    else
        return dfs(x1,y1);

}
void ans()
{
    int i,j,k;
    for(i=0;i<h;i++)
    {
        for(j=0;j<w;j++)
        {
            b[i][j]=dfs(i,j);
        }
    }
}
int main()
{
//        freopen("in.txt","r",stdin);

    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,k;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        memset(c,'\0',sizeof(c));
        printf("Case #%d:\n",i);
        scanf("%d%d",&h,&w);
        for(j=0;j<h;j++)
        {
            for(k=0;k<w;k++)
            {
                scanf("%d",&a[j][k]);
//                cout<<a[j][k]<<" ";
            }
//            cout<<endl;
        }

        ans();
        char t='a';
        for(j=0;j<h;j++)
        {

            for(k=0;k<w-1;k++)
            {
                if(c[b[j][k]]=='\0')
                {
                    c[b[j][k]]=t;
                    t++;
                }
                printf("%c ",c[b[j][k]]);
  //              printf("%d ",b[j][k]);
            }if(c[b[j][k]]=='\0')
                {
                    c[b[j][k]]=t;
                    t++;
                }
                printf("%c",c[b[j][k]]);
            cout<<endl;
        }
    }
    return 0;
}
