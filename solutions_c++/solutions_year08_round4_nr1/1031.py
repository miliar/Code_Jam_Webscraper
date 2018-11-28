#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdexcept>

typedef unsigned long long ull;
typedef long long ll;
typedef long double dd;

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

class node
{
public:
    node() {}
    node(bool op_and, bool changable, bool v=0)
        : value(v), op_and(op_and), changable(changable)
    {}
    bool value;
    bool op_and;
    bool changable;
};

void do_case(int c)
{
    unsigned M;
    bool V;
    in >> M >> V;
    vector<node> nodes;
    vector<size_t> changable;
    
    nodes.push_back(node(false, false));
    for(int i=0; i<(M-1)/2; i++)
    {
        bool G, C;
        in >> G >> C;
/*        if(V==false && G)
            C = false;
        if(V && !G)
            C = false;*/
        nodes.push_back(node(G, C));
        if(C)
            changable.push_back(nodes.size()-1);
    }
    for(int i=0; i<(M+1)/2; i++)
    {
        bool V;
        in >> V;
        nodes.push_back(node(0, 0, V));
    }
    cout << M << endl;
    cout << nodes.size() << endl;
    
    ll result = -1;
    ull max_mask = 1 << changable.size();
    if(!max_mask)
        throw(std::runtime_error("mask"));
    for(ull mask=0; mask<max_mask; mask++)
    {
        unsigned changes = 0;
        for(unsigned changer=0; changer<changable.size(); changer++)
            if(mask & (1 << changer))
            {
                nodes[changable[changer]].op_and = !nodes[changable[changer]].op_and;
                changes++;
            }

        for(int i=(M-1)/2+1; i>0; i--)
        {
            unsigned left = i*2;
            unsigned right = i*2+1;
            if(left <= M)
            {
                nodes[i].value = (nodes[i].op_and)?
                    nodes[left].value&&nodes[right].value:
                    nodes[left].value||nodes[right].value;
            }
        }
        
        if(nodes[1].value == V)
            if(result == -1 || changes < result)
                result = changes;
        
        for(unsigned changer=0; changer<changable.size(); changer++)
            if(mask & (1 << changer))
                nodes[changable[changer]].op_and = !nodes[changable[changer]].op_and;
    }
    
    out << "Case #" << c+1 << ": ";
    if(result == -1)
        out << "IMPOSSIBLE";
    else
        out << result;
    out << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
