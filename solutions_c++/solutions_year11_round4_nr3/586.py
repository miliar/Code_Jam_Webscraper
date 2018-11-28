// Mike Terranova
// Compiled with MS Visual Studio 2010
// June 4, 2011

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
#include <cstdio>

using namespace std;
using namespace std::placeholders;

typedef __int64 int64;

// ttmath Library: Available under BSD license: ttmath.org
#include <ttmath/ttmath.h> 
typedef ttmath::Int<TTMATH_BITS(64)> tt64;
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

int logX(double base, double num)
{
    return log(num) / log(base);
}

vector<int64> primes;
void getPrimes(int64 max)
{
    primes.clear();
    if (max == 1)
        return;

    primes.push_back(2);
    if (max == 2)
        return;

    for (int64 i = 3; i <= max; i++)
    {
        bool isPrime = true;
        for (int j = 0; j < primes.size(); j++)
        {
            if (i % primes[j] == 0)
            {
                isPrime = false;
                break;
            }
        }

        if (isPrime)
            primes.push_back(i);
    }
}

int main()
{
    ofstream outfile("out.txt");

    int numCases;
    cin >> numCases;

    getPrimes(32); // 10^6 takes too long. If 32 is a prime then 32^2 > 1000

    for (int i = 1; i <= numCases; i++)
    {
        int64 numFriends;
        cin >> numFriends;

        if (numFriends == 1)
        {
            outfile << "Case #" << i << ": " << 0 << endl;
            continue;
        }

        if (numFriends == 2)
        {
            outfile << "Case #" << i << ": " << 1 << endl;
            continue;
        }

        // The difference between min and max is:
        // Count of numbers that are POWERS of primes
        // And 1

        int count = 1;
        for (auto j = primes.begin(); *j * *j <= numFriends; ++j)
        {
            int64 value = *j;
            int64 logz = logX(value, numFriends) - 1;
            count += logz;
        }

        outfile << "Case #" << i << ": " << count << endl;
    }

    outfile.close();
    return 0;
}

