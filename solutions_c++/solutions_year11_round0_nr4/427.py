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

#define FILE_IN "dlarge.in"
#define FILE_OUT "output.txt"

#define MAX 1111

using namespace std;

int per[MAX];
int d[MAX];
int t, n;

void input(istream &cin)
{
    cin >> n;
    for (int i=1; i<=n; i++)
    {
        cin >> per[i];
    }
}

double solve()
{
    memset(d, 0, sizeof(d));
    double ans = 0;
    for (int i=1; i<=n; i++)
    {
        if (d[i] == 0)
        {
            int cur = i;
            int count = 1;
            while (per[cur] != i)
            {
                d[cur] = 1;
                cur = per[cur];
                count ++;
            }
            d[cur] = 1;
            //cout << i << " " << count << endl;
            if (count>1) ans += count;
        }
    }
    //cout << "-----" << ans << endl;
    return ans;
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int i=1; i<=t; i++)
    {
        input(cin);
        fout << "Case #" << i << ": " << solve() << endl;
    }

    fout.close();
    cin.close();
}
