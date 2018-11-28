/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//#pragma comment(linker,"/STACK:256000000")
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <set>

#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF 1000000500
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int,int >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt printf
#define big long long
#define VI vector <int>
#define DID (long long)


using namespace std;

bool flag;
char c[10][10];
int t,i,j,T;

bool check1()
{
    int i,j;
    for (i=0;i<4;i++)
    {
        flag=1;
        for (j=0;j<4;j++)
        if (!(c[i][j]=='X' || c[i][j]=='T')) flag=0;
        if (flag) return 1;

        flag=1;
        for (j=0;j<4;j++)
        if (!(c[j][i]=='X' || c[j][i]=='T')) flag=0;
        if (flag) return 1;
    }

    flag=1;
    for (i=0;i<4;i++)
        if (!(c[i][i]=='X' || c[i][i]=='T')) flag=0;
    if (flag) return 1;

    flag=1;
    for (i=0;i<4;i++)
        if (!(c[i][3-i]=='X' || c[i][3-i]=='T')) flag=0;
    if (flag) return 1;
}

bool check2()
{
    int i,j;
    for (i=0;i<4;i++)
    {
        flag=1;
        for (j=0;j<4;j++)
        if (!(c[i][j]=='O' || c[i][j]=='T')) flag=0;
        if (flag) return 1;

        flag=1;
        for (j=0;j<4;j++)
        if (!(c[j][i]=='O' || c[j][i]=='T')) flag=0;
        if (flag) return 1;
    }

    flag=1;
    for (i=0;i<4;i++)
        if (!(c[i][i]=='O' || c[i][i]=='T')) flag=0;
    if (flag) return 1;

    flag=1;
    for (i=0;i<4;i++)
        if (!(c[i][3-i]=='O' || c[i][3-i]=='T')) flag=0;
    if (flag) return 1;
}

bool check3()
{
    int i,j;

    for (i=0;i<4;i++)
        for (j=0;j<4;j++)
        if (c[i][j]=='.') return 0;

    return 1;
}
main()
{
    freopen("text.in","r",stdin);   freopen("text.out","w",stdout);

    scanf("%d\n",&T);
    for (t=1;t<=T;t++)
    {
        for (i=0;i<4;i++){
            for (j=0;j<4;j++)
            scanf("%c",&c[i][j]);
            scanf("\n");}

        cout<<"Case #"<<t<<": ";
        if (check1())
            cout<<"X won"<<endl; else if (check2())
            cout<<"O won"<<endl;else
            if (check3()) cout<<"Draw"<<endl; else
            cout<<"Game has not completed"<<endl;
    }
}


