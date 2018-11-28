// Network -- Google Code Jam 2010 //
/*
Note : Nothing to say...
Alex
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
typedef signed long int uli;

struct c // one case
{
    uli N;
    vector<uli> A;
    vector<uli> B;
};

int main()
{
    string inputFileName; // Here is what we need
    string outputFileName;
    uli T;
    vector<c> cases;
    vector<uli> output;

    cout << "Name of input file : "; // Asking for the input file
    cin >> inputFileName;

    ifstream iFile(inputFileName.c_str(), ios::in); // & trying to open it
    if(iFile)
    {
            string currentLine;
            cout << "Reading ..." << endl << endl;
            iFile >> T;
            cout << T << " cases will folow..."<<endl << endl;

            for (uli i=0;i<T;i++)
            {
                c currentCases;
                iFile >> currentCases.N;
                uli A,B;
                for (uli j=0;j<currentCases.N;j++)
                {
                    iFile >> A >> B;
                    currentCases.A.push_back(A);
                    currentCases.B.push_back(B);
                }
                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            cout << "Case : " << c_count+1 <<endl;
            c currentCases;
            currentCases = cases.at(c_count);
            uli out=0;

            for (uli k=0;k<currentCases.N;k++)
            {
                for (uli j=k+1;j<currentCases.N;j++)
                {
                    if ( (currentCases.A.at(k)-currentCases.A.at(j)) > 0 && (currentCases.B.at(k)-currentCases.B.at(j)) < 0 or
                        (currentCases.A.at(k)-currentCases.A.at(j)) < 0 && (currentCases.B.at(k)-currentCases.B.at(j)) > 0)
                    {
                        out ++;
                    }
                }
            }

            output.push_back(out);
        }


        cout << "Name of output file : ";   // Asking for output file
        cin >> outputFileName;

        ofstream oFile(outputFileName.c_str(), ios::out | ios::trunc);
        if(oFile)
        {
                for (uli i=0;i<cases.size()-1;i++)
                {

                    oFile << "Case #" << i+1 << ": " << output.at(i) << endl;
                }
                oFile << "Case #" << cases.size()-1+1 << ": " << output.at(cases.size()-1);

                oFile.close();
        }
        else
        {
            cout << "Unable to open the output file : " << outputFileName.c_str() << endl;
        }


    }
    else
    {
         cout << "Unable to open the input file : " << inputFileName.c_str() << endl;
    }


    cout << "Exiting ..." << endl;
    return 0;
}
