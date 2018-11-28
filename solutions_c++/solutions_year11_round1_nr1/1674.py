#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
    ifstream infile;
    infile.open("A-small-attempt6.in");
    ofstream outfile;
    outfile.open("A.out");
    int T, N, Pd, Pg;
    infile >> T;
    for (int i = 1; i <= T; i++)
    {
        cout << "Case: " << i << endl;
        bool answer = false;
        infile >> N >> Pd >> Pg;
        if (N >= 100) 
        {
            if (Pg == 0 && Pd != 0) answer = false;
            else if (Pd < 100 && Pg == 100) answer = false;
            else if (Pd == 100 && Pg == 0) answer = false;
            else answer = true;
        }
        else
        {
            if (Pg == 0 && Pd != 0) answer = false;
            else if (Pd < 100 && Pg == 100) answer = false;
            else if (Pd == 100 && Pg == 0) answer = false;
            else
            {
                if (N >= 2) 
                {
                    if (Pd%50 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N >= 4)
                            {
                    if (Pd%25 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N >= 5)
                            {
                    if (Pd%20 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N >= 10)
                            {
                    if (Pd%10 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N >= 20)
                            {
                    if (Pd%5 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N >= 50)
                            {
                    if (Pd%2 != 0) answer = answer || false;
                    else answer = answer || true;
                }
                if (N == 1)
                            {
                    if (Pd != 100 && Pd != 0) answer = false;
                    else answer = true;
                }
            }
        }
        if (answer) outfile << "Case #" << i << ": " << "Possible" << endl;
        else outfile << "Case #" << i << ": " << "Broken" << endl;
    }
    return 0;
}
            