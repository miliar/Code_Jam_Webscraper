#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

fstream fin_small("small.in", ios_base::in);
fstream fout_small("small.out", ios_base::out);
fstream fin_big("large.in", ios_base::in);
fstream fout_big("large.out", ios_base::out);
fstream fin_test("test.in", ios_base::in);
fstream fout_test("test.out", ios_base::out);

template <typename T>
T read(fstream& fin)
{
    string s;
    getline(fin, s);
    T t;
    stringstream(s) >> t;
    return t;
}

template <>
string read<string>(fstream& fin)
{
    string s;
    getline(fin, s);
    return s;
}

double dist(double x1, double y1, double x2, double y2)
{
    return sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
}

int n;
int x[3], y[3], r[3];

double answer()
{
    if (n == 1)
        return r[0];
    if (n == 2)
        return max(r[0], r[1]);
    if (n == 3)
    {
        double d1 = dist(x[0], y[0], x[1], y[1]) + r[0] + r[1];
        double d2 = dist(x[0], y[0], x[2], y[2]) + r[0] + r[2];
        double d3 = dist(x[2], y[2], x[1], y[1]) + r[2] + r[1];
        return min(d1, min(d2, d3)) / 2;
    }
}

void solve(fstream& fin, fstream& fout)
{
    int tests = read<int>(fin);
    for (int test = 1; test <= tests; test++)
    {
        n = read<int>(fin);
        for (int i = 0; i < n; i++)
        {
            string sxyr = read<string>(fin);
            stringstream(sxyr) >> x[i] >> y[i] >> r[i];
        }
        fout << "Case #" << test << ": " << setprecision(7) << fixed << answer() << endl;
    }
    fout.close();
}

void main()
{
    //solve(fin_test, fout_test);
    solve(fin_small, fout_small);
    //solve(fin_big, fout_big);
}