#include <iostream>
using namespace std;

//N W E S
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int g[100][100],father[10000],h,w,cx,cy;
char ret[100][100],cur;

bool inrange(int x,int y)
{
    return x>=0&&x<h&&y>=0&&y<w;   
}

int findfather(int x)
{
    if (father[x]==x)   return x;
    father[x]=findfather(father[x]);
    return father[x];   
}

main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for (int i=0;i<t;i++)
    {
        printf("Case #%d:\n",i+1);
        cin>>h>>w;
        for (int x=0;x<h;x++)
            for (int y=0;y<w;y++)
            {
                cin>>g[x][y];
                father[x*w+y]=x*w+y;   
                ret[x][y]=' ';
            }
        for (int x=0;x<h;x++)
            for (int y=0;y<w;y++)
            {
                cx=x;cy=y;
                for (int d=0;d<4;d++)
                    if (inrange(x+dx[d],y+dy[d])&&g[x+dx[d]][y+dy[d]]<g[cx][cy])
                        cx=x+dx[d],cy=y+dy[d];
                if (!(cx==x&&cy==y))    father[findfather(x*w+y)]=cx*w+cy;
            }
        cur='a';
        for (int x=0;x<h;x++)
        {
            for (int y=0;y<w;y++)
            {
                int p=findfather(x*w+y);
                if (ret[p/w][p%w]==' ')
                    ret[p/w][p%w]=cur++;
                ret[x][y]=ret[p/w][p%w];
                cout<<ret[x][y];
                if (y<w-1)  cout<<" ";   
            }
            cout<<endl;   
        }
    }   
}
