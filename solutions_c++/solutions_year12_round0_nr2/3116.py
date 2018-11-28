/* 
 * File:   main.cpp
 * Author: sajtos
 *
 * Created on April 14, 2012, 10:15 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct myclass
{
    bool operator() (int i, int j)
    {
        return (i > j);
    }
} myobject;

vector<int> readline(ifstream& f, int& n, int& s, int& p)
{
    f >> n;
    f >> s;
    f >> p;

    int* t = new int[n];

    for (int i = 0; i < n; i++)
    {
        f >> t[i];
    }

    vector<int> v(t, t + n);
    sort(v.begin(), v.end(), myobject);

    return v;
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
        int n, s, p;
        vector<int> v = readline(ifile, n, s, p);
        vector<int>::iterator it;
        int db = 0;
        
        for (it = v.begin(); it != v.end(); ++it)
        {
            int j = *it / 3;
            int k = *it % 3;
            
            if(j >= p)
            {
                db++;
            }
            else if(k > 0 && j + 1 >= p)
            {
                db++;
            }
            else if(s > 0)
            {
                if(k > 0 && j + k >= p)
                {
                    s--;
                    db++;
                }
                else if(*it >= 3 && (*it - 3) / 3 + 2 >= p)
                {
                    s--;
                    db++;
                }
                else if(*it >= 4 && (*it - 4) / 3 + 2 >= p)
                {
                    s--;
                    db++;
                }
                else if(*it >= 5 && (*it - 5) / 3 + 2 >= p)
                {
                    s--;
                    db++;
                }
            }
        }
        
        cout << db << endl;

        ofile << "Case #" << i + 1 << ": " << db << endl;
    }

    ifile.close();
    ofile.close();
    return 0;
}

