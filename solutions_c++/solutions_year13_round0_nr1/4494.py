#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;
typedef long double ld;
char a[4][4];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        bool f1=false,f2=false,fr=false;
        bool x_d=true,o_d=true,x_rd=true,o_rd=true;
        for(int i=0;i<4;i++)
        {
            bool x_str=true,o_str=true,x_col=true,o_col=true;
            if (a[i][i]=='O' || a[i][i]=='.')
                x_d=false;
            if (a[i][i]=='X' || a[i][i]=='.')
                o_d=false;
            if (a[i][3-i]=='O' || a[i][3-i]=='.')
                x_rd=false;
            if (a[i][3-i]=='X' || a[i][3-i]=='.')
                o_rd=false;
            for(int j=0;j<4;j++)
            {
                if (a[i][j]=='O' || a[i][j]=='.')
                    x_str=false;
                if (a[i][j]=='X' || a[i][j]=='.')
                    o_str=false;
                if (a[j][i]=='O' || a[j][i]=='.')
                    x_col=false;
                if (a[j][i]=='X' || a[j][i]=='.')
                    o_col=false;
                if (a[i][j]=='.')
                    fr=true;
            }
            if (x_str || x_col)
                f1=true;
            else if (o_str || o_col)
                f2=true;
        }
        cout<<"Case #"<<q<<": ";
        if (f1 || x_d || x_rd)
            cout<<"X won\n";
        else if (f2 || o_d || o_rd)
            cout<<"O won\n";
        else if (!fr)
            cout<<"Draw\n";
        else
            cout<<"Game has not completed\n";
    }
    return 0;
}
