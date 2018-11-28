/* 
 * File:   main.cpp
 * Author: sajtos
 *
 * Created on April 14, 2012, 10:15 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

void readline(ifstream& f, int& a, int& b)
{
    f >> a;
    f >> b;
}

bool eq(int a, int b)
{
    string A, B;

    stringstream out, out2;
    out << a;
    A = out.str();

    
    out2 << b;
    B = out2.str();
    int n = A.length();

    for (int i = 1; i <= n; i++)
    {
        if (A.substr(0, i) == B.substr(n - i, i) && A.substr(i, n - i) == B.substr(0, n - i))
        {
            return true;
        }
    }
    
    return false;
}

/*
 * 
 */
int main(int argc, char** argv)
{
    ifstream ifile;
    ofstream ofile;

    string path = argv[0];
    path += ".in";
    ifile.open(path.c_str());

    path = argv[0];
    path += ".out";
    ofile.open(path.c_str(), ios::trunc);

    int T;
    ifile >> T;

    for (int i = 0; i < T; i++)
    {
        int a, b;
        readline(ifile, a, b);
        int db = 0;
        for (int j = a; j < b; j++)
        {
            for (int k = j + 1; k <= b; k++)
            {
                if (eq(j, k))
                {
                    db++;
                }
            }
        }
        ofile << "Case #" << i + 1 << ": " << db << endl;
    }

    ifile.close();
    ofile.close();
    return 0;
}

