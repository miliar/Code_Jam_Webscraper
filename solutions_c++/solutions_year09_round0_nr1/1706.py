// Usage: rename input file -> input.txt
// output file with the solution is output.txt
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#define MAX_L 15
#define MAX_D 5000
#define MAX_N 500

using namespace std;

void reset (int * v, int max, int value)
{
    for (int i=0;i<max;i++)
    {
        v[i] = value;
    }
}

int compare (int *v, int D, int L)
{
    int sum = 0;

    for (int i = 0; i<D;i++)
        sum = sum + (v[i] == L);

    return sum;
}

int main()
{
    int i,j,k;
    int L,D,N;
    int v[MAX_D];
    string line;
    char c[MAX_D][MAX_L];
    char ch;

    ifstream infile("input.txt");
    ofstream outfile("output.txt");

    if (!infile)
    {
        cout << "There was a problem opening the file for reading."
             << endl;
        return 0;
    }
    //cout << "Opened for reading." << endl;


    getline (infile,line);
    stringstream ss(line);
    ss >> L >> D >> N;

    for (i=0;i<D;i++)
    {
        for (j=0;j<L;j++)
        {
            infile >> c[i][j];
        }
    }

    /*
        for (i=0;i<D;i++)
        {
            for (j=0;j<L;j++)
                cout << c[i][j];
            cout << endl;
        }
        */
    getline (infile,line);

    string f;


    for (i=0;i<N;i++)
    {
        reset (v,MAX_D,0);
        getline (infile,line);
        stringstream ss(line);
        for (j=0;j<L;j++)
        {
            ss >> ch;
            if (ch == '(')
            {
                ss >> ch;
                while (ch != ')')
                {
                    for (k=0;k<D;k++)
                        v[k]= v[k] + (ch == c[k][j]);
                    ss >> ch;
                }

            }

            else
            {
                for (k=0;k<D;k++)
                        v[k]= v[k] + (ch == c[k][j]);
            }


        }

        outfile << "Case #" << i+1 <<": "<<compare(v, D, L) << endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
