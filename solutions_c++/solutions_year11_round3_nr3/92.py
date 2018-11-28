///PROBLEM NAME
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

#define FILE_IN "test.txt"
#define FILE_OUT "output.txt"
#define MAX 10211

using namespace std;

int t;
int n, l, h;
int a[MAX];

bool check(int x)
{
    for (int i=0; i<n; i++)
    {
        if (!(x % a[i] == 0 || a[i] % x == 0))
        {
            return false;
        }
    }
    return true;
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int tcase = 1; tcase <= t; tcase ++)
    {
        cin >> n >> l >> h;
        for (int i=0; i<n; i++)
        {
            cin >> a[i];
        }
        fout << "Case #" << tcase << ": ";
        bool found = false;
        for (int i=l; i<=h; i++)
        {
            if (check(i))
            {
                fout << i << endl;
                found = true;
                break;
            }
        }
        if (!found) fout << "NO\n";
    }

    cin.close();
    fout.close();
}
