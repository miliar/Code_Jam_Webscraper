#include<stdio.h>
#include<iostream>
using namespace std;
char g[100][100];
int n,K;
void down()
{
    for(int i=0;i<n;i++)
    {
        for(int j=n-1;j>=0;j--)
        {
            if(g[j][i]=='.')
            {
                for(int k=j-1;k>=0;k--)
                {
                    if(g[k][i]!='.')
                    {
                        swap(g[j][i],g[k][i]);
                        break;
                    }
                }
            }
        }
    }
}
int d[8][2]={{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
int r=0,b=0;
void check()
{

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(g[i][j]!='.')
            {
                for(int k=0;k<8;k++)
                {
                    int x=i,y=j;
                    int c=0;
                    while(1)
                    {
                        if(x>=0&&x<n&&y>=0&&y<n&&g[x][y]==g[i][j])
                        {
                            c++;
                        }
                        else break;
                        x+=d[k][0];
                        y+=d[k][1];
                    }
                    if(c>=K)
                    {
                        if(g[i][j]=='R')r=1;
                        else b=1;
                    }
                }
            }
        }
    }
}
void rotate()
{
    int tem[100][100];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            tem[j][n-1-i]=g[i][j];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        g[i][j]=tem[i][j];
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int ca=0;
    while(T--)
    {
        printf("Case #%d: ",++ca);
        scanf("%d%d",&n,&K);
        for(int i=0;i<n;i++)
        {
            cin>>g[i];
        }
        r=0;b=0;
        rotate();
        down();
        check();
        if(r&&b)
        {
            printf("Both\n");
        }
        else if(r)
        {
            printf("Red\n");
        }
        else if(b)
        {
            printf("Blue\n");
        }
        else
        {
            printf("Neither\n");
        }
    }
}
