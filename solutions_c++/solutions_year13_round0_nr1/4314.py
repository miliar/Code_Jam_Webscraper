#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<utility>
#define ll long long
using namespace std;

bool check(char a[5][5],char x)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        if(x!=a[i][j] && a[i][j]!='T')
        break;

        if(j==4)
        return true;
    }

    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        if(x!=a[j][i] && a[j][i]!='T')
        break;

        if(j==4)
        return true;
    }

    for(i=0;i<4;i++)
    if(x!=a[i][i] && a[i][i]!='T')
    break;

    if(i==4)
    return true;

    for(i=0;i<4;i++)
    if(x!=a[i][3-i] && a[i][3-i]!='T')
    break;

    if(i==4)
    return true;
    return false;
}
int main()
{
    freopen("ina.txt","r",stdin);
    freopen("outa.txt","w",stdout);
    int t,T,i,j,k;
    char a[5][5];
    scanf("%d",&T);
    t=1;
    bool p,q,r;
    while(t<=T)
    {
        r=false;
        for(i=0;i<4;i++)
        {
            scanf("%s",a[i]);

            for(j=0;j<4;j++)
            if(a[i][j]=='.')
            r=true;
        }

        printf("Case #%d: ",t++);

        p=check(a,'X');
        q=check(a,'O');


        if(!p && !q)
        {
            if(!r)
            printf("Draw\n");
            else printf("Game has not completed\n");
        }
        else if (p && !q)
        {
            printf("X won\n");
        }
        else if(!p && q)
        {
            printf("O won\n");
        }

    }
return 0;
}
