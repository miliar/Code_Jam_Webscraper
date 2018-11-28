#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("blah.in");
ofstream fout ("blah.txt");

int main()
{
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
        int n, best[10100];
        int d[10100], h[10100];
        int D;
        for (int i = 0; i < 10100; i++)
            best[i] = -1;
        fin >> n;
        for (int i = 0; i < n; i++)
            fin >> d[i] >> h[i];
        fin >> D;
        best[0] = d[0];
        bool check = false;
        for (int i = 0; i < n; i++)
        {
            if (best[i] == -1)
                continue;
            int f = best[i] + d[i];
            for (int j = i + 1; j < n; j++)
                if (f >= d[j])
                {
                    best[j] = max (best[j], min (d[j] - d[i], h[j]));
                }
            if (f >= D)
                check = true;
        }
        fout << "Case #" << test + 1 << ": ";
        if (check)
            fout << "YES\n";
        else
            fout << "NO\n";
    }
    return 0;
}
