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

#define FILE_IN "test.txt"
#define FILE_OUT "output.txt"

using namespace std;

long long d, g;
long long pd, pg;
long long xd, xg;
long long yd, yg;
long long n, t;

long long gcd(long long x, long long y)
{
    if (x%y == 0) return y;
    return gcd(y,x%y);
}

int solve()
{
    xd = pd/gcd(pd,100);
    yd = 100/gcd(pd,100);
    xg = pg/gcd(pg,100);
    yg = 100/gcd(pg,100);

    //cout << 1 << endl;
    //cout << n << " " << yd << endl;
    if (n < yd) return 0;


    d = yd;
    //cout << 2 << endl;
    if (pd<100 && pg == 100) return 0;
    //cout << 3 << endl;
    if (pd>0 && pg == 0) return 0;
    //cout << 4 << endl;
    if (pd==100) return 1;
    //cout << 5 << endl;
    //int ming = max(pd*d/pg, (100-pd)*d/(100-pg));
    return 1;
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int tcase = 1; tcase <=t; tcase++)
    {
        cin >> n >> pd >> pg;
        fout << "Case #" << tcase << ": ";
        if (solve()) fout << "Possible\n";
        else fout << "Broken\n";
    }

    fout.close();
    cin.close();
}
