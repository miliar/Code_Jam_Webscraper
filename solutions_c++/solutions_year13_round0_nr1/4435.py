#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);






int st_x[10]={0,0,0,0,0,1,2,3,0,0};
int st_y[10]={0,1,2,3,0,0,0,0,0,3};
int dx[10]  ={1,1,1,1,0,0,0,0,1,1};
int dy[10]  ={0,0,0,0,1,1,1,1,1,-1};
char in[6][6];
int tx,ty;



vector<int> ptx,pty;

int chek(char ch)
{
    int ret=0;
    int k,x,y,i;
     for(k=0;k<10;k++)
        {
            x=st_x[k];
            y=st_y[k];

            int same=1;

            for(i=0;i<4;i++)
            {
                if(in[x][y]!=in[ x+i*dx[k]  ][y +i*dy[k] ]) same=0;
            }


            if(same)
            {
                if(in[x][y]==ch) ret=1;
            }
        }

    return ret;
}
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);

   //  freopen("in.txt","r",stdin);


    int T,i,j,k,cs,x,y;

    scanf("%d",&T);




    for(cs=1;cs<=T;cs++)
    {
        ptx.clear();
        pty.clear();


        printf("Case #%d: ",cs);
        for(i=0;i<4;i++)
        {
            scanf("%s",in[i]);
        }

        int x_won=0;
        int o_won=0;

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(in[i][j]=='T')
                {
                    ptx.push_back(i);
                    pty.push_back(j);
                }
            }


        for(i=0;i<ptx.size();i++)
        {
            in[ ptx[i] ][ pty[i] ]='O';
        }
        o_won=chek('O');

        for(i=0;i<ptx.size();i++)
        {
            in[ ptx[i] ][ pty[i] ]='X';
        }
        x_won=chek('X');




















        if(x_won)
        {
            printf("X won\n");
            continue;
        }

        if(o_won)
        {
            printf("O won\n");
            continue;
        }




        int draw=1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(in[i][j]=='.') draw=0;
            }


        if(draw)
        {
            printf("Draw\n");
            continue;
        }


        printf("Game has not completed\n");


    }

    return 0;
}
