#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int T, N[100], S[100], p[100], t[100][100], i, j;
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    
    infile >> T;
    for (i=0;i<T;i++)
    {
        infile >> N[i];
        infile >> S[i];
        infile >> p[i];
        for (j=0;j<N[i];j++)
        {
            infile >> t[i][j];
        }
    }
    
    for (i=0;i<T;i++)
    {
        int near = 0, pass = 0;
        for (j=0;j<N[i];j++)
        {
            if (t[i][j] >= 3*p[i]-2)
            {
                pass++;
            }
            else if (t[i][j] == 3*p[i]-3 || t[i][j] == 3*p[i]-4)
            {
                near++;
            }
        };
        if (near >= S[i] && p[i] > 1)
        {
            pass = pass + S[i];
        }
        else if (near < S[i] && p[i] > 1)
        {
            pass = pass + near;
        }
        outfile << "Case #" << i+1 << ": " << pass << endl;
    }

    infile.close();
    outfile.close();
    return 0;   
}

