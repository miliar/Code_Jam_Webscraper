#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;




void process_file(ifstream& input, ofstream& output)
{
    // Amount of test cases, search engines, queries and switches
    int numCases=0, numEngines=0,numQueries=0,numSwitches=0;
    // Array containing engine names
    vector<string> engines;
    // Array containing queries
    vector<string> queries;

    // current engine
    string cureng;



    // read number of cases
    input >> numCases;

    // start processing loop
    for(int i = 0; i < numCases;i++)
    {
        numSwitches =0;
        // number of search engines
        input >> numEngines;

        // clear and resize arrays
        engines.clear();
        engines.resize(numEngines);

        // needed to skip line end
        input.get();
        for(int j = 0; j < numEngines; j++)
        {
            getline(input,engines[j]);
        }

        // input number of queries
        input >> numQueries;
        queries.clear();
        queries.resize(numQueries);

        // skip line end;
        input.get();
        for(int j = 0; j < numQueries; j++)
        {
            getline(input,queries[j]);
        }


        vector<string>::iterator lPos = queries.begin();
        vector<string>::iterator pos = lPos;
        // find the engine which appears as last
        for(int j = 0; j < numEngines; j++)
        {
            pos = find(queries.begin(), queries.end(), engines[j]);
            if(pos > lPos)
            {
                lPos = pos;
                cureng = engines[j];
            }
        }
        // compute number of switches
        vector<string>::iterator cPos = queries.begin();
        for(cPos = queries.begin(); cPos < queries.end(); cPos++)
        {
            // have to switch
            if(cureng == *cPos)
            {
                // increase number of switches
                numSwitches++;

                // find the engine which apperas as last
                lPos = queries.begin();
                for(int j = 0; j < numEngines; j++)
                {
                    if(engines[j] == cureng) continue;
                    pos = find(cPos, queries.end(), engines[j]);
                    if(pos > lPos)
                    {
                        lPos = pos;
                        cureng = engines[j];
                    }
                }
            }
        }

        output << "Case #" << i+1 << ": " << numSwitches << endl;
    }
}

int main(int argc, char* argv[])
{
    // read command line
    string Buffer, filename="";
    for(int i = 0; i<argc;i++)
    {
        Buffer = argv[i];
        if(Buffer == "-f")
            filename = argv[++i];
    }

    // No input file specified
    if(filename=="")
    {
        cout << "No input file specified, please specify the input file" << endl
             << "Using the -f command line option" << endl;
        cin.clear();
        cin.ignore(256,'\n');
        cin.get();
        return -2;
    }

    // Open the file
    ifstream input(filename.c_str(),ios::in);
    //
    ofstream output("output.txt");

    // Process file
    process_file(input, output);

    // close filea
    input.close();
    output.close();

    return 0;
}
