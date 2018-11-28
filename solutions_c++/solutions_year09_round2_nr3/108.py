#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

const int maxrange=600;
const int delta=300;

bool inrange(int x,int y,int w)
{
    return x>=0&&x<w&&y>=0&&y<w;
}

string f[2][10][10][maxrange];

main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int task;
    cin>>task;
    for (int t=1;t<=task;t++)
    {
        int w,q;
        char g[10][10];    
        cin>>w>>q;
        for (int i=0;i<w;i++)
        {
            for (int j=0;j<w;j++)   
                cin>>g[i][j];
            scanf("\n");
        }
        /*
        for (int i=0;i<w;i++)
        {
            for (int j=0;j<w;j++)
                cout<<g[i][j];
            cout<<endl;   
        }
        */
        printf("Case #%d:\n",t);
        while (q--)
        {
            int num;
            cin>>num;   
            for (int i=0;i<w;i++)
                for (int j=0;j<w;j++)
                    for (int k=0;k<maxrange;k++)
                        f[1][i][j][k]="";
            for (int i=0;i<w;i++)
                for (int j=0;j<w;j++)
                    if (g[i][j]!='+'&&g[i][j]!='-')
                        f[1][i][j][g[i][j]-'0'+delta]=g[i][j];
            int cur=1;
            do
            {
                string ans="";
                for (int k=0;k<maxrange;k++)
                    for (int i=0;i<w;i++)
                        for (int j=0;j<w;j++)
                            f[cur^1][i][j][k]="";
                for (int k=0;k<maxrange;k++)
                    for (int i=0;i<w;i++)
                        for (int j=0;j<w;j++)
                            if (f[cur][i][j][k]!="")
                            {
                                if (k-delta==num)
                                {
                                    if (ans==""||f[cur][i][j][k]<ans)
                                        ans=f[cur][i][j][k];   
                                }
                                for (int d1=0;d1<4;d1++)
                                {
                                    int x1=i+dx[d1],y1=j+dy[d1];
                                    if (!inrange(x1,y1,w))  continue;
                                    for (int d2=0;d2<4;d2++)
                                    {
                                        int x2=x1+dx[d2],y2=y1+dy[d2];
                                        if (!inrange(x2,y2,w))  continue;
                                        int num=g[x2][y2]-'0';
                                        if (g[x1][y1]=='+')
                                            num=k+num;
                                        else
                                            num=k-num;
                                        if (num<0||num>=maxrange)   continue;
                                        string tmp=f[cur][i][j][k]+g[x1][y1]+g[x2][y2];
                                        if (f[cur^1][x2][y2][num]==""||tmp<f[cur^1][x2][y2][num])
                                            f[cur^1][x2][y2][num]=tmp;
                                    }   
                                }
                            }
                if (ans!="")
                {
                    cout<<ans<<endl;
                    break;   
                }
                cur^=1;
            }while (1);
        }
    }
}
