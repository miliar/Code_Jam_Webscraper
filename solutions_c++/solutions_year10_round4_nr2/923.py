#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int P;
int N;
int g[2048];
int m[1024];
int p[2048];

void main()
{
    ifstream fin("B-small.in");
    ofstream fout("A.out");
    int TT;
    fin >> TT; 
    for (int tt = 1; tt <= TT; ++tt)
    {
        fin >> P;
        N = (1 << P);
        for (int i = 0; i < N; ++i)
            fin >> m[i];
        for (int i = 0; i < N - 1; ++i)
            fin >> p[i];

        memset(g, 0, sizeof(g));
        for (int i = 0; i < N; ++i)
        {
            int step = N / 2;
            int q = 0;
            int j = i / 2;
            for (; step > 0; j >>= 1, step >>= 1)
            {
                if (m[i])
                    --m[i];
                else
                {
                    g[q+j] = 1;
                }
                q += step;
            }
        }
        int s = 0;
        for (int i = 0; i < N - 1; ++i)
            s += g[i];

        fout << "Case #" << tt << ": " << s << endl;
    }
    fout.close();
    fin.close();
}
