#pragma warning (disable:4786)

#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

typedef std::vector<int> TripVec;

int main ()
{
    int i, j;
    FILE *fp = NULL;

    fp = fopen("B-large.in", "r");
    if (!fp)
    {
        printf("Failed to open input file\n");
        exit(0);
    }

    // Read the number of cases
    int nCases;
    fscanf(fp, "%d", &nCases);

    i = 0;
    while (i < nCases)
    {
        // Read the turnaround time
        int taTime;
        fscanf(fp, "%d", &taTime);

        // Read the number of trips
        int nA2B;
        int nB2A;
        fscanf(fp, "%d %d", &nA2B, &nB2A);

        // Read the A2B trips
        j = 0;
        TripVec tripA2B;
        TripVec availB2A;
        while (j < nA2B)
        {
            int hhd, mmd;
            int hha, mma;
            fscanf(fp, "%d:%d %d:%d", &hhd, &mmd, &hha, &mma);
            tripA2B.push_back(60 * hhd + mmd);
            availB2A.push_back(60 * hha + mma + taTime);
            j++;
        }
        std::sort(tripA2B.begin(), tripA2B.end());
        std::sort(availB2A.begin(), availB2A.end());

        // Read the B2A trips
        j = 0;
        TripVec tripB2A;
        TripVec availA2B;
        while (j < nB2A)
        {
            int hhd, mmd;
            int hha, mma;
            fscanf(fp, "%d:%d %d:%d", &hhd, &mmd, &hha, &mma);
            tripB2A.push_back(60 * hhd + mmd);
            availA2B.push_back(60 * hha + mma + taTime);
            j++;
        }
        std::sort(tripB2A.begin(), tripB2A.end());
        std::sort(availA2B.begin(), availA2B.end());

        // Analyze the data, start at A first
        int nStartAtA = 0;
        TripVec::const_iterator tripIter;
        TripVec::const_iterator availIter;

        for (tripIter = tripA2B.begin(), availIter = availA2B.begin();
                tripIter != tripA2B.end(); tripIter++)
        {
            if (availIter != availA2B.end())
            {
                if (*tripIter < *availIter)
                    nStartAtA++; // We need a new train
                else
                    availIter++; // We can send this available train
            }
            else
            {
                nStartAtA++;
            }
        }
        
        // now B
        int nStartAtB = 0;
        for (tripIter = tripB2A.begin(), availIter = availB2A.begin();
                tripIter != tripB2A.end(); tripIter++)
        {
            if (availIter != availB2A.end())
            {
                if (*tripIter < *availIter)
                    nStartAtB++; // We need a new train
                else
                    availIter++; // We can send this available train
            }
            else
            {
                nStartAtB++;
            }
        }

        // Print the output
        printf("Case #%d: %d %d\n", i + 1, nStartAtA, nStartAtB);
        i++;
    }

    fclose(fp);
    return 0;
}