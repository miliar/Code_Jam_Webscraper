#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <string>
#define LL long long
#define DB double

using namespace std;
const int N = 6;
char re[N][N];
int n;
int O,X,dr;
bool oor(int x,int y,char t)
{
    if(re[x][y]==t||re[x][y]=='T') return true;
    return false;
}
void solve()
{
    dr = 1;
    for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
    if(re[i][j]=='.') dr = 0;
    for(int i=0;i<4;i++)
    {
        int j,c=0;
        for(j=0;j<4;j++)
        if(re[i][j]=='O'||re[i][j]=='T')
        {
            if(re[i][j]=='T') c++;
        }
        else break;
        if(j>=4&&c<2) O = 1;
        c = 0;
        for(j=0;j<4;j++)
        if(re[j][i]=='O'||re[j][i]=='T')
        {
            if(re[i][j]=='T') c++;
        }
        else break;
        if(j>=4&&c<2) O = 1;
    }
    for(int i=0;i<4;i++)
    {
        int j,c=0;
        for(j=0;j<4;j++)
        if(re[i][j]=='X'||re[i][j]=='T')
        {
            if(re[i][j]=='T') c++;
        }
        else break;
        //cout<<j<<endl;

        if(j>=4&&c<2) X = 1;
        c = 0;
        for(j=0;j<4;j++)
        if(re[j][i]=='X'||re[j][i]=='T')
        {
            if(re[i][j]=='T') c++;
        }
        else break;
        if(j>=4&&c<2) X = 1;
    }
    int j,c=0;
    for(j=0;j<4;j++)
    if(!oor(j,j,'O')) break;
    else
    {
        if(re[j][j]=='T') c++;
    }
    if(j>=4&&c<2) O = 1;
    c = 0;
    for(j=0;j<4;j++)
    if(!oor(j,3-j,'O')) break;
    else
    {
        if(re[j][3-j]=='T') c++;
    }
    if(j>=4&&c<2) O = 1;
    c = 0;
    for(j=0;j<4;j++)
    if(!oor(j,j,'X')) break;
    else
    {
        if(re[j][j]=='T') c++;
    }
    if(j>=4&&c<2) X = 1;
    c = 0;
    for(j=0;j<4;j++)
    if(!oor(j,3-j,'X')) break;
    else
    {
        if(re[j][3-j]=='T') c++;
    }
    if(j>=4&&c<2) X = 1;
}
int main()
{
    //#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w+",stdout);
    //#endif
    int cas,T=1;
    scanf("%d",&cas);
    while(cas--)
    {
        X = O = 0;dr = 0;
        for(int i=0;i<4;i++) scanf("%s",re[i]);
        solve();
        printf("Case #%d: ",T++);
        if(X) printf("X won\n");
        else if(O) printf("O won\n");
        else if(dr) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
