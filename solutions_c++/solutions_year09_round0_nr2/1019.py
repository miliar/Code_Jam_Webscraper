#include<iostream>
#include<cstdio>
using namespace std;
int mp[105][105];
char ans[105][105];
char cnt;
int e[4]={-1,0,0,1};
int f[4]={0,-1,1,0};
int h,w;

char dfs(int i,int j)
{
    if(ans[i][j]==' ')
    {
        int ch[4],k,x,y;
        for(k=0;k<4;k++)
        {
            x=i+e[k];
            y=j+f[k];
            if(x>=0&&x<h&&y>=0&&y<w)
                ch[k]=mp[x][y];
            else
                ch[k]=0x7fffffff;
        }
        int minn=0x7fffffff,tmp;
        for(k=0;k<4;k++)
            if(minn>ch[k])
            {
                minn=ch[k];
                tmp=k;
            }
        if(minn>=mp[i][j])
            ans[i][j]=char(cnt++);
        else
            ans[i][j]=dfs(i+e[tmp],j+f[tmp]);
    }
    return ans[i][j];
}

int main()
{
    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );
    
    int t,T,i,j;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d",&h,&w);
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
            {
                scanf("%d",&mp[i][j]);
                ans[i][j]=' ';
            }
        cnt='a';
        char tmp;
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
                tmp=dfs(i,j);
//        char tmp = dfs(0,0);
        printf("Case #%d:\n",t);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
                printf("%c ",ans[i][j]);
            printf("\n");
        }
    }
    return 0;
}
