#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

    ifstream in("input.in");
    ofstream out("out");

void fill(set<unsigned> &valid, unsigned size)
{
    valid.clear();
    for(unsigned i=0; i<size; i++)
        valid.insert(i);
}

void do_case(int c)
{
    unsigned S;
    
    in >> S;
    char search[200];
    
    vector<string> engines;
    
    in.getline(search, 200);
    for(unsigned s=0; s<S; s++)
    {
        in.getline(search, 200);
        engines.push_back(string(search));
    }
    
    unsigned Q;
    in >> Q;
    in.getline(search, 200);
    
    set<unsigned> valid;
    fill(valid, engines.size());
    unsigned switches = 0;
    
    for(unsigned q=0; q<Q; q++)
    {
        in.getline(search, 200);
        string query(search);
        
        vector<string>::iterator found=find(engines.begin(), engines.end(), query);
        if(found==engines.end())
            continue;
        unsigned index = found - engines.begin();
        valid.erase(index);
        if(valid.empty())
        {
            switches++;
            fill(valid, engines.size());
            valid.erase(index);
        }
    }
    
    out << "Case #" << c+1 << ": " << switches << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
