// Theme Park -- Google Code Jam 2010 //
/*
Note : Nothing to say...
Alex
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
typedef unsigned long int uli;

struct c // one case containing R=number of running, k=train capacity,N=number of groups,G vector of group's size
{
    uli R,k,N;
    vector<uli> G;
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
                uli currentSize;
                iFile >> currentCases.R >> currentCases.k >> currentCases.N;
                for (uli j=0;j<currentCases.N;j++)
                {
                    iFile >> currentSize;
                    currentCases.G.push_back(currentSize);
                }
                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            c currentCases;
            currentCases = cases.at(c_count);
            uli iGroupWaiting=0; // indice on the first waiting group (each time a group is boarding, this indice take +1)
            uli moneyTaken=0;
            for (uli run_count=0;run_count<currentCases.R;run_count++)  // For each train run
            {
                bool isBoarding = true;
                uli iFirstGroupWaiting=iGroupWaiting;
                uli remainingPlace = currentCases.k;
                while(isBoarding)
                {
                    if ( currentCases.G.at(iGroupWaiting) <= remainingPlace )   // Can we place the next group in the train ?
                    {
                        remainingPlace-=currentCases.G.at(iGroupWaiting);
                        moneyTaken+=currentCases.G.at(iGroupWaiting);
                        iGroupWaiting++;
                        iGroupWaiting=iGroupWaiting%currentCases.N;
                        if ( iFirstGroupWaiting ==  iGroupWaiting ) { isBoarding = false; }  // The iGroupWaiting is already onboard
                    }
                    else
                    {
                        isBoarding = false;
                    }
                }
            }
            output.push_back(moneyTaken);
        }


        cout << "Name of output file : ";   // Asking for output file
        cin >> outputFileName;

        ofstream oFile(outputFileName.c_str(), ios::out | ios::trunc);
        if(oFile)
        {
                for (uli i=0;i<cases.size();i++)
                {

                    oFile << "Case #" << i+1 << ": " << output.at(i) << endl;
                }

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
