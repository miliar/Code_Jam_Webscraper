#include <iostream>
#include <string>

using namespace std;

char table[10][10];
int XcntCol[10], OcntCol[10], XcntRow[10], OcntRow[10];
int main()
{
    int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
        for (int i = 0; i < 4; i++)
        {
            XcntCol[i] = XcntRow[i] = OcntCol[i] = OcntRow[i] = 0;
            for (int j = 0; j < 4; j++)
                cin >> table[i][j];
        }
        cout << "Case #" << tt + 1 << ": ";
        bool empty = false;
        int XmainDiagon = 0, XsecDiagon = 0, OmainDiagon = 0, OsecDiagon = 0;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (table[i][j] == 'T')
                {
                    XcntCol[j]++;
                    OcntCol[j]++;
                    XcntRow[i]++;
                    OcntRow[i]++;
                    if (i == j)
                    {
                        XmainDiagon++;
                        OmainDiagon++;
                    }
                    if (i == 3 - j)
                    {
                        XsecDiagon++;
                        OsecDiagon++;
                    }
                }
                else if (table[i][j] == 'X')
                {
                    XcntCol[j]++;
                    XcntRow[i]++;
                    if (i == j)
                        XmainDiagon++;
                    if (i == 3 - j)
                        XsecDiagon++;
                }
                else if (table[i][j] == 'O')
                {
                    OcntCol[j]++;
                    OcntRow[i]++;
                    if (i == j)
                        OmainDiagon++;
                    if (i == 3 - j)
                        OsecDiagon++;
                }
                else
                    empty = true;
        bool breaked = false;
        if (XmainDiagon == 4 || XsecDiagon == 4)
        {
            cout << "X won" << endl;
            continue;
        }
        if (OmainDiagon == 4 || OsecDiagon == 4)
        {
            cout << "O won" << endl;
            continue;
        }
        for (int i = 0; i < 4; i++)
        {
            if (XcntCol[i] == 4 || XcntRow[i] == 4)
            {
                cout << "X won" << endl;
                breaked = true;
                break;
            }
            if (OcntCol[i] == 4 || OcntRow[i] == 4)
            {
                cout << "O won" << endl;
                breaked = true;
                break;
            }
        }
        if (!breaked)
            if (empty)
                cout << "Game has not completed" << endl;
            else
                cout << "Draw" << endl;

    }
}
