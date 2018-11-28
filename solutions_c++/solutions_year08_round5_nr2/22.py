#include <cstdio>
#include <iostream>
#include <list>
#include <map>
#include <algorithm>
#define MAXM 15
#define MAXN 15
using namespace std;

const int dx[4]={-1,0,1,0};
const int dy[4]={0,1,0,-1};
char board[MAXN+1][MAXM+1];
int n,m,sx,sy,tx,ty;

struct State
{
    int x;
    int y;
    int x1;
    int y1;
    int x2;
    int y2;
    int type;
    State()
    {
    }
    State(int a,int b)
    {
        x=a;
        y=b;
        x1=0;
        y1=0;
        x2=0;
        y2=0;
        type=0;
    }
};

map<long long,int> M;
list<State> Q;

long long gethash(const State &s)
{
    return (((((s.type*41LL+s.x)*41LL+s.y)*41LL+s.x1)*41LL+s.y1)*41LL+s.x2)*41LL+s.y2;
}

bool valid(int x,int y)
{
    if((x>=0)&&(x<n)&&(y>=0)&&(y<m)&&(board[x][y]=='.'))
    {
        return true;
    }
    else
    {
        return false;
    }
}

void addnewstate(const State &s,int nextstep,int currstep)
{
    if((M.find(gethash(s))==M.end())||(M[gethash(s)]>nextstep))
    {
        M[gethash(s)]=nextstep;
        if(nextstep==currstep)
        {
            Q.push_front(s);
        }
        else
        {
            Q.push_back(s);
        }
    }
}

void BFS()
{
    State p,q;
    int i,j,k,d,nx,ny,step;
    M.clear();
    Q.clear();
    p=State(sx,sy);
    M[gethash(p)]=0;
    Q.push_back(p);
    while(Q.empty()==false)
    {
        q=Q.front();
        Q.pop_front();
        step=M[gethash(q)];
        if((q.x==tx)&&(q.y==ty))
        {
            printf("%d\n",step);
            return;
        }
        for(d=0;d<4;d++)
        {
            nx=q.x+dx[d];
            ny=q.y+dy[d];
            if(valid(nx,ny)==true)
            {
                p=q;
                p.x=nx;
                p.y=ny;
                addnewstate(p,step+1,step);
            }
        }
        if(q.type!=2)
        {
            for(d=0;d<4;d++)
            {
                for(k=0;k<MAXN;k++)
                {
                    nx=q.x+k*dx[d];
                    ny=q.y+k*dy[d];
                    if(valid(nx,ny)==false)
                    {
                        break;
                    }
                }
                nx=q.x+(k-1)*dx[d];
                ny=q.y+(k-1)*dy[d];
                p=q;
                p.x2=q.x1;
                p.y2=q.y1;
                p.x1=nx;
                p.y1=ny;
                p.type++;
                addnewstate(p,step,step);
            }
        }
        if(q.type!=0)
        {
            p=q;
            p.x1=p.x2;
            p.y1=p.y2;
            p.x2=-1;
            p.y2=-1;
            p.type--;
            addnewstate(p,step,step);
        }
        if(q.type==2)
        {
            p=q;
            swap(p.x1,p.x2);
            swap(p.y1,p.y2);
            addnewstate(p,step,step);
            if((q.x==q.x1)&&(q.y==q.y1))
            {
                p=q;
                p.x=p.x2;
                p.y=p.y2;
                addnewstate(p,step+1,step);
            }
        }
    }
    printf("THE CAKE IS A LIE\n");
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,t;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            scanf("%s",board[i]);
            for(j=0;j<m;j++)
            {
                if(board[i][j]=='O')
                {
                    board[i][j]='.';
                    sx=i;
                    sy=j;
                }
                if(board[i][j]=='X')
                {
                    board[i][j]='.';
                    tx=i;
                    ty=j;
                }
            }
        }
        printf("Case #%d: ",k+1);
        BFS();
    }
    return 0;
}
