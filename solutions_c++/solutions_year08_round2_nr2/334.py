#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>

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

vector<unsigned long> belongs;

unsigned long A, B, P;

void unify(unsigned long a, unsigned long b)
{
    //cout << "uni " << a << " " << b << endl;
    for(unsigned long i=A; i<=B; i++)
        if(belongs[i]==b)
            belongs[i]=a;
}

bool is_prime(unsigned long p)
{
    if(p<=2)
        return true;
    if(p%2 == 0)
        return false;
    unsigned long root = sqrt(p);
    if(p == root*root)
        return false;
    for(unsigned long i=3; i<=root; i++)
        if(p % i == 0)
            return false;
    return true;
}

void do_case(int c)
{
    in >> A >> B >> P;
    belongs.resize(B+1);
    
    //cout << "case " << c << endl;
    for(unsigned long i=A; i<=B; i++)
        belongs[i]=i;
        
    for(unsigned long p=P; p<=B; p++)
        if(is_prime(p))
        {
            //cout << p << " is prime " << endl;
            unsigned long first=0;
            for(unsigned long n=p; n<=B; n+=p)
            {
                if(n<A)
                    continue;
                if(!first)
                    first = n;
                if(belongs[first]!=belongs[n])
                    unify(belongs[first], belongs[n]);
            }
            
        }


    vector<bool> counted(B+1, false);
    unsigned long sets = 0;
    
    for(unsigned long i=A; i<=B; i++)
        if(!counted[belongs[i]])
        {
            //cout << "counting " << belongs[i] << endl;
            counted[belongs[i]]=true;
            sets++;
        }
    
    out << "Case #" << c+1 << ": " << sets << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
