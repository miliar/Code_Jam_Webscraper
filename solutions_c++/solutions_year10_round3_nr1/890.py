#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <string>

using namespace std;

typedef long unsigned int lui;



void round1c_A(void)
{
    // Input file
    ifstream inputFile;
        inputFile.open("Round1c-A-data/A-large.in");

    if(!inputFile.is_open())
    {
        printf("Error opening the input file.\n");
        return;
    }

    // Output file
    ofstream outputFile;
        outputFile.open("Round1c-A-data/A-large.out");

    if(!outputFile.is_open())
    {
        printf("Error opening the output file.\n");
        return;
    }

    lui T, N, A, B;
    lui t, n, i, j, c;
    vector<lui> a(1000);
    vector<lui> b(1000);

    inputFile >> T;
    cout << "T: " << T << endl;

    for(t=0; t<T; t++)
    {
        inputFile >> N;
        for(n=0; n<N; n++)
        {
            inputFile >> a[n] >> b[n];
        }

        c=0;

        for(i=0; i<N; i++)
        {
            for(j=i+1; j<N;j++)
            {
                if(a[i] < a[j] && b[i] > b[j])
                    c++;
                else if(a[i] > a[j] && b[i] < b[j])
                    c++;
            }
        }

        cout  << "Case #" << t+1 << ": " << c << endl;
        outputFile << "Case #" << t+1 << ": " << c << endl;
    }

    // Close opened files
    outputFile.close();
    inputFile.close();

}



