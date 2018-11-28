#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream ifile("A-large.in");
    ofstream ofile("A-large.txt");
    int t, n ,k;
    ifile >> t;
    for(int i=0;i<t;++i)
    {
        ofile << "Case #" << i+1 << ": ";
        ifile >> n >> k;

        if(k % 2 == 0)
        {
            ofile << "OFF\n";
            continue;
        }
        int cycle = pow((float)2,n);
        int final_times = k % cycle;
        if(final_times+1 == cycle)
            ofile << "ON\n";
        else
            ofile << "OFF\n";
    }
    return 0;
}
