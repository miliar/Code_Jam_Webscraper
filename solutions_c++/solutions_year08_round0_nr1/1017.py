// CodeJam.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
//#include <stdio.h>

#include <cmath>
#include <cassert>

// STL containers
#include <vector>
#include <map>
#include <string>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <bitset>

// STL algorithms & functions
#include <functional>
#include <algorithm>
#include <limits>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
    FILE* fInput = fopen("A-large.in", "r");
    FILE* fOutput = fopen("output.txt", "w");
    if(!fInput || !fOutput)
        return 0;

    int nCases = 0;
    fscanf(fInput, "%d", &nCases);

    char itemName[200];

    std::vector<std::string> engines;
    std::vector<std::string> queries;

    engines.reserve(100);
    queries.reserve(1000);

    for(int iCase = 0 ; iCase < nCases; ++iCase)
    {
        //TODO: write your code here   
        int nEngines = 0;
        int nQueries = 0;
       
        engines.clear();
        queries.clear();

        fscanf(fInput, "%d\n", &nEngines);
        for(int iEngines = 0; iEngines < nEngines; ++iEngines)
        {
            fscanf(fInput , "%[^\n]\n" , itemName);
            engines.push_back( std::string(itemName) );
        }

        fscanf(fInput, "%d\n", &nQueries);
        for(int iQueries = 0; iQueries < nQueries; ++iQueries)
        {
            fscanf(fInput , "%[^\n]\n" , itemName);
            queries.push_back( std::string(itemName) );
        }

        int nSwitches = 0;

        std::vector<std::string>::iterator f_it, next_it;
        std::vector<std::string>::iterator cur_it = queries.begin();
        next_it = cur_it;
        while(cur_it != queries.end())
        {
            for(int iEngine = 0; iEngine < nEngines; ++iEngine)
            {
                f_it = std::find(cur_it, queries.end(), engines[iEngine]);
                if(f_it == queries.end())
                {
                    next_it = f_it;
                    break;
                }
                if(f_it > next_it)
                    next_it = f_it;
            }
            cur_it = next_it;
            if(cur_it != queries.end())
                nSwitches ++;
        }

        fprintf(fOutput, "Case #%d: ", iCase+1);
        fprintf(fOutput, "%d\n", nSwitches);
    }
    fclose(fOutput);
    fclose(fInput);

    return 0;
}

