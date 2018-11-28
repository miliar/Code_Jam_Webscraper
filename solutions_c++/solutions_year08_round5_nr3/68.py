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
char board[10][10];

int mem[1<<10][10];

int rec(int mask, int y)
{
    if(y==H) return 0;
    int &r=mem[mask][y];
    if(r!=-1) return r;
    r=0;
    int T=1<<W;
    int best=0;
    for (int b=0;b<T;b++)
    {
        bool valid=true;
        int c=0;
        for (int i=0;i<W;i++) if(b&(1<<i))
        {
            c++;
            if(board[i][y]!='.')
            {
                valid=false;
                continue;
            }
            int nx=i+1;
            if(nx<W)
            {
                if(b&(1<<nx)) valid=false;
                if(mask&(1<<nx)) valid=false;
            }
            nx=i-1;
            if(nx>=0)
            {
                if(b&(1<<nx)) valid=false;
                if(mask&(1<<nx)) valid=false;
            }
            //if(mask&(1<<i)) valid=false;
            if(!valid) break;
        }
        if(valid) 
            r>?=c+rec(b,y+1);
        if(c+rec(b,y+1)==r) best=b;
    }
    //if( (mask==5) && (y==1) ) cerr<<"|| "<<mask<<","<<y<<" "<<best<<endl;
    return r;
}

int solve()
{
    /*for(int i=0;i<H;i++)
    {
        for(int j=0;j<W;j++) cerr<<board[j][i];
        cerr<<endl;
    }*/
    memset(mem,-1,sizeof(mem));
    return rec(0, 0);
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
                cin>>board[j][H-x-1];

        cout<<"Case #"<<i<<": "<<solve()<<endl;       
    }
    return 0;
}
