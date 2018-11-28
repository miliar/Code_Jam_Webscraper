///candy splitting
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>
#include <fstream>

#define FILE_IN "C-large.in"
#define FILE_OUT "output.txt"

using namespace std;

int t, n, sum, minc = 99999999, res = 0;

int solve(istream &cin, ostream &fout)
{
    minc = 99999999;
    sum = 0;
    res = 0;

    cin >> n;

    int x;
    for (int i=0; i<n; i++)
    {
        cin >> x;
        minc = min(minc, x);
        sum += x;
        res = res ^ x;
       //  cout << res << endl;
    }

    if (res != 0)
    {
        fout << "NO";
        return 0;
    }
    fout << sum-minc;
    return 0;
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int i=1; i<=t; i++)
    {
        fout << "Case #" << i << ": ";
        solve(cin, fout);
        fout << endl;
    }

    fout.close();
    cin.close();
}
