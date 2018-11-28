#include <iostream>
#include <fstream>
using namespace std;

int main(int argc,char ** argv)
{

    int tcase;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin >> tcase;
    char a[4][4];
    for (int t=0; t<tcase; t++)
    {

        cout << "Case #" << t+1 << ": "; 
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
                cin >> a[i][j];
        }

        char cur;
        bool flag=false;
        for (int i=0; i<4; i++)
        {
            cur=a[i][0];
            if (cur=='T')
                cur == a[i][1];
            if (cur=='X' || cur =='O')
            {
                int j=1;
                while (j<4 && (a[i][j]==cur || a[i][j]=='T'))
                    j++;
                if (j==4)
                {
                    cout << cur << " won" << endl;
                    flag=true;
                    break;
                }
            }
        }
        if (flag)
            continue;
        for (int j=0; j<4; j++)
        {
            cur=a[0][j];
            if (cur=='T')
                cur == a[1][j];

            if (cur=='X' || cur =='O')
            {
                int i=1;
                while (i<4 && (a[i][j]==cur || a[i][j]=='T'))
                    i++;
                if (i==4)
                {
                    cout << cur << " won" << endl;
                    flag=true;
                    break;
                }
            }
        }
        if (flag)
            continue;
            cur=a[0][0];
            if (cur=='T')
                cur == a[1][1];
            if (cur=='X' || cur =='O')
            {
                int i=1;
                while (i<4 && (a[i][i]==cur || a[i][i]=='T'))
                    i++;
                if (i==4)
                {
                    cout << cur << " won" << endl;
                    flag=true;
                }
            }
        if (flag)
            continue;

        cur=a[0][3];
            if (cur=='T')
                cur == a[1][2];
            if (cur=='X' || cur =='O')
            {
                int i=1;
                while (i<4 && (a[i][3-i]==cur || a[i][3-i]=='T'))
                    i++;
                if (i==4)
                {
                    cout << cur << " won" << endl;
                    flag=true;
                }
            }
        if (flag)
            continue;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
                if (a[i][j]=='.')
                {
                    cout << "Game has not completed"<< endl;
                    flag=true;
                    break;
                }
            if (flag)
                break;
        }
        if (flag)
            continue;
        cout << "Draw" << endl;
    }
    return 0;
}
