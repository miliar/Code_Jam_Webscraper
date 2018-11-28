#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define rep(i,n) for(int i=0;i<n;i++)
#define A frist
#define B second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;
char s[5][5];

int cc(int i,int j,char c)
{
    if(s[i][j]==c || s[i][j]=='.')return 1;
    return 0;
}
int f(char c)
{
    for(int i=0; i<4; i++)
    {
        int flag=0;
        for(int j=0; j<4; j++)
        {
            if(s[i][j]==c || s[i][j]=='.')
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            return 1;
        }
    }
    if(cc(0,0,c) || cc(1,1,c) || cc(2,2,c) || cc(3,3,c));
    else return 1;
    if(cc(0,3,c) || cc(1,2,c) || cc(2,1,c) || cc(3,0,c));
    else return 1;

    return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_large_out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    rep(cas,T)
    {
        rep(i,4)scanf("%s",s[i]);

        printf("Case #%d: ",cas+1);
        if(f('O')){puts("X won");continue;}
        rep(i,4)for(int j=i+1;j<4;j++)swap(s[i][j],s[j][i]);
        if(f('O')){puts("X won");continue;}
        rep(i,4)for(int j=i+1;j<4;j++)swap(s[i][j],s[j][i]);
        if(f('X')){puts("O won");continue;}
        rep(i,4)for(int j=i+1;j<4;j++)swap(s[i][j],s[j][i]);
        if(f('X')){puts("O won");continue;}
        int cnt=0;
        rep(i,4)rep(j,4)if(s[i][j]=='.')cnt++;
        if(cnt>0)puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}



