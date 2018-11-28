
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <fstream>
#include <algorithm>

using namespace std;

///////////////////////////////////
//
void getfarfarEngine(vector<string> engines, vector<string> *requests, vector<string>::iterator *requestsIt)
{
    vector<string>::iterator it;
    while (!engines.empty())
    {
        it = find_first_of(*requestsIt, requests->end(), engines.begin(), engines.end());
        if(it == requests->end())
        {
            *requestsIt = it;
            return;
        }
        else
        {
            vector<string>::iterator engineIt = find(engines.begin(), engines.end(), *it ); 
            engines.erase(engineIt);
        }
    }
    *requestsIt = it;
}

///////////////////////////////////
//
int computeStuff(vector<string> *engines, vector<string> *requests)
{
    int switchNb = -1;
    vector<string>::iterator requestsIt = requests->begin();
    while (requestsIt != requests->end())
    {
        getfarfarEngine(*engines, requests, &requestsIt);
        switchNb++;
    }
     
    return switchNb;
}

///////////////////////////////////
//
int main(int argc, char* argv[])
{
    fstream inputFile ("input.dat", fstream::in);
    fstream outputFile ("output.dat", fstream::out);
    int testCase;
    inputFile >>testCase;

    // leak me
    vector<string> *engines = new vector<string>;
    vector<string> *requests= new vector<string>;;

    for (int test = 0; test< testCase; test++)
    {
        int engineNb;
        inputFile >> engineNb;
        string caca;
        getline(inputFile, caca);
        for (int i = 0; i< engineNb; i++)
        {
            string engine;
            getline(inputFile, engine);
            engines->push_back(engine);
        }

        int requestNb;
        inputFile >> requestNb;
        getline(inputFile, caca);
        for (int i = 0; i< requestNb; i++)
        {
            string request;
            getline(inputFile, request);

            requests->push_back(request);
        }
        int switchNb = 0; 
        if (requestNb != 0)
            switchNb = computeStuff(engines, requests);
        outputFile << "Case #"<<test+1<<": "<<switchNb << endl;
        engines->clear();
        requests->clear();
    }
	return 0;
}

