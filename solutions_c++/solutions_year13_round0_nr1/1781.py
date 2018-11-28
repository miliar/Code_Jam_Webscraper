/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
#define M 1000000007


int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int t,caseno=1;
    scanf("%d\n",&t);
    while(t--)
    {
        char game[5][5];
        for(int i=0;i<4;i++)
        {
            gets(game[i]);
//            puts(game[i]);
        }
        gets(game[4]);
        int tx,ty;
        tx=ty=-1;
        bool dothas=0;

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                if(game[i][j]=='O')game[i][j]='Y';
                if(game[i][j]=='T')
                {
                    tx=i;
                    ty=j;
                }
                if(game[i][j]=='.')
                    dothas=1;
            }

        if(tx!=-1)
        {
            game[tx][ty]='X';
        }
        bool xw,yw;
        xw=yw=0;
        if(game[0][0]=='X' && game[0][1]=='X' && game[0][2]=='X' && game[0][3]=='X')xw=1;
        if(game[1][0]=='X' && game[1][1]=='X' && game[1][2]=='X' && game[1][3]=='X')xw=1;
        if(game[2][0]=='X' && game[2][1]=='X' && game[2][2]=='X' && game[2][3]=='X')xw=1;
        if(game[3][0]=='X' && game[3][1]=='X' && game[3][2]=='X' && game[3][3]=='X')xw=1;
        if(game[0][0]=='X' && game[1][0]=='X' && game[2][0]=='X' && game[3][0]=='X')xw=1;
        if(game[0][1]=='X' && game[1][1]=='X' && game[2][1]=='X' && game[3][1]=='X')xw=1;
        if(game[0][2]=='X' && game[1][2]=='X' && game[2][2]=='X' && game[3][2]=='X')xw=1;
        if(game[0][3]=='X' && game[1][3]=='X' && game[2][3]=='X' && game[3][3]=='X')xw=1;
        if(game[0][0]=='X' && game[1][1]=='X' && game[2][2]=='X' && game[3][3]=='X')xw=1;
        if(game[0][3]=='X' && game[1][2]=='X' && game[2][1]=='X' && game[3][0]=='X')xw=1;

        if(tx!=-1)
        {
            game[tx][ty]='Y';
        }

        if(game[0][0]=='Y' && game[0][1]=='Y' && game[0][2]=='Y' && game[0][3]=='Y')yw=1;
        if(game[1][0]=='Y' && game[1][1]=='Y' && game[1][2]=='Y' && game[1][3]=='Y')yw=1;
        if(game[2][0]=='Y' && game[2][1]=='Y' && game[2][2]=='Y' && game[2][3]=='Y')yw=1;
        if(game[3][0]=='Y' && game[3][1]=='Y' && game[3][2]=='Y' && game[3][3]=='Y')yw=1;
        if(game[0][0]=='Y' && game[1][0]=='Y' && game[2][0]=='Y' && game[3][0]=='Y')yw=1;
        if(game[0][1]=='Y' && game[1][1]=='Y' && game[2][1]=='Y' && game[3][1]=='Y')yw=1;
        if(game[0][2]=='Y' && game[1][2]=='Y' && game[2][2]=='Y' && game[3][2]=='Y')yw=1;
        if(game[0][3]=='Y' && game[1][3]=='Y' && game[2][3]=='Y' && game[3][3]=='Y')yw=1;
        if(game[0][0]=='Y' && game[1][1]=='Y' && game[2][2]=='Y' && game[3][3]=='Y')yw=1;
        if(game[0][3]=='Y' && game[1][2]=='Y' && game[2][1]=='Y' && game[3][0]=='Y')yw=1;

        printf("Case #%d: ",caseno++);

        if(xw==1)
            printf("X won\n");
        else if(yw==1)
            printf("O won\n");
        else if(dothas)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
	return 0;
}
