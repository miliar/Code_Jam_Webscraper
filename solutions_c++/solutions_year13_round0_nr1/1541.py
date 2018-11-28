#include <fstream>
#include <vector>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int A[4][4];

bool Win(int pl)
{
    int B[4][4];
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            B[i][j] = A[i][j];
            if (B[i][j] == 3)
            {
                B[i][j] = pl;
            }
        }
    }
    int F1 = 1, F2 = 1;
    for (int i = 0; i < 4; ++i)
    {
        if (B[i][i] != pl)
        {
            F1 = 0;
        }
        if (B[i][3 - i] != pl)
        {
            F2 = 0;
        }
        int flag1 = 1, flag2 = 1;
        for (int j = 0; j < 4; ++j)
        {
            if (B[i][j] != pl)
            {
                flag1 = 0;
            }
            if (B[j][i] != pl)
            {
                flag2 = 0;
            }
        }
        if (flag1 || flag2)
        {
            return 1;
        }
    }
    return F1 || F2;
}

int main()
{
    int N;
    cin >> N;
    for (int gh = 0; gh < N; ++gh)
    {
        int flag = 1;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                A[i][j] = 0;
                char c;
                cin >> c;
                if (c == 'T')
                {
                    A[i][j] = 3;
                }
                else if (c == 'O')
                {
                    A[i][j] = 2;
                }
                else if (c == 'X')
                {
                    A[i][j] = 1;
                }
                else
                {
                    A[i][j] = 0;
                    flag = 0;
                }
            }
        }
        cout << "Case #" << gh + 1 << ": ";
        if (Win(1))
        {
            cout << "X won" << endl;
        }
        else if (Win(2))
        {
            cout << "O won" << endl;
        }
        else if (flag)
        {
            cout << "Draw" << endl;
        }
        else
        {
            cout << "Game has not completed" << endl;
        }
    }
}
