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

unsigned long long n, A, B, C, D, x0, y0, M;

unsigned long long what(unsigned long long x, unsigned long long y)
{
//    cout << x << ", " << y << endl;
    return(x%3) + 3*(y%3);
}

bool ok(int first, int second, int third)
{
    return (first+second+third) % 3 == 0;
}

unsigned long long factn_k(unsigned long long n, unsigned long long left)
{
    if(left==0)
        return 1;
    else
        return factn_k(n-1,left-1)*n;
}

unsigned long long fact(unsigned long long n)
{
    if(n==0)
        return 1;
    else
        return fact(n-1)*n;
}

unsigned long long choose (unsigned long long n, unsigned long long k)
{
    if(n<k)
        return 0;
    return factn_k(n,k)/fact(k);
}

void do_case(int c)
{
    in >> n >> A >> B>>C>>D>>x0>>y0 >> M;

    vector<unsigned long long> cases(3*3, 0);
    
    unsigned long long X, Y;
    X = x0;
    Y = y0;
    
    cases[what(x0, y0)]++;
    for (unsigned long long i = 1; i<n; i++)
    {
      X = (A * X + B) % M;
      Y = (C * Y + D) % M;
        cases[what(X, Y)]++;
    }
    unsigned long long count = 0;
    
    for(int first=0; first<9; first++)
        for(int second=first; second<9; second++)
            for(int third=second; third<9; third++)
            {
                if(!ok(first/3, second/3, third/3))
                    continue;
                if(!ok(first%3, second%3, third%3))
                    continue;
                //cout << "ok: " << first << second << third << endl;
                unsigned long long cnt1 = cases[first];
                unsigned long long cnt2 = cases[second];
                unsigned long long cnt3 = cases[third];
                if(!cnt1 || !cnt2 || !cnt3)
                    continue;
                if(first == second && second == third)
                {
                    count += choose(cnt1, 3);
                }
                else if (first == second)
                    count += choose(cnt1, 2)*cnt3;
                else if (second == third)
                    count += choose(cnt2, 2)*cnt1;
                else
                    count += cnt1*cnt2*cnt3;
            }
    
    out << "Case #" << c+1 << ": " << count << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
