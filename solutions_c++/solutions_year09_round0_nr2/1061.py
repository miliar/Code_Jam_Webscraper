#include <iostream>
#include <string.h>
using namespace std;

int h,w;
int grid[120][120];
char mark[120][120];
char tmark,m;
int dirx[4]={-1,0,0,1};
int diry[4]={0,-1,1,0};

bool in(int i, int j)
{
        if(i>=0&&i<h&&j>=0&&j<w)
                return 1;
        else
                return 0;
}

void print()
{
        for(int i=0;i<h;i++)
        {
                for(int j=0;j<w;j++)
                        cout<<mark[i][j]<<" ";
                cout<<endl;
        }
}

void search(int x , int y)
{
        int tx,ty;
        int cx=x,cy=y;
        int i;
        int min=12000;
        for(i=0;i<4;i++)
        {
                tx=x+dirx[i];
                ty=y+diry[i];
                if(in(tx,ty))
                {
                        if(grid[tx][ty]<grid[x][y]&&grid[tx][ty]<min)
                        {
                                min=grid[tx][ty];
                                cx=tx;
                                cy=ty;
                        }
                }
        }
        if(cx!=x||cy!=y)
        {
                search(cx,cy);
                mark[cx][cy]=tmark;
        }
        else
        {

                if(mark[cx][cy]=='0')
                {
                        mark[cx][cy]=m;
                        tmark=m;
                        m++;
                }
                else
                        tmark=mark[cx][cy];
        }
}

int main()
{
//        freopen("B-small-attempt1.in","r",stdin);
//        freopen("B-small-attempt1.out","w",stdout);

       freopen("B-large.in","r",stdin);
        freopen("B-large.out","w",stdout);
        int T;
        int i,j;
        cin>>T;
        for(int cases=1; cases<=T;cases++)
        {
                memset(grid, 0 , sizeof(grid));
                memset(mark,'0',sizeof(mark));

                cin>>h>>w;
                for(i=0;i<h;i++)
                        for(j=0;j<w;j++)
                                cin>>grid[i][j];

                m='a';
                for(i=0;i<h;i++)
                {
                        for(j=0;j<w;j++)
                        {
                                if(mark[i][j]=='0')
                                {
                                        search(i,j);
                                        mark[i][j]=tmark;
                                }
                        }
                }
                printf("Case #%d: \n",cases);
                print();
        }
        return 0;
}
