#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

static const int N = 101;
char ibuffer[N];
typedef map<string, int> mapt;

mapt::iterator max(mapt &m) {
    int max = numeric_limits<int>::min();
    mapt::iterator it;
    for(mapt::iterator i= m.begin(); i != m.end(); i++){
        if( i->second == -1) return i;
        if( i->second > max ){ 
            max = i->second;
            it = i;
        }
    }
    return it;
}

mapt::iterator choose(mapt &s, vector<string> &q, int x = 0){
    for(mapt::iterator i = s.begin(); i!=s.end(); i++)
        i->second = -1;

    for(int i = x; i < q.size(); i++){
        if( s[ q[i] ] == -1 )
            s[ q[i] ] = i;
    }
   
    return max(s);
}

int process_case(ifstream &in){
    in.getline(ibuffer, N);
    int s = atoi(ibuffer);

    mapt search_engines;
    while (s){
        in.getline(ibuffer, N);
        search_engines[string(ibuffer)] = -1;
        s--;
    }

    in.getline(ibuffer,N);
    int nqueries = atoi(ibuffer);
    vector<string> queries(nqueries, "");
    for(int i = 0; i < nqueries; i++){
        in.getline(ibuffer, N);
        queries[i] = string(ibuffer);
        if( search_engines[ queries[i] ] == -1 )
            search_engines[ queries[i] ] = i;
    }

    if(max(search_engines)->second == -1)
        return 0;

    int changes = 0;
    mapt::iterator choosen = choose(search_engines, queries);
    if(choosen->second == -1) return changes;
    for(int i = 0; i < nqueries; i++){
        cout << choosen->first << endl;
        if( queries[i] == choosen->first ){
            changes++;
            choosen = choose(search_engines, queries, i);
        }
    }


    for(mapt::iterator i=search_engines.begin(); 
            i != search_engines.end(); i++){
        cout << i->first << " " << i->second << endl;
    }

    return changes;
}

int main (int argc, char **argv) {
    
    ofstream out;
    ifstream in;
    if(argc < 2) {
        cerr << "Usage: " << argv[0] << " <input filename> [output filename]\n";
        return -1;
    } else {
        in.open(argv[1]);
    }
    
    if(argc > 2){
        out.open(argv[1]);
    } else {
        out.open("out.dat");
    }

    in.getline(ibuffer, N);
    int ncases = atoi(ibuffer);

    for(int i = 0; i < ncases; i++){
        int x = process_case(in); 
        out << "Case #" << (i+1) << ": " << x << endl;
    }

    out.close();
}

