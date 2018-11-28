#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#define DBLE 1e-8
#define PI 3.1415926535898
#define INF 1000000000
#define MAXN 1010
#define MP(x,y) (make_pair((x),(y)))
#define FI first
#define SE second
using namespace std;
char ma[10][10],str[10];
int check()
{
    int bel[128]={0};
    for(int i=0;i<4;++i)
        ++bel[str[i]];
    if(bel['X']+bel['T']==4)
        return -1;
    else    if(bel['O']+bel['T']==4)
        return 1;
    else    return 0;
}
int cal(int x,int y)
{
    int flag=0;
    for(int i=0;i<4;++i)
        str[i]=ma[x][i];
    flag=check();
    if(flag!=0)
        return flag;
    for(int i=0;i<4;++i)
        str[i]=ma[i][y];
    return check();
}
int cal2()
{
    int cnt=0;
    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j)
            cnt+=(ma[i][j]!='.');
    return cnt==16?2:3;
}
int main()
{
//    freopen("J:\\MyDocument\\Code\\input.txt","r",stdin);
//    freopen("J:\\MyDocument\\Code\\output.txt","w",stdout);
    int ncase;
    int flag;
    scanf("%d",&ncase);
    for(int h=1;h<=ncase;++h)
    {
        for(int i=0;i<4;++i)
            scanf("%s",ma[i]);
        for(int i=0;i<4;++i)
            str[i]=ma[i][i];
        flag=check();
        if(flag==0)
        {
            for(int i=0;i<4;++i)
                str[i]=ma[i][3-i];
            flag=check();
        }
        for(int i=0;i<4&&flag==0;++i)
            for(int j=0;j<4&&flag==0;++j)
                flag=cal(i,j);
        if(flag==0)
            flag=cal2();
        printf("Case #%d: ",h);
        if(flag==-1)
            printf("X won\n");
        else    if(flag==1)
            printf("O won\n");
        else    if(flag==2)
                printf("Draw\n");
        else    if(flag==3)
                printf("Game has not completed\n");
    }
    return 0;
}

