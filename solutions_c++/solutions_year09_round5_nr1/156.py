#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int N = 1005,INF = 1<<29;
const double eps = 1e-10;
const double pi = acos(-1.);
int n,m,L;
char s[13][13];
typedef pair<char,char> pcc;
#define MP(A,B) make_pair((A),(B))
#define pb push_back
typedef vector<pcc> vt;
vt a,b;
char tp[13][13],tq[13][13];
map<vt,int> mp;
vt getstate(char p[13][13])
{
    vt x;
    x.clear();
    int ct = 0;
    int i,j;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            if(p[i][j]==1)
            {
          //      puts("x");
                x.pb(MP(i,j));
            }
   // for(i=0;i<x.size();i++)printf("%d,%d   ",x[i].first,x[i].second);puts("");
    return x;
}
bool isok(vt x)
{
    for(int i=0;i<x.size();i++)
        if(x[i]!=b[i])return 0;
    return 1;
}
int head,tail;
vt q[1000005];
int val[1000005];
bool ok(int x,int y)
{return x>=0&&x<n&&y>=0&&y<m;}
int dx[]={1,0,0,-1};
int dy[]={0,1,-1,0};
bool yes(vt x)
{
    if(L==1)return 1;
    for(int i=0;i<L;i++)
    {
        int tx,ty;
        int j;
        tx=x[i].first;
        ty=x[i].second;
        for(j=0;j<4;j++)
        {
            int k;
            int nx,ny;
            nx=tx+dx[j];
            ny=ty+dy[j];
            for(k=0;k<L;k++)
                if(nx==x[k].first&&ny==x[k].second)break;
            if(k<L)break;
        }
        if(j==4)return 0;
    }
    return 1;
}
int bfs()
{
    int i,j,k;
    if(isok(a))return 0;
   // puts("xxx");
    mp[a]=0;
    head=tail=0;
    q[tail++]=a;
    val[tail-1]=0;
    for(j=0;j<n;j++)
    {
        for(k=0;k<m;k++)
        {
            tp[j][k]=s[j][k];
           // printf("%d",s[j][k]);

        }
        //puts("");
    }
    for(i=0;i<tail;i++)
    {
        vt x = q[i];
        //printf("state : ");
        for(j=0;j<L;j++)
        {
            tp[x[j].first][x[j].second]=1;
           // printf("%d,%d ",x[j].first,x[j].second);
        }
        //puts("");
        int y1 = yes(x);
        //printf("%d : %d\n",i,y1);
        for(j=0;j<L;j++)
        {
            int tx = x[j].first;
            int ty = x[j].second;
            for(k=0;k<4;k++)
            {
                int nx,ny;
                int ox,oy;
                ox=tx+dx[k];
                oy=ty+dy[k];
                nx=tx-dx[k];
                ny=ty-dy[k];
            //    printf("%d,%d - %d,%d\n",ox,oy,nx,ny);
                if(ok(ox,oy)&&ok(nx,ny)&&!tp[ox][oy]&&!tp[nx][ny])
                {
                    tp[nx][ny]=1;
                    tp[tx][ty]=0;
                    vt y;
                    y=getstate(tp);tp[nx][ny]=0;
                    tp[tx][ty]=1;
                //    puts("x");
                    int y2=yes(y);
                    //for(int u=0;u<L;u++)printf("%d,%d ",y[u].first,y[u].second);puts("");
                    if(y1==0&&y2==0)continue;
                    if(isok(y))return val[i]+1;
                    if(mp.find(y)==mp.end())
                    {//puts("xx");
                        mp[y]=val[i]+1;
                        q[tail]=y;
                        val[tail++]=val[i]+1;
                    }

                }
            }
        }
        for(j=0;j<L;j++)
            tp[x[j].first][x[j].second]=0;
    }
    return -1;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,K=1;

    int i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        mp.clear();
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            scanf("%s",s[i]);
           // puts(s[i]);
        }
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(s[i][j]=='o'||s[i][j]=='w')
                    tp[i][j]=1;
                else tp[i][j]=0;
        a=getstate(tp);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(s[i][j]=='x'||s[i][j]=='w')
                    tp[i][j]=1;
                else tp[i][j]=0;
        b=getstate(tp);
        L=b.size();
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(s[i][j]=='#')s[i][j]=2;
                else s[i][j]=0;
        printf("Case #%d: %d\n",K++,bfs());
    }
    return 0;
}
