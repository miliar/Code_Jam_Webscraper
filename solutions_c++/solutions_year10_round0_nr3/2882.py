#include <iostream>
#include <fstream>

using namespace std;

const int R_MAX = 1000;
const int K_MAX = 100;
const int N_MAX = 10;

int g[10];
int r, k, n;

void main()
{
    ifstream fin("C-small.in");
    int T;
    fin >> T;
    for (int tt = 1; tt <= T; ++tt)
    {
        fin >> r >> k >> n;
        for (int i = 0; i < n; ++i)
            fin >> g[i];

        int i = 0, j = 0;
        int s = 0;
        for (j = 0; j < r; ++j)
        {
            int p = 0;
            int ii = i;
            for (; p + g[i] <= k; )
            {
                p += g[i];
                if (++i == n)
                    i = 0;
                if (ii == i)
                    break;
            }
            s += p;
        }
        cout << "Case #" << tt << ": " << s << endl;
    }
    fin.close();
}
