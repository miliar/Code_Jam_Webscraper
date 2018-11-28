#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;

char tt[4][4];

bool check(char pl)
{
    int i,j,k,f;

    for(i=0;i<4;i++)
    {
        f=1;
        for(j=0;j<4;j++)
        {
            if(tt[i][j]!=pl && tt[i][j]!='T')
                f=0;
        }
        if(f)
            return true;
    }

    for(i=0;i<4;i++)
    {
        f=1;
        for(j=0;j<4;j++)
        {
            if(tt[j][i]!=pl && tt[j][i]!='T')
                f=0;
        }
        if(f)
            return true;
    }

    f=1;
    for(i=0;i<4;i++)
    {
        if(tt[i][i]!=pl && tt[i][i]!='T')
            f=0;
    }
    if(f)
        return true;

    f=1;
    for(i=0;i<4;i++)
    {
        if(tt[i][3-i]!=pl && tt[i][3-i]!='T')
            f=0;
    }
    if(f)
        return true;

    return false;
}

bool complete()
{
    int i,j;

    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(tt[i][j]=='.')
                return false;
        }
    }

    return true;
}

int main()
{
    int t,n,m,i,j,k,l=0;
    S(t);
    getchar();
    while(t--)
    {
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                tt[i][j]=getchar();
            }
            getchar();
        }
        getchar();

        l++;
        if(check('X'))
        {
            printf("Case #%d: X won\n",l);
        }
        else if(check('O'))
        {
            printf("Case #%d: O won\n",l);
        }
        else if(complete())
        {
            printf("Case #%d: Draw\n",l);
        }
        else
        {
            printf("Case #%d: Game has not completed\n",l);
        }
    }

    return 0;
}

