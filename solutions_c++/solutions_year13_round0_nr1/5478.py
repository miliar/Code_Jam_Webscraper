/*
uva :
author : rafsan
algo :
*/
#include<iostream>
#include<algorithm>
#include<bitset>
#include<cctype>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<climits>
#include<functional>
#include<istream>
#include<iterator>
#include<iomanip>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>

using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b-1);i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define PB push_back
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define PII pair<int,int>
#define PCC pair<char,char>
#define PIC pair<int,char>
#define PCI pair<char,int>
#define FST first
#define SEC second
#define VS vector<string>
#define VI vector<int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define MIN(a,b) (a>b?b:a)
#define MAX(a,b) (a>b?a:b)
#define PI acos(-1.0)
#define RADIANS(x) (((1.0 * x * PI) / 180.0))
#define DEGREES(x) (((x * 180.0) / (1.0 * pi)))
#define SINE(x) (sin(RADIANS(x)))
#define COSINE(x) (cos(RADIANS(x)))
#define SETBIT(x, i) (x |= (1 << i))
#define TANGENT(x) (tan(RADIANS(x)))
#define ARCSINE(x) (DEGREES((asin(x))))
#define RESETBIT(x, i) (x &= (~(1 << i)))
#define ARCCOSINE(x) (DEGREES((acos(x))))
#define ARCTANGENT(x) (DEGREES((atan(x))))
#define INFILE() freopen("A-small-attempt1.in","r",stdin)
#define OUTFILE()freopen("out_at_1.out","w",stdout)
#define IN scanf
#define OUT printf
#define LL long long
#define ULL unsigned long long
#define EPS 1e-9
#define MOD 10007
#define LIM 4

//int dx[]= {0,0,1,-1};
//int dy[]= {-1,1,0,0};
char g[5][5];
int checkX()
{
    int T=0,X=0;

    FOR(i,0,4)
    {
        X=0;
        T=0;
        FOR(j,0,4)
        {
            if(g[i][j]=='X')X++;
            else if(g[i][j]=='T')T++;
            else break;
        }
       // cout<<X<<"->"<<T<<endl;
        if(T<=1&& X+T==4)return 4;
    }

    return 0;
}
int checkXX()
{
    int T=0,X=0;
    FOR(j,0,4)
    {
        X=0;
        T=0;
        FOR(i,0,4)
        {
            if(g[i][j]=='X')X++;
            else if(g[i][j]=='T')T++;
            else break;
        }
        if(T<=1&&X+T==4)return 4;
    }
    return 0;
}
int checkY()
{
    int T=0,Y=0;
    FOR(i,0,4)
    {
        Y=0;
        T=0;
        FOR(j,0,4)
        {
            if(g[i][j]=='O')Y++;
            else if(g[i][j]=='T')T++;
            else break;
        }
        if(T<=1&&Y+T==4)return 4;
    }
    return 0;
}
int checkYY()
{
    int T=0,X=0;
    FOR(j,0,4)
    {
        X=0;
        T=0;
        FOR(i,0,4)
        {
            if(g[i][j]=='O')X++;
            else if(g[i][j]=='T')T++;
            else break;
        }
        if(T<=1&&X+T==4)return 4;
    }
    return 0;
}
bool isok()
{
    FOR(i,0,4)FOR(j,0,4)if(g[i][j]=='.')return 0;
    return 1;
}
int main()
{
    int ks;
    INFILE();
    OUTFILE();
    cin>>ks;
    FOR(cas,1,ks+1)
    {
        CLR(g);
        FOR(i,0,4)cin>>g[i];
        int X=0,Y=0,T=0,resX=0,resY=0;;
        FOR(i,0,4)
        {
            if(g[i][i]=='O')Y++;
            else if(g[i][i]=='T')T++;
            else Y=0;
        }
        if(T<=1)resY=max(resY,Y+T);
        T=0;
        Y=0;
        RFOR(i,0,4)
        {
            if(g[3-i][i]=='O')Y++;
            else if(g[3-i][i]=='T')T++;
            else break;
        }

        if(T<=1)resY=max(resY,Y+T);
        T=X=0;
        FOR(i,0,4)
        {

            if(g[i][i]=='X')X++;
            else if(g[i][i]=='X')T++;
            else break;
        }
        if(T<=1)resX=max(resX,X+T);
        T=X=0;
        RFOR(i,0,4)
        {
          //  cout<<g[3-i][i]<<" " <<3-i<<" "<<i <<"===\n";
            if(g[3-i][i]=='X')X++;
            else if(g[3-i][i]=='T')T++;
            else break;
        }
 //   cout<<X<<"-->"<<T<<endl;
        if(T<=1)resX=max(resX,X+T);

        //cout<<checkX()<<"---\n";
        resX=max(resX,checkX());
        resX=max(resX,checkXX());
        resY=max(resY,checkY());
        resY=max(resY,checkYY());

        X=Y=0;
        FOR(i,0,4)FOR(j,0,4){if(g[i][j]=='X')X++;if(g[i][j]=='O')Y++;}
        bool state=isok();

        cout<<"Case #"<<cas<<": ";
        if(resX==4&&resY==4){if(X>Y)cout<<"X won\n";else cout<<"O won\n";}
        else if(resX==4)cout<<"X won\n";
        else if(resY==4)cout<<"O won\n";
        else if(state)cout<<"Draw\n";
        else cout<<"Game has not completed\n";

    }
    return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
*/
