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

struct DATE
{
    DATE (): h(0), m(0) {}
    DATE (int h_, int m_): h(h_), m(m_) {}
    
    bool operator < (const DATE& rhnd) const
    {
        if(h != rhnd.h)
            return h > rhnd.h;
        if(m != rhnd.m)
            return m > rhnd.m;
        return false;
    }
    
    int h, m;
};

int _tmain(int argc, _TCHAR* argv[])
{
    FILE* fInput = fopen("B-large.in", "r");
    FILE* fOutput = fopen("output.txt", "w");
    if(!fInput || !fOutput)
        return 0;

    int nCases = 0;
    fscanf(fInput, "%d", &nCases);

    std::vector<DATE> depFromA;
    std::vector<DATE> depFromB;
    std::vector<DATE> arrToA;
    std::vector<DATE> arrToB;

    for(int iCase = 0 ; iCase < nCases; ++iCase)
    {
        //TODO: write your code here   

        int nRoundoff = 0;

        int nAB = 0;
        int nBA = 0;
       
        depFromA.clear();
        depFromB.clear();
        arrToA.clear();
        arrToB.clear();

        fscanf(fInput, "%d\n", &nRoundoff);

        fscanf(fInput, "%d %d\n", &nAB, &nBA);
        
        int hSt, mSt, hEnd, mEnd; 
        for(int i = 0; i < nAB; ++i)
        {
            fscanf(fInput , "%d:%d %d:%d\n", &hSt, &mSt, &hEnd, &mEnd);
           
            DATE endDate, startDate(hSt, mSt);
            
            endDate.h = hEnd + (int)((mEnd + nRoundoff)/60);
            endDate.m = (mEnd + nRoundoff)%60;
            
            arrToB.push_back(endDate);
            depFromA.push_back(startDate);
        }

        for(int i = 0; i < nBA; ++i)
        {
            fscanf(fInput , "%d:%d %d:%d\n" , &hSt, &mSt, &hEnd, &mEnd);
            DATE endDate, startDate(hSt, mSt);

            endDate.h = hEnd + (int)((mEnd + nRoundoff)/60);
            endDate.m = (mEnd + nRoundoff)%60;

            arrToA.push_back(endDate);
            depFromB.push_back(DATE(hSt, mSt));
        }

        std::sort(arrToA.begin(), arrToA.end());
        std::sort(arrToB.begin(), arrToB.end());
        std::sort(depFromA.begin(), depFromA.end());
        std::sort(depFromB.begin(), depFromB.end());

        int nTrA = 0, nTrB = 0;
        std::vector<DATE>::iterator iter, f_it;
        for(iter = depFromB.begin(); iter != depFromB.end(); ++iter)
        {
            f_it = std::lower_bound(arrToB.begin(), arrToB.end(), *iter);
            if(f_it == arrToB.end())
                nTrB ++;
            else
                arrToB.erase(f_it);
        }
        
        for(iter = depFromA.begin(); iter != depFromA.end(); ++iter)
        {
            f_it = std::lower_bound(arrToA.begin(), arrToA.end(), *iter);
            if(f_it == arrToA.end())
                nTrA ++;
            else
                arrToA.erase(f_it);
        }

        fprintf(fOutput, "Case #%d: ", iCase+1);
        fprintf(fOutput, "%d %d\n", nTrA, nTrB);
    }
    fclose(fOutput);
    fclose(fInput);

    return 0;
}

