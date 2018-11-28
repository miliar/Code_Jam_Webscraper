// google code jam A

#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

const int MAXN = 110;

int list[2][MAXN], n;

int absol(int x)
{
    return x > 0 ? x : -x;
}

int solve()
{
    int pos[2] = {1, 1}, ans = 0;
    for (int i = 1; i <= n; i++)
    {
        int flag = -1, role = list[1][i];
        for (int j = i + 1; j <= n; j++)
            if (list[1][i] != list[1][j])
            {
                flag = j;
                break;
            }
        int temp = 1 + absol(list[0][i] - pos[role]);
        pos[role] = list[0][i], ans += temp;
        if (flag > 0)
        {
            int wantT = absol(list[0][flag] - pos[1 - role]), dir;
            if (list[0][flag] > pos[1 - role])
                dir = 1;
            else
                dir = -1;
            pos[1 - role] += wantT < temp ? dir * wantT : dir * temp;
        }
    }
    return ans;
}

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::in);
    ofstream fout("aout.txt", ios::out);
    int testcase;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> n;
        for (int i = 1; i <= n; i++)
        {
            char ch;
            fin >> ch >> list[0][i];
            list[1][i] = ch == 'O' ? 0 : 1;
        }
        fout << "Case #" << test << ": " << solve() << endl;
    }
    fout.close();
    fin.close();
    return 0;
}






