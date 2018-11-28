#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream infile("A-large.in");
    ofstream outfile("a_small.txt");
    
    int t, n, i, j;
    int a[100][2], index[2], time[2];
    char c;
    infile >> t;
    
    for ( i = 1; i <= t; ++i)
    {
        infile >> n;
        for (j = 0; j < n; ++j)
        {
            infile >> c;
            if ( c == 'O')
            {
                a[j][0] = 0;
                infile >> a[j][1];
            }
            else
            {
                a[j][0] = 1;
                infile >> a[j][1];
            }
        }

        time[a[0][0]] = a[0][1];
        time[1 - a[0][0]] = 0;
        index[0] = 1;
        index[1] = 1;

        for (j = 1; j < n; ++j)
        {
            if (a[j][0] == a[j-1][0])
            {
                time[a[j][0]] += abs(a[j][1] - a[j-1][1]) + 1;
                index[a[j][0]] = a[j][1];
            }
            else
            {
                time[a[j][0]] += abs(a[j][1] - index[a[j][0]]) + 1;
                if (time[a[j][0]] <= time[1 - a[j][0]])
                    time[a[j][0]] = time[1 - a[j][0]] + 1;
                index[a[j][0]] = a[j][1];
                index[a[j-1][0]] = a[j-1][1];
            }
        }
        outfile << "Case #" << i << ": " << time[a[n-1][0]] << endl;
    }
    return 0;
}
        