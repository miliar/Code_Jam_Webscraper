#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

using namespace std;


int main()
{
    int Tcases;
    string line;
    ifstream infile ("input.txt");
    ofstream outfile ("output.txt");

    int data[30];
    data[0]=1;
    for (int i = 1; i < 30; i++)
    {
        data[i] = 2*data[i-1]+1;
    }

    getline (infile,line);
    Tcases = atoi(line.c_str());

    for (int i = 0; i < Tcases; i++)
    {
        int N, k;
        string buf;

        getline (infile,line);
        stringstream ss (stringstream::in | stringstream::out);
        ss << line;
        int j = 0;
        while (ss >> buf){
            switch(j){
                case 0:
                    N = atoi(buf.c_str());
                    break;
                case 1:
                    k = atoi(buf.c_str());
                    break;
            }
            j++;
        }
        //RECOGI DATOS.

        bool luzPrendida = false;
        if(data[N-1]==k)luzPrendida = true;
        else if( (k-data[N-1]) % (data[N-1]+1)==0)luzPrendida = true;
        outfile << "Case #" << i+1 << ": ";
        if(luzPrendida) outfile << "ON" << endl;
        else outfile << "OFF" << endl;
    }
    system("pause");
    return 0;
}

