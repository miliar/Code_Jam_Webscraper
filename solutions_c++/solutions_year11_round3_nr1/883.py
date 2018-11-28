#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define vi vector <int>
#define rep(i,n) for(int i = 0; i < n; i++)
#define read(a) rep(i, a.size()) cin >> a[i];
#define write(a) rep(i, a.size()) cout << a[i] << ' '; cout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const double eps = 0.000001;

int main()
{
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int count = 1; count <= t; count++)
    {
        cout << "Case #" << count << ": " << endl;
        int r, c;
        cin >> r >> c;
        char a[50][50];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                cin >> a[i][j];
        bool ok = true;
        for (int i = 0; i < r - 1; i++)
            for (int j = 0; j < c - 1; j++)
            {
                if (a[i][j] == '#')
                {
                   if (a[i + 1][j] != '#' || a[i][j + 1] != '#' || a[i + 1][j + 1] != '#')
                      ok = false;
                   else
                   {
                       a[i][j] = a[i + 1][j + 1] = '/';
                       a[i + 1][j] = a[i][j + 1] = '\\';
                   }
                }
            }
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (a[i][j] == '#')
                   ok = false;
        if (!ok)
           cout << "Impossible" << endl;
        else
        {
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++)
                    cout << a[i][j];
                cout << endl;
            }
        }
    }
    return 0;
}








