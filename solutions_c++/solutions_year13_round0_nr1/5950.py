#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;
int main ()
{
    freopen("read.in","r",stdin);
    freopen("write.txt","w",stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        string s[5];
        for (int i=0;i<4;i++)
            cin >> s[i];

        printf("Case #%d: ",t);
        int nX,nO,nT;

        for (int i=0;i<4;i++)
        {
            nX = nO = nT = 0;
            for (int j=0;j<4;j++)
            {
                if (s[i][j]=='T') nT++;
                else if (s[i][j]=='X') nX++;
                else if (s[i][j]=='O') nO++;
            }
            if (nX+nT==4 || nO+nT==4) break;
        }
        if (nX+nT==4)
        {
            cout << "X won\n";
            continue;
        }
        if (nO+nT==4)
        {
            cout << "O won\n";
            continue;
        }

        for (int i=0;i<4;i++)
        {
            nX = nO = nT = 0;
            for (int j=0;j<4;j++)
            {
                if (s[j][i]=='T') nT++;
                else if (s[j][i]=='X') nX++;
                else if (s[j][i]=='O') nO++;
            }
            if (nX+nT==4 || nO+nT==4) break;
        }
        if (nX+nT==4)
        {
            cout << "X won\n";
            continue;
        }
        if (nO+nT==4)
        {
            cout << "O won\n";
            continue;
        }

        nX = nO = nT = 0;

        for (int i=0;i<4;i++)
        {
            if (s[i][i]=='T') nT++;
            else if (s[i][i]=='X') nX++;
            else if (s[i][i]=='O') nO++;
        }

        if (nX+nT==4)
        {
            cout << "X won\n";
            continue;
        }
        if (nO+nT==4)
        {
            cout << "O won\n";
            continue;
        }


        nX = nO = nT = 0;

        for (int i=0,j=3;i<4;i++,j--)
        {
            if (s[i][j]=='T') nT++;
            else if (s[i][j]=='X') nX++;
            else if (s[i][j]=='O') nO++;
        }

        if (nX+nT==4)
        {
            cout << "X won\n";
            continue;
        }
        if (nO+nT==4)
        {
            cout << "O won\n";
            continue;
        }

        bool f=0;

        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
                if (s[i][j]=='.') {f=1; break;}
            if (f) break;
        }
        f? cout << "Game has not completed\n" : cout << "Draw\n";
    }
    return 0;
}


