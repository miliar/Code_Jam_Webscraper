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
        __int64 numPlayers;
        __int64 lowNote, highNote;
        cin >> numPlayers >> lowNote >> highNote;

        if (lowNote == 1)
        {
            outfile << "Case #" << i << ": " << 1 << endl;
            
            char c;
            cin >> c;
            do {        
                cin.get(c);
            } while (c != '\n');

            continue;
        }
        
        __int64 curFreq;

        vector<__int64> possible;
        possible.clear();
        for (int k = lowNote; k <= highNote; k++)
        {
            possible.push_back(k);
        }

        bool no = false;
        for (int j = 0; !no && j < numPlayers; j++)
        {
            cin >> curFreq;
            if (curFreq == 1 || curFreq == lowNote || curFreq == highNote)
                continue;
            
            for (int m = 0; m < possible.size(); m++)
            {
                if (curFreq % possible[m] == 0 ||
                    possible[m] % curFreq == 0)
                {
                    continue;
                }
                else
                {
                    possible.erase(possible.begin() + m);
                    m--;
                }
            }
        }

        if (no || possible.empty())
            outfile << "Case #" << i << ": NO" << endl;
        else
            outfile << "Case #" << i << ": " << possible[0] << endl;
    }

    outfile.close();
    return 0;
}

