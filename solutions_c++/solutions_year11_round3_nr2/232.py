// Mike Terranova
// Compiled with MS Visual Studio 2010
// May 21, 2011

#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;
using namespace std::placeholders;

// ttmath Library: Available under BSD license: ttmath.org
#include <ttmath/ttmath.h> 
typedef ttmath::Int<TTMATH_BITS(128)> int128;
typedef ttmath::Int<TTMATH_BITS(256)> int256;
typedef ttmath::Int<TTMATH_BITS(512)> int512;
typedef ttmath::Int<TTMATH_BITS(1024)> int1024;
typedef ttmath::Int<TTMATH_BITS(2048)> int2048;

typedef ttmath::Big<TTMATH_BITS(32), TTMATH_BITS(96)> quadruple;
typedef ttmath::Big<TTMATH_BITS(64), TTMATH_BITS(192)> octuple;


/* #include <boost/graph/graph_traits.hpp>
#include <boost/graph/properties.hpp>
#include <boost/graph/adjacency_list.hpp>
using namespace boost;

typedef adjacency_list<vecS, vecS, directedS, no_property, property<edge_weight_t, int> > Graph;
typedef graph_traits<Graph>::edge_descriptor Edge;
typedef graph_traits<Graph>::vertex_descriptor Vertex;
typedef pair<int, int> E;

Graph g;
Edge e, bool ok;
tie(e, ok) = add_edge(0, 2, g);
auto weightmap = get(edge_weight, g);
weightmap[e] = weight; */

int main()
{
    ofstream outfile("out.txt");

    int numCases;
    cin >> numCases;

    for (int i = 1; i <= numCases; i++)
    {
        __int64 numBoosters, buildTime, numStars, numNumbers;
        cin >> numBoosters >> buildTime >> numStars >> numNumbers;

        vector<__int64> numbers(numNumbers);
        for (int j = 0; j < numNumbers; j++)
            cin >> numbers[j];

        vector<int> numCycles(numNumbers);
        for (int k = 0; k < numNumbers; k++)
        {
            numCycles[k] = numStars / numNumbers;
            if ((numStars % numNumbers) > k)
                numCycles[k]++;
        }

        vector<__int64> totalTime(numNumbers);
        for (int m = 0; m < numNumbers; m++)
        {
            totalTime[m] = numbers[m] * numCycles[m];
        }

        // cout << "Done 1, " << i << endl;

        __int64 sumAll = 0;
        for (int z = 0; z < numNumbers; z++)
        {
            sumAll += numbers[z];
        }

        // Get rid of build time from the counts
        __int64 initBuildTime = buildTime;
        int numCyclesKilled = 0;
        while (initBuildTime > (sumAll * 2))
        {
            initBuildTime -= sumAll * 2;
            numCyclesKilled++;
        }

        for (int y = 0; y < numNumbers; y++)
        {
            totalTime[y] -= (numbers[y] * numCyclesKilled);
        }

        // cout << "Done 2, " << i << endl;

        for (int a = 0; initBuildTime > 0; a = ((a+1) % numNumbers))
        {
            __int64 subtractor;
            if (initBuildTime <= (numbers[a] * 2))
                subtractor = initBuildTime / 2;
            else
                subtractor = numbers[a];
            
            totalTime[a] -= subtractor;
            if (totalTime[a] < numbers[a])
                numbers[a] = totalTime[a];

            initBuildTime -= (subtractor * 2);
        }

        // Now, the final time will be (sum of totalTime) * 2
        // MINUS the biggest boosters
        // PLUS buildTime

        // cout << "Done 3, " << i << endl;

        __int64 finalTime = buildTime;
        for (int b = 0; b < numNumbers; b++)
        {
            finalTime += totalTime[b] * 2;
        }

        // cout << "Done 4, " << i << endl;

        for (int c = 0; c < numBoosters; c++)
        {
            int index = max_element(numbers.begin(), numbers.end()) - numbers.begin();

            finalTime -= numbers[index];
            totalTime[index] -= numbers[index];
            if (totalTime[index] < numbers[index])
                numbers[index] = totalTime[index];
        }

        // cout << "Done 5, " << i << endl;

        outfile << "Case #" << i << ": " << finalTime << endl;
    }

    outfile.close();
    return 0;
}

