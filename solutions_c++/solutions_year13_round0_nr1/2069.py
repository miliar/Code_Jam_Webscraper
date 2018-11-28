#define filer() freopen("f.in","r",stdin)
#define filew() freopen("out.txt","w",stdout)
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stack>
#include<string>
#include<vector>
#include <map>
#define INF 1<<29
#define PI pair<int,int>

#define SET(a, x) memset((a), (x), sizeof(a))
#define pb push_back
#define i64 long long
#define EPS (1e-9)
using namespace std;
typedef vector<int> VI;
typedef vector<PI> vii;
//i64 INF=(i64)((i64)1<<(i64)59);

int N;
char grid[10][10];

void print(int x,bool t,int cas)
{
    if(x==1)printf("Case #%d: X won\n",cas);
    else if(x==2)printf("Case #%d: O won\n",cas);
    else if( t==1)printf("Case #%d: Game has not completed\n",cas);
    else printf("Case #%d: Draw\n",cas);
}

int main()
{
    //filer();
    //filew();
    int T,cas=0;
    int i,j;
    scanf("%d",&T);
    //while(T--)
    for(cas=1;cas<=T;cas++)
    {
        int x=0;
        bool t=0;
        for(i=1;i<=4;i++)scanf("%s",grid[i]+1);

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(grid[i][j]=='.')t=1;
                //cout<<grid[i][j];
            }//cout<<endl;
        }//cout<<endl;

        //Column checkin
        bool t1=0;
        for(j=1;j<=4;j++)
        {
            t1=0;
            for(i=1;i<=4;i++)
            {
                if(grid[i][j]!='T' && grid[i][j]!='X')t1=1;
            }
            if(t1==0)
            {
                x=1;
                print(x,t,cas);
                break;
            }
        }
        if(!t1)continue;

        t1=0;
        for(j=1;j<=4;j++)
        {
            t1=0;
            for(i=1;i<=4;i++)
            {
                if(grid[i][j]!='T' && grid[i][j]!='O')t1=1;
            }
            if(t1==0)
            {
                x=2;
                print(x,t,cas);
                break;
            }
        }
        if(t1==0)continue;

        //Row Checking

        for(i=1;i<=4;i++)
        {
            t1=0;
            for(j=1;j<=4;j++)
            {
                if(grid[i][j]!='T' && grid[i][j]!='X')t1=1;
            }
            if(t1==0)
            {
                x=1;
                print(x,t,cas);
                break;
            }

        }
        if(!t1)continue;

        for(i=1;i<=4;i++)
        {
            t1=0;
            for(j=1;j<=4;j++)
            {
                if(grid[i][j]!='T' && grid[i][j]!='O')t1=1;
            }
            if(t1==0)
            {
                x=2;
                print(x,t,cas);
                break;
            }

        }
        if(!t1)continue;

        //diagonal checkin
        t1=0;
        for(i=1;i<=4;i++)
        {
            if(grid[i][i]!='T' && grid[i][i]!='X')t1=1;
        }
        if(t1==0)
        {
            x=1;
            print(x,t,cas);
            //break;
        }
        if(!t1)continue;
        t1=0;
        for(i=1;i<=4;i++)
        {
            if(grid[i][i]!='T' && grid[i][i]!='O')t1=1;
        }
        if(t1==0)
        {
            x=2;
            print(x,t,cas);
            //break;
        }

        if(!t1)continue;


        t1=0;
        for(i=1;i<=4;i++)
        {
            if(grid[i][5-i]!='T' && grid[i][5-i]!='X')t1=1;
        }
        if(!t1)
        {
            x=1;
            print(x,t,cas);
            //break;
        }
        if(!t1)continue;


        t1=0;
        for(i=1;i<=4;i++)
        {
            if(grid[i][5-i]!='T' && grid[i][5-i]!='O')t1=1;
        }
        if(!t1)
        {
            x=2;
            print(x,t,cas);
            //break;
        }
        if(!t1)continue;

        print(x,t,cas);



    }

    return 0;
}
/*
Test Case:

*/

