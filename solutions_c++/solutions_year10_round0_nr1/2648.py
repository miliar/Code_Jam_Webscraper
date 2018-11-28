// Solving the snapper problem //
/*
Note : hmm, I coded the C way, shame on me ^^
*/



#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;
typedef unsigned long int uli;

struct c    // one case containing N & K
{
    uli N;
    uli K;
};

int main()
{
    string inputFileName;   // Here it's what we need
    string outputFileName;
    uli T;
    vector<c> cases;
    vector<string> output;

    cout << "Name of input file : ";   // Asking for input file
    cin >> inputFileName;

    ifstream iFile(inputFileName.c_str(), ios::in);   // & opening this file
    if(iFile)
    {
        cout << "Reading ..." << endl << endl;
        iFile >> T;
        cout << "There will be : " << T << " lines" << endl << endl;

        uli currentN;
        uli currentK;
        c currentCase;
        for (unsigned i=0;i<T;i++)
        {
            iFile >> currentN >> currentK;
            currentCase.K = currentK;
            currentCase.N = currentN;
            cases.push_back(currentCase);
        }
        iFile.close();      // End reading the input file

        cout << "Processing" << endl;
        uli allOn;
        bool currentResult;

        for (unsigned i=0;i<cases.size();i++)
        {
            allOn = pow(2,cases.at(i).N)-1;
            cases.at(i).K = cases.at(i).K % (allOn+1);
            currentResult = (cases.at(i).K == allOn);
            if (currentResult) {output.push_back("ON");} else {output.push_back("OFF");}
        }

        cout << "Name of output file : ";   // Asking for output file
        cin >> outputFileName;

        ofstream oFile(outputFileName.c_str(), ios::out | ios::trunc);
        if(oFile)
        {
                for (unsigned i=0;i<cases.size();i++)
                {

                    oFile << "Case #" << i+1 << ": " << output.at(i).c_str() << endl;
                }

                oFile.close();
        }
        else
        {
            cout << "Unable to open the output file : " << outputFileName.c_str() << endl;
        }



    }
    else    // Failed to open the input file
    {
         cout << "Unable to open the input file : " << inputFileName.c_str() << endl;
    }


    cout << "Exiting ..." << endl;
    return 0;
}
