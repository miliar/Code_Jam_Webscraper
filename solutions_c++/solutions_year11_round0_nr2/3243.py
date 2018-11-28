// Magicka -- Google Code Jam 2011 //
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


struct c // one case
{
    uli C,D,N;
    vector<string> combinableList;   //3 characters string of combinable elements
    vector<string> oppositeList;   //2 characters string of opposed elements
    string invocationList;
};

string combineList(string elementsList, c *currentCases)
{
    if (elementsList.size()>=2)
    {

        string e1 = elementsList.substr(elementsList.size()-2,1);
        string e2 = elementsList.substr(elementsList.size()-1,1);

        string e3 = e1 + e2;
        string e4 = e2 + e1;

        for (uli i=0;i<currentCases->C;i++)
        {
            if (currentCases->combinableList.at(i).find(e3)==0 or currentCases->combinableList.at(i).find(e4)==0)
            {
                elementsList.replace(elementsList.size()-2,2,currentCases->combinableList.at(i).substr(2,1));
                break;
            }
        }

    }
    return elementsList;
}

string opposeList(string  elementsList, c *currentCases)
{
    if (elementsList.size()>=1)
    {
        string e1 = elementsList.substr(elementsList.size()-1,1);
        string n = "";

        for (uli i=0;i<currentCases->D;i++)
        {
            if (currentCases->oppositeList.at(i).find(e1)==0)
            {
                if (elementsList.find(currentCases->oppositeList.at(i).substr(1,1))!=string::npos)
                    return n;
            }
            if (currentCases->oppositeList.at(i).find(e1)==1)
            {
                if (elementsList.find(currentCases->oppositeList.at(i).substr(0,1))!=string::npos)
                    return n;
            }
        }
    }
    return elementsList;
}

string formatList(string L)
{
    string T;
    if (L.size() != 0)
    {
        for (uli i=0;i<L.size()-1;i++)
        {
            T = T + L.substr(i,1);
            T = T + ',' + ' ';
        }
        T = T + L.substr(L.size()-1,1);
    }
    L = '['+T+']';
    return L;
}

int main()
{
    string inputFileName; // Here is what we need
    string outputFileName;
    uli T;
    vector<c> cases;
    vector<string> output;

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
                iFile >> currentCases.C;
                string currentString;
                for (uli j=0;j<currentCases.C;j++)
                {
                    iFile >> currentString;
                    currentCases.combinableList.push_back(currentString);
                }
                iFile >> currentCases.D;
                for (uli j=0;j<currentCases.D;j++)
                {
                    iFile >> currentString;
                    currentCases.oppositeList.push_back(currentString);
                }
                iFile >> currentCases.N;
                iFile  >> currentCases.invocationList;

                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            cout << "Case : " << c_count+1 <<endl;
            c currentCases;
            currentCases = cases.at(c_count);

            string elementsList;
            for  (uli i=0;i<currentCases.N;i++)
            {
                elementsList = elementsList + currentCases.invocationList.at(i);
                elementsList = combineList(elementsList, &currentCases);
                elementsList = opposeList(elementsList, &currentCases);
            }

            elementsList = formatList(elementsList);
            output.push_back(elementsList);
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
