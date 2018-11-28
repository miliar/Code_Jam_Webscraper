#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;

bool g_eflag;

int func2(char c)
{
    int ret = 0;
    switch (c)
    {
    case 'X':
        ret = 1;
        break;
    case 'O':
        ret = 2;
        break;
    case '.':
        ret = 3;
        break;
    case 'T':
        ret = 4;
        break;
    }
    return ret;
}

int func(char c1, char c2, char c3, char c4)
{
    int x = 0;
    int o = 0;
    int e = 0;
    int t = 0;
    
    switch (func2(c1))
    {
    case 1:
        x++;
        break;
    case 2:
        o++;
        break;
    case 3:
        e++;
        break;
    case 4:
        t++;
        break;
    }
    switch (func2(c2))
    {
    case 1:
        x++;
        break;
    case 2:
        o++;
        break;
    case 3:
        e++;
        break;
    case 4:
        t++;
        break;
    }
    switch (func2(c3))
    {
    case 1:
        x++;
        break;
    case 2:
        o++;
        break;
    case 3:
        e++;
        break;
    case 4:
        t++;
        break;
    }
    switch (func2(c4))
    {
    case 1:
        x++;
        break;
    case 2:
        o++;
        break;
    case 3:
        e++;
        break;
    case 4:
        t++;
        break;
    }

    if (e >= 1)
    {
        g_eflag = true;
        return 0;
    }
    if (t >= 2)
    {
        return 0;
    }
    if ((x == 4)
        || (x == 3 && t == 1))
    {
        return 1;
    }
    if ((o == 4)
        || (o == 3 && t == 1))
    {
        return 2;
    }

    return 0;
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int f;

    int T;
    fin >> T;
    char t[4][4];
    for (int j = 0; j < T; j++)
    {
        g_eflag = false;
        string ret = "Draw";
        for (int i = 0; i < 4; i++)
        {
            fin >> t[i][0] >> t[i][1] >> t[i][2] >> t[i][3];
        }

        for (int i = 0; i < 4; i++)
        {
            f = func(t[i][0], t[i][1], t[i][2], t[i][3]);
            if (f == 1)
            {
                ret = "X won";
            }
            else if (f == 2)
            {
                ret = "O won";
            }
        }
        for (int i = 0; i < 4; i++)
        {
            f = func(t[0][i], t[1][i], t[2][i], t[3][i]);
            if (f == 1)
            {
                ret = "X won";
            }
            else if (f == 2)
            {
                ret = "O won";
            }
        }

        f = func(t[0][0], t[1][1], t[2][2], t[3][3]);
        if (f == 1)
        {
            ret = "X won";
        }
        else if (f == 2)
        {
            ret = "O won";
        }

        f = func(t[0][3], t[1][2], t[2][1], t[3][0]);
        if (f == 1)
        {
            ret = "X won";
        }
        else if (f == 2)
        {
            ret = "O won";
        }

        if (ret == "Draw" && g_eflag == true)
        {
            ret = "Game has not completed";
        }

        fout << "Case #" << j+1 << ": " << ret << endl;
    }

    return (0);
}
