// google code jam round 2 A

#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

const int MAXN = 1000100;

double len[MAXN], w[MAXN], x, s, r, t;
int n;

void qs(int l, int r)
{
    int i = l, j = r, xx = w[(l + r) >> 1];
    do
    {
        while (i < r && w[i] > xx) i++;
        while (l < j && w[j] < xx) j--;
        if (i <= j)
        {
            double temp = len[i];
            len[i] = len[j];
            len[j] = temp;
            temp = w[i];
            w[i] = w[j];
            w[j] = temp;
            i++, j--;
        }
    } while (i <= j);
    if (i < r)
        qs(i, r);
    if (l < j)
        qs(l, j);
}

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::out);
    ofstream fout("aout.txt", ios::out);
    int testcase;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> x >> s >> r >> t >> n;
        if (r <= s)
            t = 0;
        for (int i = 1; i <= n; i++)
        {
            double b, e;
            fin >> b >> e >> w[i];
            len[i] = e - b;
            x -= len[i];
        }
        n++;
        len[n] = x, w[n] = 0;
        qs(1, n);
        double ans = 0;
        for (int i = n; i > 0; i--)
        {
            double needRun = len[i] / (r + w[i]);
            if (needRun >= t)
            {
                double temp = len[i] - (r + w[i]) * t;
                ans += t + temp / (w[i] + s);
                t = 0;
            }
            else
            {
                ans += len[i] / (r + w[i]);
                t -= needRun;
            }
        }
        fout << "Case #" << test <<": " << setiosflags(ios::fixed) << setprecision(10) << ans << endl;
    }
    fout.close();
    fin.close();
    return 0;
}