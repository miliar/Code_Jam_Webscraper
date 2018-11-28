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
/* #include <ttmath/ttmath.h> 
typedef ttmath::Int<TTMATH_BITS(128)> int128;
typedef ttmath::Int<TTMATH_BITS(256)> int256;
typedef ttmath::Int<TTMATH_BITS(512)> int512;
typedef ttmath::Int<TTMATH_BITS(1024)> int1024;
typedef ttmath::Int<TTMATH_BITS(2048)> int2048;

typedef ttmath::Big<TTMATH_BITS(32), TTMATH_BITS(96)> quadruple;
typedef ttmath::Big<TTMATH_BITS(64), TTMATH_BITS(192)> octuple; */


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
        int numRows, numCols;
        cin >> numRows >> numCols;
        
        vector<string> inGraph(numRows);
        for (int j = 0; j < numRows; j++)
        {
            cin >> inGraph[j];
        }

        bool impossible = false;
        for (int k = 0; k < numRows && !impossible; k++)
        {
            for (int m = 0; m < numCols; m++)
            {
                if (inGraph[k][m] == '#')
                {
                    if (m == numCols - 1 || k == numRows - 1)
                    {
                        impossible = true;
                        break;
                    }
                    
                    if (inGraph[k+1][m] == '#' &&
                        inGraph[k][m+1] == '#' &&
                        inGraph[k+1][m+1] == '#')
                    {
                        inGraph[k][m] = '/';
                        inGraph[k+1][m] = '\\';
                        inGraph[k][m+1] = '\\';
                        inGraph[k+1][m+1] = '/';
                    }
                    else
                    {
                        impossible = true;
                        break;
                    }
                }
            }
        }

        outfile << "Case #" << i << ": " << endl;

        if (impossible)
        {
            outfile << "Impossible" << endl;
        }
        else
        {
            for (int q = 0; q < numRows; q++)
            {
                outfile << inGraph[q] << endl;
            }
        }
    }

    outfile.close();
    return 0;
}

