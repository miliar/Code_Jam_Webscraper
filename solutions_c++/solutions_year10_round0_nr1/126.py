#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <cstdio>
#include <fstream>
using std::vector;
using std::map;
using std::pair;
using std::make_pair;
using std::cout;
using std::cin;
using std::endl;
using std::set;
using std::string;
using std::ifstream;
using std::ofstream;


int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int T;
    fin >> T;

    for(int t = 0; t < T; t++) {
        int N,K;
        fin >> N >> K;
        K++;        

        fout << "Case #" << t+1 << ": "
             << ((K % (1 << N))? "OFF" : "ON") << endl;
    }
    fin.close();
    fout.close();

    return 0;
}
