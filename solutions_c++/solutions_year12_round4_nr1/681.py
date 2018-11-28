#include <fstream>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <deque>
#include <iomanip>
using namespace std;

bool Swing(int *d, int *l, int index, int len, int D, int N)
{
    len = min(len, l[index]);
    if (d[index] + len >= D)
    {
        return true;
    }
    else
    {
        int j = index + 1;
        while ((j < N) && (d[index] + len >= d[j]))
        {
            if (Swing(d, l, j, d[j] - d[index], D, N))
            {
                return true;
            }
            else
            {
                j++;
            }
        }
        return false;
    }
}

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    int T;
    in >> T;
    for (int x = 0; x < T; x++)
    {
        int N, D;
        int *d, *l;
        in >> N;
        d = new int[N];
        l = new int[N];
        for (int i = 0; i < N; i++)
        {
            in >> d[i] >> l[i];
        }
        in >> D;

        out << "Case #" << (x+1) << ": ";
        if (Swing(d, l, 0, d[0], D, N))
        {
            out << "YES";
        }
        else
        {
            out << "NO";
        }
        out << endl;
        delete [] d;
        delete [] l;
    }
    in.close();
    out.close();
    return 0;
}
