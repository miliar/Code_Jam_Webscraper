#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    long long int K, N, T, div;
    vector<long long int> powers(1,1);

    for(long long int i=0; i<33; i++)
    {
        powers.push_back(2*powers[i]);
    }

    ifstream ifile;
    ofstream ofile;

    ifile.open("in.txt");
    ofile.open("out.txt");

    ifile >> T;

    for(long long int i=1; i<=T; i++)
    {
        ifile >> N >> K;

        ofile << "Case #" << i << ": ";

        if(N == 1)
        {
            if(K%2 != 0)
                ofile << "ON" << endl;
            else
                ofile << "OFF" << endl;
        }
        else
        {
            div = powers[N];
            if((K+1)%div == 0 && K != 0)
                ofile << "ON" << endl;
            else
                ofile << "OFF" << endl;
        }
    }

    ifile.close();
    ofile.close();

    return 0;
}
