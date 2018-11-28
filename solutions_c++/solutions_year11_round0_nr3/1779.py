#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream infile("C-large.in");
    ofstream outfile("c_large.txt");

    int t, n, b, c[20];
    infile >> t;
    int i, j, k, min, sum;
    int a[20];

    c[0] = 1;

    for (i = 1; i < 20; ++i)
    {
        c[i] = c[i - 1] * 2;
    }

    for (i = 0; i < t; ++i)
    {
        memset(a, 0, sizeof(a));
        min = 1000001;
        infile >> n;
        sum = 0;
        for (j = 0; j < n; ++j)
        {
            infile >> b;
            if (min > b)
                min = b;
            sum += b;
            for ( k = 19; k >= 0; --k)
            {
                a[k] += b / c[k];
                b = b % c[k];
            }
        }

        for (j = 0; j < 20; ++j)
        {
            if (a[j] % 2 == 1)
                break;
        }

        if (j == 20)
        {
            outfile << "Case #" << i + 1 << ": " << sum - min << endl;
        }
        else
        {
            outfile << "Case #" << i + 1 << ": NO" << endl;
        }
    }
    return 0;
}

    