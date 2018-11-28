#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>


using namespace std;

int W,H;

char board[15][15];
int visited[15][15][15][15];
struct node
{
    int x,y, bx,by;
    int steps;
    
};


struct priority
{
    bool operator ()(const node a, const node b)
    {
        return (a.steps>b.steps);
    }
};


int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

bool wbounds(int x, int y)
{
    if((x<0)||(y<0)||(x>=W)||(y>=H)) return false;
    return (board[x][y]=='.');
}
bool bounds(int x, int y)
{
    if((x<0)||(y<0)||(x>=W)||(y>=H)) return false;
    return (true);
}

int solve()
{
    priority_queue< node, vector<node> , priority > Q;
    int mx=0,my=0,cx,cy;




    for (int i=W;i--;)
        for (int j=H;j--;)
            if(board[i][j]=='O')
            {
                mx=i,my=j;
                board[i][j]='.';
            }
            else if(board[i][j]=='X')
            {
                cx=i,cy=j;
                board[i][j]='.';
            }
            
            
    /*for (int j=H;j--;)
    {
        for (int i=W;i--;) cout<<board[i][j];
        cout<<endl;
    }*/
                    
    node nd;
    nd.x=mx,nd.y=my,nd.bx=mx,nd.by=my;
    nd.steps=0;
    
    Q.push(nd);
    memset(visited,-1,sizeof(visited));
    visited[mx][my][mx][my]=0;
    //cout<<"("<<cx<<","<<cy<<")]"<<endl;
    while(! Q.empty() )
    {
        nd=Q.top();
        Q.pop();
        
        int x=nd.x,y=nd.y;
        int bx=nd.bx,by=nd.by;
        
        if(visited[x][y][bx][by]<nd.steps) continue;
        //cout<<string(nd.steps+1,' ')<<"("<<x<<","<<y<<","<<bx<<","<<by<<")"<<endl;
        
        if((x==cx)&&(y==cy)) return nd.steps;
        //try shooting the portal:
        for (int r=0;r<4;r++)
        {
            int wx=x, wy=y;
            while (wbounds(wx+dx[r],wy+dy[r] )) wx+=dx[r],wy+=dy[r];
            //try to shoot portal at (wx,wy)
            if((visited[x][y][wx][wy]==-1) || (visited[x][y][wx][wy]>nd.steps)  )
            {
                visited[x][y][wx][wy]=nd.steps;
                node nnd;
                nnd.x=x;
                nnd.y=y;
                nnd.bx=wx;
                nnd.by=wy;
                nnd.steps=nd.steps;
                Q.push(nnd);
            }
        }
        
        //try moving
        for (int r=0;r<4;r++)
        {
            int nx=x+dx[r],ny=y+dy[r];
            
            
            if(! wbounds(nx,ny) ) //a wall,
            {
                if((visited[bx][by][bx][by]==-1) || (visited[bx][by][bx][by]>nd.steps+1)  )
                {
                    visited[bx][by][bx][by]=nd.steps+1;
                    node nnd;
                    nnd.x=bx;
                    nnd.y=by;
                    nnd.bx=bx;
                    nnd.by=by;
                    nnd.steps=nd.steps+1;
                    Q.push(nnd);
                    //cout<<"used portal"<<endl;
                }
            }
            else
            {
                if((visited[nx][ny][bx][by]==-1) || (visited[nx][ny][bx][by]>nd.steps+1)  )
                {
                    visited[nx][ny][bx][by]=nd.steps+1;
                    node nnd;
                    nnd.x=nx;
                    nnd.y=ny;
                    nnd.bx=bx;
                    nnd.by=by;
                    nnd.steps=nd.steps+1;
                    Q.push(nnd);
                }

            }
        }
        
        
        
    }
    
    return -1;
}

//=========================================================
// I/O:
//
int main()
{
    int C; cin>>C;
    for (int i=1;i<=C;i++)
    {
        memset(board,'?',sizeof(board));
        cin>>H>>W;
        for (int x=0;x<H;x++)
            for (int j=0;j<W;j++)
                cin>>board[j][x];

        int r=solve();
        cout<<"Case #"<<i<<": ";
        if(r<0) cout<<"THE CAKE IS A LIE";
        else cout<<r;
        cout<<endl;
    }
    return 0;
}
