// Rotate-- Google Code Jam 2010 //
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
    uli K,N;
    vector<char> map;
};

uli readingS(char car,uli i,uli j,uli num,c ca)
{
    if ((i>=0) && (j>=0) && (i<ca.N) && (j<ca.N) && (ca.map.at(i+ca.N*j) == car))
        return readingS(car,i,j+1,num+1,ca);
    else
        return num;
}

uli readingE(char car,uli i,uli j,uli num,c ca)
{
    if ((i>=0) && (j>=0) && (i<ca.N) && (j<ca.N) && (ca.map.at(i+ca.N*j) == car))
        return readingE(car,i+1,j,num+1,ca);
    else
        return num;
}

uli readingSE(char car,uli i,uli j,uli num,c ca)
{
    if ((i>=0) && (j>=0) && (i<ca.N) && (j<ca.N) && (ca.map.at(i+ca.N*j) == car))
        return readingSE(car,i+1,j+1,num+1,ca);
    else
        return num;
}

uli readingSO(char car,uli i,uli j,uli num,c ca)
{
    if ((i>=0) && (j>=0) && (i<ca.N) && (j<ca.N) && (ca.map.at(i+ca.N*j) == car))
        return readingSO(car,i-1,j+1,num+1,ca);
    else
        return num;
}

bool reading(char car,uli i,uli j,c ca)
{
    if ((readingS(car,i,j,0,ca)>=ca.K) or (readingE(car,i,j,0,ca)>=ca.K) or
        (readingSE(car,i,j,0,ca)>=ca.K) or (readingSO(car,i,j,0,ca)>=ca.K))
    {
        return true;
    }
    else
    {
        return false;
    }
}

void  print_map(c ca)
{
    for (uli j=0;j<ca.N;j++)
    {
        for (uli i=0;i<ca.N;i++)
        {
            cout << ca.map.at(i+ca.N*j);
        }
        cout << endl;
    }
    cout << endl;
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
                iFile >> currentCases.N >> currentCases.K;
                char currentChar;
                for (uli j=0;j<currentCases.N*currentCases.N;j++)
                {
                    iFile >> currentChar;
                    currentCases.map.push_back(currentChar);
                }
                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            cout << "Case : " << c_count <<endl;
            c currentCases;
            currentCases = cases.at(c_count);

            cout << "Gravity..." << endl;
            // For each line :

            for (uli j=0;j<currentCases.N;j++)
            {
                for (uli i=currentCases.N-1;i<currentCases.N;i--)
                {
                    uli limit=0;
                    while ((currentCases.map.at(i+currentCases.N*j) == '.') && (limit<i))
                    {
                        limit++;
                        for (uli k=i;k>0;k--)
                        {
                            currentCases.map.at(k+currentCases.N*j) = currentCases.map.at(k+currentCases.N*j-1);
                            currentCases.map.at(k+currentCases.N*j-1) = '.';
                        }
                    }
                }
            }

            cout << "Compting..." << endl;
            // For each coins :
            uli RgotIt=0;
            uli BgotIt=0;
            for (uli j=0;j<currentCases.N;j++)
            {
                for (uli i=0;i<currentCases.N;i++)
                {
                    if (currentCases.map.at(i+currentCases.N*j)!='.')
                    {
                        if ((currentCases.map.at(i+currentCases.N*j)=='R' && RgotIt==0) or
                        (currentCases.map.at(i+currentCases.N*j)=='B' && BgotIt==0))
                        {
                            if (reading(currentCases.map.at(i+currentCases.N*j),i,j,currentCases))
                            {
                                if (currentCases.map.at(i+currentCases.N*j)=='R')
                                {
                                    RgotIt=1;
                                }
                                else
                                {
                                    BgotIt=1;
                                }
                            }
                        }
                    }
                }
            }

            string out;
            if (RgotIt==1 && BgotIt==0)
            {
                out = "Red";
            }
            if (RgotIt==0 && BgotIt==1)
            {
                out = "Blue";
            }
            if (RgotIt==0 && BgotIt==0)
            {
                out = "Neither";
            }
            if (RgotIt==1 && BgotIt==1)
            {
                out = "Both";
            }
            output.push_back(out);
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
