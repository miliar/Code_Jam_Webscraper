#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

bool fulfill(string mp[])
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (mp[i][j] == '.')
                return false;
    return true;
}

bool line(string s, char symbol)
{
    for (int i = 0; i < 4; i++)
        if (s[i] != symbol && s[i] != 'T')
            return false;
    return true;
}
bool judge(string mp[], char symbol)
{
    string tmp = "    ";
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
            tmp[j] = mp[i][j];
        if (line(tmp, symbol))
            return true;

        for (int j = 0; j < 4; j++)
            tmp[j] = mp[j][i];
        if (line(tmp, symbol))
            return true;
    }
    for (int i = 0; i < 4; i++)
        tmp[i] = mp[i][i];
    if (line(tmp, symbol))
        return true;

    for (int i = 0; i < 4; i++)
        tmp[i] = mp[i][3 - i];
    if (line(tmp, symbol))
        return true;

    return false;
}

int main()
{
    int n;
    string mp[4];
    cin >> n;
    for (int cs = 1; cs <= n; cs++)
    {
        for (int i = 0; i < 4; i++)
        {
            cin >> mp[i];
        }
        if (judge(mp, 'X'))
        {
            cout << "Case #" << cs << ": X won" << endl;
        }
        else if (judge(mp, 'O'))
        {
            cout << "Case #" << cs << ": O won" << endl;
        }
        else if (fulfill(mp))
        {
            cout << "Case #" << cs << ": Draw" << endl;
        }
        else
        {
            cout << "Case #" << cs << ": Game has not completed" << endl;
        }
    }
    return 0;
}
