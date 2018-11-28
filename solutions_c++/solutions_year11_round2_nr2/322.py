// google code jam B

#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

const int MAXN = 1000100;
const double eps = 1e-8;

double pos[MAXN], c, d;
int n;

void qs(int l, int r)
{
    int i = l, j = r;
    double x = pos[(l + r) >> 1];
    do
    {
        while (i < r && pos[i] < x) i++;
        while (l < j && pos[j] > x) j--;
        if (i <= j)
        {
            double t = pos[i];
            pos[i] = pos[j];
            pos[j] = t;
            i++, j--;
        }
    } while (i <= j);
    if (i < r)
        qs(i, r);
    if (l < j)
        qs(l, j);
}

bool check(double lim)
{
    double p = pos[1] - lim;
    for (int i = 2; i <= n; i++)
        if (pos[i] < p + d)
        {
            if (pos[i] + lim < p + d)
                return false;
            p = p + d;
        }
        else
        {
            double delta = lim < pos[i] - (p + d) ? lim :  pos[i] - (p + d);
            p = pos[i] - delta;
        }
    return true;
}

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::in);
    ofstream fout("bout.txt", ios::out);
    int testcase;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> c >> d;
        n = 0;
        for (int i = 1; i <= c; i++)
        {
            int p, v;
            fin >> p >> v;
            for (int j = 1; j <= v; j++)
                pos[++n] = p;
        }
        qs(1, n);
        double l = 0, r = (1e23);
        int btime = 0;
        while (r - l > eps && btime < 150)
        {
            btime++;
            double mid = (l + r) / 2;
            if (check(mid))
                r = mid;
            else
                l = mid;
        }
        double ans = (l + r) / 2;
        fout << "Case #" << test << ": " << setiosflags(ios::fixed) <<setprecision(10) << ans << endl;
    }
    fout.close();
    fin.close();
    return 0;
}