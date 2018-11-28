#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <fstream>
#include <bitset>
#include <iomanip>
using namespace std;
#define INF 0x7ffffff
#define eps 1e-9
#define pi 3.14159265358979626
#define LL long long
#define clr(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define exch(a,b) {int t111=a;a=b;b=t111;}
#define sp struct point
#define sl struct line
#define zero(x) (((x)>0?(x):-(x))<eps)
#define read(a) scanf("%d",&a);

#define N 50500
#define M 600

char a[10][10];

bool win(char ch)
{
    bool f;
    FOR(i,0,3)
    {
        f=true;

        FOR(j,0,3) if (a[i][j]!=ch && a[i][j]!='T')
        {
            f=false;
            break;
        }
        if (f) return true;
    }
    FOR(i,0,3)
    {
        f=true;

        FOR(j,0,3) if (a[j][i]!=ch && a[j][i]!='T')
        {
            f=false;
            break;
        }
        if (f) return true;
    }

    f=true;
    FOR(i,0,3) if (a[i][i]!=ch && a[i][i]!='T')
    {
        f=false;
        break;
    }
    if (f) return true;
    f=true;
    FOR(i,0,3) if (a[i][3-i]!=ch && a[i][3-i]!='T')
    {
        f=false;
        break;
    }
    if (f) return true;

    return false;
}

bool check(char ch)
{
    FOR(i,0,3)
    FOR(j,0,3)
    if (a[i][j]==ch) return true;
    return false;
}

int main()
{
    //freopen("subset.in","r",stdin);freopen("subset.out","w",stdout);
    //freopen("A-large.in","r",stdin);
    //freopen("small1.out","w",stdout);

    int T;
    scanf("%d\n",&T);
    FOR(kk,1,T)
    {
        printf("Case #%d: ",kk);
        FOR(i,0,4) gets(a[i]);

        bool f;
        f=win('X');
        if (f)
        {
            puts("X won");
            continue;
        }
        f=win('O');
        if (f)
        {
            puts("O won");
            continue;
        }

        if (check('.')) puts("Game has not completed");
        else puts("Draw");
    }

    return 0;
}
