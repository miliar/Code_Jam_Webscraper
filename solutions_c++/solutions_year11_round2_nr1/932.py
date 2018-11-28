///PROBLEM NAME
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>

#define MAX 200
#define FILE_IN "alarge.in"
#define FILE_OUT "output.txt"

using namespace std;

int t, n;
int resboard[MAX][MAX];
int win[MAX];
int play[MAX];
double wp[MAX];
double owp[MAX];
double oowp[MAX];

double calwp(int x)
{
    win[x] = 0;
    play[x] = 0;
    for (int i=0; i<n; i++)
    {
        if (resboard[x][i] != -1) play[x]++;
        if (resboard[x][i] == 1) win[x]++;
    }
    return (double)win[x]/play[x];
}

double calwpwo(int x, int y)
{
    int pl = play[x] - 1;
    if (pl == 0) return 0;
    int wpl = win[x] - resboard[x][y];

    return (double) wpl/pl;
}

double calowp(int x)
{
    double sum = 0;
    for (int i=0; i<n; i++)
    {
        if (resboard[x][i] != -1)
            sum += calwpwo(i, x);
    }
    return sum / play[x];
}

double caloowp(int x)
{
    double sum = 0;
    for (int i=0; i<n; i++)
    {
        if (resboard[x][i] != -1)
            sum += owp[i];
    }
    return sum/play[x];
}

double rpi(int x)
{
    return (0.25 * wp[x] + 0.5 * owp[x] + 0.25 * oowp[x]);
}

int solve(ostream &fout)
{
    for (int i=0; i<n; i++)
    {
        wp[i] = calwp(i);
    }
    for (int i=0; i<n; i++)
    {
        owp[i] = calowp(i);
    }
    for (int i=0; i<n; i++)
    {
        oowp[i] = caloowp(i);
    }
    for (int i=0; i<n; i++)
    {
        fout << rpi(i) << endl;
    }
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int tcase = 1; tcase <= t; tcase++)
    {
        cin >> n;
        char c;
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<n; j++)
            {
                cin >> c;
                switch(c)
                {
                    case '.':
                        resboard[i][j] = -1;
                        break;
                    case '1':
                        resboard[i][j] = 1;
                        break;
                    case '0':
                        resboard[i][j] = 0;
                        break;
                }
            }
        }
        fout << "Case #" << tcase << ":\n";
        solve(fout);
    }

    fout.close();
    cin.close();
}
