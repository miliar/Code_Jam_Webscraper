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

#define FILE_IN "blarge.in"
#define FILE_OUT "output.txt"

#define MAX 1011
#define MAXD 1000011

using namespace std;

long long t, c, n, l, tme;
long long a[MAX];
long long d[MAXD];
long long rem[MAXD];

long long convert()
{
    for (long long i=0; i<n; i++)
    {
        d[i] = a[i%c] * 2;
        //cout << d[i] << " ";
    }
    //cout << endl;
}

long long solve()
{
    long long sum = 0;
    long long st = 0;
    while (st < n && sum < tme)
    {
        sum += d[st];
        st++;
    }
    //cout << sum << endl;

    if (st == n && sum <= tme)
    {
        return sum;
    }

    rem[0] = sum - tme;
    sum = tme;
    //cout << rem [0] << " ";
    long long count = 1;
    for (long long i=st; i<n; i++)
    {
        rem[count] = d[i];
        //cout << rem[i] << " ";
        count++;
    }
    //cout << endl;

    sort(rem, rem+count);
    for (long long i=count-1; i>=0; i--)
    {
        if (l>0)
        {
            rem[i] /= 2;
            l--;
        }
        //cout << rem[i] << " ";
        sum += rem[i];
    }
    //cout << endl;

    return sum;
}

int main()
{
    ifstream cin (FILE_IN);
    ofstream fout (FILE_OUT);

    cin >> t;
    for (long long tcase = 1; tcase <= t; tcase++)
    {
        cin >> l >> tme >> n >> c;
        for (long long i=0; i<c; i++)
        {
            cin >> a[i];
        }
        convert();

        fout << "Case #" << tcase << ": ";
        fout << solve() << endl;
    }

    cin.close();
    fout.close();
}
