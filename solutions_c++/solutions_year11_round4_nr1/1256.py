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
#include <iomanip>

#define FILE_IN "Asmall.in"
#define FILE_OUT "output.txt"
#define MAX 1111

using namespace std;

int t, N;
double len;
double time_run, walk_speed, run_speed;
int b[MAX], e[MAX], w[MAX];
double l[MAX];

double solve()
{
    int tmp;
    int sum = 0;
    for (int i=0; i<N; i++)
    {
        l[i] = e[i] - b[i];
  //      cout << l[i] << " ";
        sum += l[i];
    }
    l[N] = len - sum;
    cout << l[N] << endl;
    w[N] = 0;

    for (int i=0; i<N; i++)
    {
        for (int j=i+1; j<=N; j++)
        {
            if (w[j] < w[i])
            {
                tmp = w[i];
                w[i] = w[j];
                w[j] = tmp;

                tmp = l[i];
                l[i] = l[j];
                l[j] = tmp;
            }
        }
    }
  //  for (int i=0; i<=N; i++)
 //  {
  //      cout << l[i] << " " << w[i] << endl;
 //   }

    double loss;
    double ans = 0;
    for (int i=0; i<=N; i++)
    {
        if (fabs(time_run)>0.00000001)
        {
            loss = l[i] / (w[i] + run_speed);
        //    cout << "loss " << loss << endl;
            if (loss < time_run){
                time_run -= loss;
                ans += loss;
            }
            else {
                double rem = l[i] - (w[i] + run_speed) * time_run;
                ans += time_run + (rem / (w[i] + walk_speed));
                time_run = 0;
            }
        }
        else
        {
            ans += l[i] / (w[i] + walk_speed);
        }
   //     cout << ans << endl;
    }
  //  cout << endl;
    return ans;
}

int main()
{
    ifstream fin(FILE_IN);
    ofstream fout(FILE_OUT);

    fin >> t;
    for (int tcase=1; tcase <= t; tcase++)
    {
        fin >> len >> walk_speed >> run_speed >> time_run >> N;
        for (int i=0; i<N; i++)
        {
            fin >> b[i] >> e[i] >> w[i];
        }
        fout.setf(ios::fixed);
        fout.precision(7);
        fout << "Case #" << tcase << ": " << solve() << endl;
    }

    fin.close();
    fout.close();
}
