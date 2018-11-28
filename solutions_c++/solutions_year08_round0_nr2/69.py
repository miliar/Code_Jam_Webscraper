#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <utility>
#include <stdexcept>
// range_ex
#include <boost/range/algorithm.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;

    ifstream in("input.in");
    ofstream out("out");

int read()
{
    int hr, min;
    in >> hr;
//    cout<<hr<<endl;
    char c;
    in.get(c);
    if(c!=':') throw std::runtime_error("crap : != " + boost::lexical_cast<string>(c) + "(" + boost::lexical_cast<string>(int(c)) + ")");
    in >> min;
//    cout<<min<<endl;
    
    return hr*60+min;
    
}

void process(int T, int N, vector<int> &leaver, vector<int> &arriver)
{
    for(int i=0; i<N; i++)
    {
        int leaves = read();
        int arrives = read() + T;
        
        for(int t=leaves; t<60*24; t++)
            leaver[t]++;
        for(int t=arrives; t<60*24; t++)
            arriver[t]--;
    }
}

void do_case(int c)
{
    int T;
    in >> T;
    
    int NA, NB;
    in >> NA >> NB;
    
    vector<int> ADebt(60*24), BDebt(60*24);
    
    process(T, NA, ADebt, BDebt);
    process(T, NB, BDebt, ADebt);
    
    int Aneeds = *boost::max_element(ADebt);
    int Bneeds = *boost::max_element(BDebt);
    
    out << "Case #" << c+1 << ": " << Aneeds << " " << Bneeds << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
