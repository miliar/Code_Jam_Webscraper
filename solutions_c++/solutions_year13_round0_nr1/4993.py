#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;
typedef long long LL;
char a[10][10];
bool check(char ch)
{
    int i,j;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
            if(a[i][j] != 'T' && a[i][j] != ch)
               break;
        if(j >= 4) break;
    }
    if(i < 4) return true;

    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
            if(a[j][i] != 'T' && a[j][i] != ch)
               break;
        if(j >= 4) break;
    }
    if(i < 4) return true;

    for(i=0; i<4; i++)
        if(a[i][i]!='T' && a[i][i]!=ch)
          break;
    if(i >= 4) return true;
    for(i=0; i<4; i++)
        if(a[i][3-i]!='T' && a[i][3-i]!=ch)
           break;
    if(i >= 4) return true;
    return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("lww_out.txt","w",stdout);

    int T,ta=1;
    scanf("%d",&T);
    while(T--)
    {
        int i,j,flag=0;
        for(i=0; i<4; i++) scanf(" %s",a[i]);

        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
               if(a[i][j] == '.')
                 break;
            if(j < 4) break;
        }
        if(i < 4) flag = 3;

        if(check('X')) flag = 1;
        if(check('O')) flag = 2;

        printf("Case #%d: ",ta++);
        if(flag == 1) puts("X won");
        else if(flag == 2) puts("O won");
        else if(flag == 3) puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
