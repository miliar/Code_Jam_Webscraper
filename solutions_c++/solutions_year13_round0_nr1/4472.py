
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

char squ[10][10];
int t,ans,cc,rec=0,tot=0;

int calc(char a, char b, char c, char d)
{
    int x,o,tt;
    x=(a=='X')+(b=='X')+(c=='X')+(d=='X');
    o=(a=='O')+(b=='O')+(c=='O')+(d=='O');
    tt=(a=='T')+(b=='T')+(c=='T')+(d=='T');
    if (x==4 || (x==3 && tt==1)) return -1;
    if (o==4 || (o==3 && tt==1)) return 1;
    tot++;
    return 0;
}

int main()
{
    int i,j;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    while (t--)
    {
        rec++;
        cc=0; tot=0;
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++)
            {
                cin>>squ[i][j];
                while (squ[i][j]!='.' && squ[i][j]!='T' && squ[i][j]!='X' && squ[i][j]!='O')
                    cin>>squ[i][j];
                cc+=(squ[i][j]=='.');
            }
        ans=calc(squ[1][1],squ[2][2],squ[3][3],squ[4][4])+calc(squ[1][4],squ[2][3],squ[3][2],squ[4][1]);
        for (i=1; i<=4; i++)
        {
            ans+=calc(squ[1][i],squ[2][i],squ[3][i],squ[4][i])+calc(squ[i][1],squ[i][2],squ[i][3],squ[i][4]);
        }
        if (ans>0) printf("Case #%d: O won\n",rec);
        if (ans<0) printf("Case #%d: X won\n",rec);
        if (ans==0 && tot==10)
        {
            if (cc) printf("Case #%d: Game has not completed\n",rec);
                else printf("Case #%d: Draw\n",rec);
        }
    }
    return 0;
}
