#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

/*
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>
typedef adjacency_list < listS, vecS, directedS,
    no_property, property < edge_weight_t, int > > graph_t;
typedef graph_traits < graph_t >::vertex_descriptor vertex_descriptor;
typedef graph_traits < graph_t >::edge_descriptor edge_descriptor;
typedef std::pair<int, int> Edge;
*/

using namespace std;

ifstream in("input.in");
ofstream out("out");


void do_case(int c)
{
    int n;
    vector<long> x, y;
    
    in >> n;
    
    for(int i=0; i<n; i++)
    {
        int e;
        in >> e;
        x.push_back(e);
    }
    for(int i=0; i<n; i++)
    {
        int e;
        in >> e;
        y.push_back(e);
    }
    std::sort(x.begin(), x.end());
    std::sort(y.begin(), y.end());
    
    long sum=0;
    for(int i=0; i<n; i++)
    {
        sum += x[i]*y[n-i-1];
    }
    
    out << "Case #" << c+1 << ": " << sum << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
