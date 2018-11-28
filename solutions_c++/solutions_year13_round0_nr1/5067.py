#include <cctype> // knapsack Item print http://codepad.org/CDN8Aum3
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

#define nln puts("")
#define Max(a,b,c) max(a,max(b,c))      ///3 ta theke max
#define Min(a,b,c) min(a,min(b,c))      ///3 ta theke min
#define Pi acos(-1.0)                   ///PI er value

#define ALL(p) p.begin(),p.end()
#define MP(x, y) make_pair(x, y)

#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
char board[5][5];
int dots;

bool checkwin(char c)
{
    int row[5],col[5],Adg=0,Bdg=0;
    MEM(row,0);
    MEM(col,0);
    for(int i=1; i<=4; i++)
    {
        for(int j=1; j<=4; j++)
        {
            if(board[i][j]==c)row[i]++;
            if(board[i][j]==c)col[j]++;
            if(board[i][j]=='.')dots++;
            if(board[i][j]==c&&i==j)Adg++;
            if(board[i][j]==c&&i+j==5)Bdg++;
        }
    }
    for(int i=1; i<=4; i++)
    {
        if(row[i]==4)return true;
        if(col[i]==4)return true;
    }

    if(Adg==4)return true;
    if(Bdg==4)return true;

    for(int i=1; i<=4; i++)
    {
        if(row[i]==3)
        {
            for(int j=1;j<=4;j++)
                if(board[i][j]=='T')
                return true;
        }
        if(col[i]==3)
        {
            for(int j=1;j<=4;j++)
            {
                if(board[j][i]=='T')
                    return true;
            }
        }
    }

    if(Adg==3)
    {
        if(board[1][1]=='T'||board[2][2]=='T'||board[3][3]=='T'||board[4][4]=='T')
            return true;
    }
    if(Bdg==3)
    {
        if(board[1][4]=='T'||board[2][3]=='T'||board[3][2]=='T'||board[4][1]=='T')
            return true;
    }
    return false;
}

int main()
{
    //READ("input.txt");
    //WRITE("output.txt");
    int kase,a,b,diff,t=1,cnt,i,j;
    cin>>kase;

    while(kase--)
    {
        getchar();
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                scanf("%c",&board[i][j]);
            }
            getchar();
        }

        dots=0;
        bool winx=checkwin('X');
        bool wino=checkwin('O');

        cout<<"Case #"<<t++<<": ";
        if(winx)puts("X won");
        else if(wino)puts("O won");
        else if(!dots)puts("Draw");
        else puts("Game has not completed");

    }
    return 0;
}


