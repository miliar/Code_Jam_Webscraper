#include <iostream>
#include <string.h>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <limits.h>
#include <vector>
#include <string>
#include <ctype.h>
#include <complex>
#include <cmath>
using namespace             std;
const int                   Maxn=600,Maxm=2500000,Mo=1000000007,oo=INT_MAX;
struct F {
    int c1,c2,b;
};
int                         cs,cx,co;
char                        mp[Maxn][Maxn];
int main()
{
    ios::sync_with_stdio(0);
//    freopen("/Users/MAC/Desktop/Error202/Error202/1.in","r",stdin);
//    freopen("/Users/MAC/Desktop/Error202/Error202/1.out","w",stdout);
    cin>>cs;
    int tt=0;
    while (cs--)
    {
        cout<<"Case #"<<++tt<<": ";
        int ck=0,yy=0;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        {
            cin>>mp[i][j];
            if(mp[i][j]=='.') ck=1;
        }
        for(int i=1;i<=4;i++)
        {
            cx=co=0;
            for (int j=1;j<=4;j++)
            {
                if (mp[i][j]=='X') cx++;
                else if (mp[i][j]=='T') cx++,co++;
                else if(mp[i][j]=='O') co++;
                if (cx==4) {cout<<"X won\n"; yy=1;break;}
                if (co==4) {cout<<"O won\n"; yy=1;break;}
            }
            if (yy) break;
        }
        if(yy) continue;
        for(int i=1;i<=4;i++)
        {
            cx=co=0;
            for (int j=1;j<=4;j++)
            {
                if (mp[j][i]=='X') cx++;
                else if (mp[j][i]=='T') cx++,co++;
                else if(mp[j][i]=='O') co++;
                if (cx==4) {cout<<"X won\n"; yy=1;break;}
                if (co==4) {cout<<"O won\n"; yy=1;break;}
            }
            if (yy) break;
        }
        if(yy) continue;
        cx=co=0;
        for (int i=1;i<=4;i++)
            if (mp[i][i]=='X') cx++;
            else if (mp[i][i]=='T') cx++,co++;
            else if(mp[i][i]=='O') co++;
        if (cx==4) {cout<<"X won\n"; continue;}
        if (co==4) {cout<<"O won\n"; continue;}
        cx=co=0;
        for (int i=1;i<=4;i++)
            if (mp[i][4-i+1]=='X') cx++;
            else if (mp[i][4-i+1]=='T') cx++,co++;
            else if(mp[i][4-i+1]=='O') co++;
        if (cx==4) {cout<<"X won\n"; continue;}
        if (co==4) {cout<<"O won\n"; continue;}
        if(!ck) cout<<"Draw\n";
        else cout<<"Game has not completed\n";
        
    }
}