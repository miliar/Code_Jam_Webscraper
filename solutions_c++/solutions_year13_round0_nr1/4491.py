#include <iostream>
#include <sstream>
#include <cstdio>
#include <map>
using namespace std;
char ch[5][5];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for (int icase=1; icase<=T; icase++)
    {
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                cin >> ch[i][j];
        cout << "Case #" << icase << ": ";
        int ans=0;
        for (int i=0; !ans && i<4; i++)
        {
            int flagx=1,flago=1;
            for (int j=0; j<4; j++)
            {
                if (ch[i][j]!='X' && ch[i][j]!='T') flagx=0;
                if (ch[i][j]!='O' && ch[i][j]!='T') flago=0;
            }
            if (flagx) {ans=1;break;}
            if (flago) {ans=2;break;}
        }
        for (int j=0; !ans && j<4; j++)
        {
            int flagx=1,flago=1;
            for (int i=0; i<4; i++)
            {
                if (ch[i][j]!='X' && ch[i][j]!='T') flagx=0;
                if (ch[i][j]!='O' && ch[i][j]!='T') flago=0;
            }
            if (flagx) {ans=1;break;}
            if (flago) {ans=2;break;}
        }
        int flagxx=1,flagoo=1;
        for (int i=0; i<4; i++)
        {
            if (ch[i][i]!='X' && ch[i][i]!='T') flagxx=0;
            if (ch[i][i]!='O' && ch[i][i]!='T') flagoo=0;
        }
        if (flagxx) {ans=1;}
        if (flagoo) {ans=2;}
        flagxx=1;flagoo=1;
        for (int i=0; i<4; i++)
        {
            if (ch[i][3-i]!='X' && ch[i][3-i]!='T') flagxx=0;
            if (ch[i][3-i]!='O' && ch[i][3-i]!='T') flagoo=0;
        }
        if (flagxx) {ans=1;}
        if (flagoo) {ans=2;}
        if (ans==1) cout << "X won" << endl;
        else if (ans==2) cout << "O won" << endl;
        else
        {
            int flag=1;
            for (int i=0; i<4; i++)
                for (int j=0; j<4; j++)
                    if (ch[i][j]=='.') flag=0;
            if (flag) cout << "Draw" << endl;
            else cout << "Game has not completed" << endl;
        }


    }
}
