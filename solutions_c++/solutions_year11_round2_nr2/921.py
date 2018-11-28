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
#include <iomanip>

#define MAX 222
#define FILE_IN "bsmall1.in"
#define FILE_OUT "output.txt"
#define EPS 0.00000001
#define MLEN 1100000000000

using namespace std;

double d;
int c, t;
double pos[MAX];
int num[MAX];
double st[MAX];
double end[MAX];
double mintime[MAX];

int cal(int x)
{
    double length;

    {
        length = (num[x] - 1) * d;
    }
    mintime[x] = length/2;
    st[x] = pos[x] - mintime[x];
    end[x] = pos[x] + mintime[x] + d;
    cout << st[x] << " " << end[x] <<  " " << mintime[x] << endl;
}

bool check(double len)
{
    double curr = -1e13;
    bool debug = 0;
    double allow;
    if (fabs(len - 6.5) < EPS) debug = 1;
    for (int i=0; i<c; i++)
    {
        if (debug) cout << curr << endl;
        allow = len - mintime[i];
        if (st[i] - allow >= curr)
        {
            curr = end[i] - allow;
        }
        else if (st[i] >= curr)
        {
            curr = end[i] - (st[i] - curr);
        }
        else if (st[i] < curr)
        {
            if (curr - st[i] > allow) return false;
            curr = end[i] + (curr - st[i]);
        }
    }
    return true;
}

double solve()
{
    double left = 0;
    for (int i=0; i<c; i++)
    {
        cal(i);
        if (mintime[i] > left) left = mintime[i];
    }

    double right = 1e13;
    double mid;
    double res;
    double tres;

    while (left < right)
    {
        mid = (left + right) / 2;
        if (check(mid))
        {
            res = mid;
            right  = mid - EPS;
        }
        else
        {
            left = mid + EPS;
        }
    }
    return res;
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int tcase = 1; tcase <= t; tcase++)
    {
        cin >> c >> d;
        for (int i=0; i<c; i++)
        {
            cin >> pos[i] >> num[i];
        }
        fout << "Case #" << tcase << ": ";
        fout.setf(ios::fixed);
        fout.precision(7);
        fout << solve() << endl;
    }

    fout.close();
    cin.close();
}
