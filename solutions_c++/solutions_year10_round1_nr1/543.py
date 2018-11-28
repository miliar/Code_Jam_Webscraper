#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int grid[100][100];

int N, K;
char map[100][100], rot[100][100];

char checkh(int ii, int jj)
{
    char first = rot[ii][jj];
    if (first == '.') return '.';
    for (int j = jj + 1; j <= jj + K - 1; ++j)
        if (rot[ii][j] != first) return '.';
    return first;
}

char checkv(int ii, int jj)
{
    char first = rot[ii][jj];
    if (first == '.') return '.';
    for (int i = ii + 1; i <= ii + K - 1; ++i)
        if (rot[i][jj] != first) return '.';
    return first;
}

char checkd1(int ii, int jj)
{
    char first = rot[ii][jj];
    if (first == '.') return '.';
    int i, j;
    for (i = ii + 1, j = jj + 1; j <= jj + K - 1; ++i, ++j)
        if (rot[i][j] != first) return '.';
    return first;
}

char checkd2(int ii, int jj)
{
    if (jj - K + 1 < 0) return '.';
    char first = rot[ii][jj];
    if (first == '.') return '.';
    int i, j;
    for (i = ii + 1, j = jj - 1; i <= ii + K - 1; ++i, --j)
        if (rot[i][j] != first) return '.';
    return first;
}

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void solve()
{
    fin >> N >> K;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
        {
            char c;
            fin >> c;
            map[i][j] = c;
        }

    for (int i = 0; i < 100; ++i)
        for (int j = 0; j < 100; ++j)
            rot[i][j] = '.';

    for (int i = N - 1; i >=0; --i)
    {
        int p = 0;
        for (int j = N-1; j >=0; --j)
            if (map[i][j] != '.')
                rot[N - i - 1][p++] = map[i][j];
    }

    bool winred = 0, winblue = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
        {
            char temp1 = checkh(i, j);
            char temp2 = checkv(i, j);
            char temp3 = checkd1(i, j);
            char temp4 = checkd2(i, j);

            if (temp1 == 'R') winred = 1;
            if (temp2 == 'R') winred = 1;
            if (temp3 == 'R') winred = 1;
            if (temp4 == 'R') winred = 1;

            if (temp1 == 'B') winblue = 1;
            if (temp2 == 'B') winblue = 1;
            if (temp3 == 'B') winblue = 1;
            if (temp4 == 'B') winblue = 1;
        }

    string ans;
    if (winred && winblue)
        ans = "Both";
    else if (winred)
        ans = "Red";
    else if (winblue)
        ans = "Blue";
    else
        ans = "Neither";

    fout << ans << endl;
}

int main()
{
    int T;
    fin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        fout << "Case #" << cas << ": ";
        solve();
    }

    fin.close();
    fout.close();
    return 0;
}
