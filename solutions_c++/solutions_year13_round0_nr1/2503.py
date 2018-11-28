#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <ctime>
#define mod 1000000007
#define INF 10000
using namespace std;

char str[10][10];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int tot=0,a,b,c,flag=0,i,j;
        for(i=0;i<4;i++)
            scanf("%s",str[i]);
        for(i=0;i<4;i++)
        {
            a=0;
            b=0;
            c=0;
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='X')
                    a++;
                if(str[i][j]=='O')
                    b++;
                if(str[i][j]=='T')
                    c++;
                if(str[i][j]=='.')
                    tot++;
            }
            if(a+c==4)
                flag=1;
            if(b+c==4)
                flag=2;
        }
        for(j=0;j<4;j++)
        {
            a=0;
            b=0;
            c=0;
            for(i=0;i<4;i++)
            {
                if(str[i][j]=='X')
                    a++;
                if(str[i][j]=='O')
                    b++;
                if(str[i][j]=='T')
                    c++;
            }
            if(a+c==4)
                flag=1;
            if(b+c==4)
                flag=2;
        }
        a=0;
        b=0;
        c=0;
        for(i=0;i<4;i++)
        {
            if(str[i][i]=='X')
                a++;
            if(str[i][i]=='O')
                b++;
            if(str[i][j]=='T')
                c++;
        }
        if(a+c==4)
            flag=1;
        if(b+c==4)
            flag=2;
        a=0;
        b=0;
        c=0;
        for(i=0;i<4;i++)
        {
            if(str[i][3-i]=='X')
                a++;
            if(str[i][3-i]=='O')
                b++;
            if(str[i][3-i]=='T')
                c++;
        }
        if(a+c==4)
            flag=1;
        if(b+c==4)
            flag=2;
        if(flag==1)
            printf("Case #%d: X won\n",++cas);
        else if(flag==2)
            printf("Case #%d: O won\n",++cas);
        else
        {
            if(tot==0)
                printf("Case #%d: Draw\n",++cas);
            else
                printf("Case #%d: Game has not completed\n",++cas);
        }
    }
    return 0;
}
