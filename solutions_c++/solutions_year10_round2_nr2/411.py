#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int N, K, B, T;
int X[50];
int V[50];
int a[50];

int compareFunc(const void* ii, const void* jj)
{
    int i = *((const int*)ii);
    int j = *((const int*)jj);
    long long ti = (long long)(B - X[i]) * V[j];
    long long tj = (long long)(B - X[j]) * V[i];
    if (ti > tj)
        return -1;
    else if (ti < tj)
        return 1;
    else
        return 0;
}

void main()
{
    ifstream fin("B-large.in");
    ofstream fout("A.out");
    for (int i = 0; i < 50; ++i)
        a[i] = i;
    int TT;
    fin >> TT; 
    for (int tt = 1; tt <= TT; ++tt)
    {
        fin >> N >> K >> B >> T;
        for (int i = 0; i < N; ++i)
            fin >> X[i];
        for (int i = 0; i < N; ++i)
            fin >> V[i];

        //qsort(a, 50, sizeof(int), compareFunc);

        //if (K > N || (B - X[a[K-1]] > V[a[K-1]] * T))
            //fout << "Case #" << tt << ": IMPOSSIBLE" << endl;
        //else
        //{
            //fout << "Case #" << tt << ": " << ans << endl;
        //}

        int s = 0;
        for (int i = N - 1; i >= 0 && K > 0; --i, --K)
        {
            int j = i;
            for (; j >= 0 && B - X[j] > T * V[j]; --j, ++s);
            if (j < 0)
            {
                s = -1;
                break;
            }
            for (; j < i; ++j)
            {
                X[j] = X[j+1];
                V[j] = V[j+1];
            }
        }

        fout << "Case #" << tt << ": ";
        if (s == -1)
            fout << "IMPOSSIBLE" << endl;
        else
            fout << s << endl;
    }
    fout.close();
    fin.close();
}
