// google code jam A

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;

const int MAXN = 110;

double winC[MAXN], allC[MAXN], n;
double wp[MAXN], owp[MAXN], oowp[MAXN];
string state[MAXN];

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::in);
    ofstream fout("aout.txt", ios::out);
    int testcase;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> n;
        for (int i = 0; i < n; i++)
        {
            winC[i] = allC[i] = 0;
            fin >> state[i];
            for (int j = 0; j < n; j++)
            {
                if (state[i][j] == '1')
                    winC[i]++;
                if (state[i][j] != '.')
                    allC[i]++;
            }
        }
        for (int i = 0; i < n; i++)
        {
            double against = 0, sum = 0;
            for (int j = 0; j < n; j++)
                if (state[i][j] != '.')
                {
                    against++;
                    double a = (state[i][j] == '1' ? winC[j] : winC[j] - 1), b = allC[j] - 1;
                    sum += (b == 0 ? 0 : a / b);
                }
            owp[i] = (against == 0 ? 0 : sum / against);
        }
        for (int i = 0; i < n; i++)
        {
            double against = 0, sum = 0;
            for (int j = 0; j < n; j++)
                if (state[i][j] != '.')
                {
                    against++;
                    sum += owp[j];
                }
            oowp[i] = (against == 0 ? 0 : sum / against);
        }
        fout << "Case #" << test << ":" << endl;
        for (int i = 0; i < n; i++)
        {
            double wp = (allC[i] == 0 ? 0 : winC[i] / allC[i]);
            double ans = 0.25 * wp + 0.5 * owp[i] + 0.25 * oowp[i];
            fout << setiosflags(ios::fixed) << setprecision(8) << ans << endl;
        }
    }
    fout.close();
    fin.close();
    return 0;
}