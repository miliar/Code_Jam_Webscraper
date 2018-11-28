#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#define nabs(x) (x)<0?(-(x)):(x)
#define N 55
using namespace std;

char grib[N][N];
bool flag[N][N];
int r, c;

int change()
{
    int i, j;
    memset(flag, false, sizeof(flag));
    for(i = 1; i <= r; ++i)
    {
        for(j = 1; j <= c; ++j)
        {
            if(grib[i][j] == '#')
            {
                if(grib[i - 1][j] == '1')
                {
                    grib[i][j] = '3';
                }
                else if(grib[i - 1][j] == '2')
                {
                    grib[i][j] = '4';
                }
                else if(grib[i][j - 1] == '1')
                {
                    grib[i][j] = '2';
                }
                else
                {
                    grib[i][j] = '1';
                }
            }
        }
    }
    return 0;
}

bool judge()
{
    int i, j;
    int ul, ur, dl, dr;
    ul = ur = dl = dr = 0;
    memset(flag, false, sizeof(flag));
    for(i = 1; i <= r; ++i)
    {
        for(j = 1; j <= c; ++j)
        {
            if(grib[i][j] == '1' && flag[i][j] == false)
            {
                if(grib[i + 1][j] != '3')
                    return false;
                if(grib[i][j + 1] != '2')
                    return false;
                if(grib[i + 1][j + 1] != '4')
                    return false;
                flag[i][j] = flag[i + 1][j] = flag[i][j + 1] = flag[i + 1][j + 1] = true;
            }
        }
    }
    return true;
}

int output()
{
    int i, j;
    for(i = 1; i <= r; ++i)
    {
        for(j = 1; j <= c; ++j)
        {
            switch(grib[i][j])
            {
                case '1':
                    cout << '/';
                    break;
                case '2':
                    cout << '\\';
                    break;
                case '3':
                    cout << '\\';
                    break;
                case '4':
                    cout << '/';
                    break;
                case '.':
                    cout << '.';
                    break;
            }
        }
        cout << endl;
    }
    return 0;
}

int main()
{
    int t, k;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> t;
    for(k = 1; k <= t; ++k)
    {
        printf("Case #%d:\n", k);
        cin >> r >> c;
        int i;
        for(i = 1; i <= r; ++i)
            cin >> (grib[i] + 1);
        change();
        if(!judge())
            cout << "Impossible" << endl;
        else
            output();
    }
    return 0;
}
