#include <iostream>
#include <cstdio>

using namespace std;

char a[5][5];

int cnt()
{
    for (int i = 0; i < 4; i++)
    {
        int sumx = 0, sumo = 0;
        for (int j = 0; j < 4; j++)
        {
            if (a[i][j] == 'X')
            {
                sumx++;
            }
            else if (a[i][j] == 'O')
            {
                sumo++;
            }
            else if (a[i][j] == 'T')
            {
                sumx++;
                sumo++;
            }
        }
        if (sumx == 4)
        {
            return 0;
        }
        else if (sumo == 4)
        {
            return 1;
        }
    }

    for (int i = 0; i < 4; i++)
    {
        int sumx = 0, sumo = 0;
        for (int j = 0; j < 4; j++)
        {
            if (a[j][i] == 'X')
            {
                sumx++;
            }
            else if (a[j][i] == 'O')
            {
                sumo++;
            }
            else if (a[j][i] == 'T')
            {
                sumx++;
                sumo++;
            }
        }
        if (sumx == 4)
        {
            return 0;
        }
        else if (sumo == 4)
        {
            return 1;
        }
    }

    int sumx = 0, sumo = 0;

    for (int i = 0; i < 4; i++)
    {
        if (a[i][i] == 'X')
        {
            sumx++;
        }
        else if (a[i][i] == 'O')
        {
            sumo++;
        }
        else if (a[i][i] == 'T')
        {
            sumx++;
            sumo++;
        }
    }

    if (sumx == 4)
    {
        return 0;
    }
    else if (sumo == 4)
    {
        return 1;
    }

    sumx = sumo = 0;


    for (int i = 0; i < 4; i++)
    {
        if (a[3 - i][i] == 'X')
        {
            sumx++;
        }
        else if (a[3 - i][i] == 'O')
        {
            sumo++;
        }
        else if (a[3 - i][i] == 'T')
        {
            sumx++;
            sumo++;
        }
    }

    if (sumx == 4)
    {
        return 0;
    }
    else if (sumo == 4)
    {
        return 1;
    }

    int sm = 0;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (a[i][j] == '.')
            {
                sm++;
            }
        }
    }
    if (sm == 0)
    {
        return 2;
    }
    return 3;

}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> a[j][k];
            }
        }
        int p = cnt();
        cout << "Case #" << i + 1 << ": ";
        if (p == 0)
        {
            cout << "X won" << endl;
        }
        else if (p == 1)
        {
            cout << "O won" << endl;
        }
        else if (p == 2)
        {
            cout << "Draw" << endl;
        }
        else
        {
            cout << "Game has not completed" << endl;
        }
    }

    return 0;
}
