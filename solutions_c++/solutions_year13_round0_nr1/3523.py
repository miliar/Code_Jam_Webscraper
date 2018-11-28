#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#define mp make_pair
#define ll long long
#define s second
#define f first
#define pii pair<int,int>
#define pll pair<ll,ll>
using namespace std;
const ll c=2000,inf=2000000000ll;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    char q[6][6];
    cin>>t;
    for (int u=1; u<=t; u++)
    {
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                cin>>q[i][j];
        int win=-1,p=0;
        for (int j=0; j<4; j++)
        {
            int x=0,y=0,z=0;
            for (int i=0; i<4; i++)
                if (q[i][j]=='X')
                   x++;
                else if (q[i][j]=='O')
                        y++;
                else if (q[i][j]=='T')
                        z++;
                else p=1;
            if (x+z==4)
               win=0;
            if (y+z==4)
               win=1;
        }
        for (int i=0; i<4; i++)
        {
            int x=0,y=0,z=0;
            for (int j=0; j<4; j++)
                if (q[i][j]=='X')
                   x++;
                else if (q[i][j]=='O')
                        y++;
                else if (q[i][j]=='T')
                        z++;
                else p=1;
            if (x+z==4)
               win=0;
            if (y+z==4)
               win=1;
        }
        int x,y,z;
        x=y=z=0;
        for (int i=0; i<4; i++)
            if (q[i][i]=='X')
               x++;
            else if (q[i][i]=='O')
                    y++;
            else if (q[i][i]=='T')
                    z++;
            else p=1;
        if (x+z==4)
           win=0;
        if (y+z==4)
           win=1;
        x=y=z=0;
        for (int i=0; i<4; i++)
            if (q[i][3-i]=='X')
               x++;
            else if (q[i][3-i]=='O')
                    y++;
            else if (q[i][3-i]=='T')
                    z++;
            else p=1;
        if (x+z==4)
           win=0;
        if (y+z==4)
           win=1;
        if (win==-1)
           if (p)
              printf("Case #%d: Game has not completed\n",u);
           else printf("Case #%d: Draw\n",u);
        else if (win==0)
                printf("Case #%d: X won\n",u);
        else printf("Case #%d: O won\n",u);
    }
    //system("pause");
    return 0;
}
