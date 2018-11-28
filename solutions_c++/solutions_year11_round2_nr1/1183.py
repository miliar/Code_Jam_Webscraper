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

struct Team {
    string games;
    int wins;
    int losses;
    double WP;
    double OWP;
    double OOWP;
};

int main()
{
    ofstream outfile("out.txt");

    int numCases;
    cin >> numCases;

    for (int i = 1; i <= numCases; i++)
    {
        int numTeams;
        cin >> numTeams;
        vector<Team> teams(numTeams);

        for (int j = 0; j < numTeams; j++)
        {
            cin >> teams[j].games;
            teams[j].wins   = count(teams[j].games.begin(),
                                    teams[j].games.end(), '1');
            teams[j].losses = count(teams[j].games.begin(),
                                    teams[j].games.end(), '0');

            teams[j].WP = (double)teams[j].wins / ((double)teams[j].wins + (double)teams[j].losses);
        }

        // Find opponent's win%
        for (int k = 0; k < numTeams; k++)
        {
            int totalOpponents = 0;
            double totalOppWinPct = 0;
            for (int m = 0; m < numTeams; m++)
            {
                if (teams[k].games[m] == '0')
                {
                    totalOpponents++;
                    totalOppWinPct += (double)(teams[m].wins - 1) / 
                                      (teams[m].wins + teams[m].losses - 1);
                }
                else if (teams[k].games[m] == '1')
                {
                    totalOpponents++;
                    totalOppWinPct += (double)(teams[m].wins) / 
                                      (teams[m].wins + teams[m].losses - 1);
                }
            }

            teams[k].OWP = totalOppWinPct / totalOpponents;
        }

        for (int q = 0; q < numTeams; q++)
        {
            int totalOpponents = 0;
            double totalOppOWP = 0;
            for (int r = 0; r < numTeams; r++)
            {
                if (teams[q].games[r] == '0' ||
                    teams[q].games[r] == '1')
                {
                    totalOpponents++;
                    totalOppOWP += teams[r].OWP;
                }
            }

            teams[q].OOWP = totalOppOWP / totalOpponents;
        }

        outfile << "Case #" << i << ": " << endl;

        for (int z = 0; z < numTeams; z++)
        {
            outfile << teams[z].WP * 0.25 +
                       teams[z].OWP * 0.5 +
                       teams[z].OOWP * 0.25 << endl;
        }
    }

    outfile.close();
    return 0;
}

