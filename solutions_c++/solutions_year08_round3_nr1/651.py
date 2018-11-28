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

const double pi = 3.141592653589793238;

typedef long long ll;
typedef pair<int,int> IntPair;

int _tmain(int argc, _TCHAR* argv[])
{
    FILE* fInput = fopen("A-small-attempt0.in", "r");
    FILE* fOutput = fopen("output.txt", "w");
    if(!fInput || !fOutput)
        return 0;

    int nCases = 0;
    fscanf(fInput, "%d", &nCases);

    for(int iCase = 0 ; iCase < nCases; ++iCase)
    {
        //TODO: write your code here   

        int P, K, L;
        
        fscanf(fInput, "%d %d %d\n", &P, &K, &L);
        std::vector<long long> msg(L, (long long)0);
        for(int i = 0; i < L; ++i)
            fscanf(fInput, "%ld ", &msg[i]);
        fscanf(fInput,"\n");
        std::sort(msg.begin(), msg.end(), greater<long long>());

        if (L > K*P)
        {
            fprintf(fOutput, "Case #%d: Impossible\n", iCase+1);
            continue;
        }
    
        long long n = L/K;
        long long m = L%K;

        long long cnt =  0.0;
        for(int i = 0; i < L; ++i)
        {
            long long weight = i/K + 1;
             cnt += weight*msg[i];
        }

        fprintf(fOutput, "Case #%d: ", iCase+1);
        fprintf(fOutput, "%d\n", cnt);

    }
    fclose(fOutput);
    fclose(fInput);

    return 0;
}

