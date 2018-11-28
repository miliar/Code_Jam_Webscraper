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
#include<set>

using namespace std;

//=========================================================
// libs:
//
//=========================================================
// program:
//
int r,c;
char board[15][15];
int dx[8]={0, 0, 1, 1,1,-1,-1,-1};
int dy[8]={1,-1, 1,-1,0, 1,-1, 0};

char mem[1<<16][4][4];



bool rec(int mask, int x, int y)
{
    char &res = mem[mask][x][y];
    
    if(res!=-1) return res;

    res=0;
    for (int t=0;t<8;t++)
    {
        int nx=x+dx[t];
        int ny=y+dy[t];
        if((nx<0)||(nx>=r)||(ny<0)||(ny>=c)) continue;
        int ind = nx*c+ny;
        //cout<<" "<<ind<<"{";
        if ( (mask&(1<<ind)) && !rec(mask-(1<<ind),nx,ny) )
            res=1;
        
        
    }
    return res;
   
   
}

bool solve()
{
    assert(r<=4);
    assert(c<=4);
    int mask=0;
    int x=-1,y=-1;
    for (int i=0;i<r;i++)
        for (int j=0;j<c;j++)
            if(board[i][j]=='.')
                mask|=( 1<< (i*c+j) );
            else if(board[i][j]=='K')
                x=i,y=j;
    memset(mem,-1,sizeof(mem));
    return rec(mask,x,y);
}

inline void init(){}
//=========================================================
// I/O:
//
int main()
{
    init();
    
    int C; cin>>C;
    for (int i=1;i<=C;i++)
    {
        cin>>r>>c;
        for (int x=r;x--;)
            for (int y=c;y--;)
                cin>>board[x][y];
        
        bool res=solve();
        cerr<<"["<<i<<" / "<<C<<"]"<<endl;
        cout<<"Case #"<<i<<": " << (res?'A':'B')  << endl;
        
        
        
    }
    return 0;
}
