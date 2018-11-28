#include <iostream>
#include <stdio.h>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int i,j,k;
    char a[4][4];
    bool x,o,ciao;

    cin>>T;t=1;
    while (T--)
    {
        x=0;o=0;ciao=0;

        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
            {
                cin>>a[i][j];
                if (a[i][j]=='.') ciao=1;
            }


        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
                if (a[i][j]=='O' || a[i][j]=='.') break;

            if (j==4) {x=1;break;}
        }

        for (j=0;j<4;j++)
        {
            for (i=0;i<4;i++)
                if (a[i][j]=='O' || a[i][j]=='.') break;

            if (i==4) {x=1;break;}
        }

        if ((a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T')) x=1;
        if ((a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X' || a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X' || a[3][0]=='T')) x=1;

        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
                if (a[i][j]=='X' || a[i][j]=='.') break;

            if (j==4) {o=1;break;}
        }

        for (j=0;j<4;j++)
        {
            for (i=0;i<4;i++)
                if (a[i][j]=='X' || a[i][j]=='.') break;

            if (i==4) {o=1;break;}
        }

        if ((a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T')) o=1;
        if ((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O' || a[3][0]=='T')) o=1;

        cout<<"Case #"<<t<<": ";
        if (x) cout<<"X won"<<endl;
        else if (o) cout<<"O won"<<endl;
        else if (ciao) cout<<"Game has not completed"<<endl;
        else cout<<"Draw"<<endl;

        t++;
    }

    return 0;
}
