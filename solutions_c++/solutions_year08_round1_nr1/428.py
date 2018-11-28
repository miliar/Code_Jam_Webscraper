/*
ID: kazastankas
PROG: saving_the_universe
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
ifstream fin("1AA-large.in");
ofstream fout("1AA-large.out");
long long cases, dimensions;
int main() {
    fin >> cases;
    // whoops forgot that it was now. Commence bathroom coding!
    for (long long i=0;i<cases;i++) {
        fin >> dimensions;
        long long vecone[dimensions];
        long long vectwo[dimensions];
        for (long long j=0;j<dimensions;j++) {
            fin >> vecone[j];
        }
        for (long long k=0;k<dimensions;k++) {
            fin >> vectwo[k];
        }
        sort(vecone,vecone+dimensions);
        sort(vectwo,vectwo+dimensions);
        long long answer=0;
        long long lastanswer=0;
        for (long long l=0;l<dimensions;l++) {
            lastanswer=answer;
            answer+=vecone[l]*vectwo[dimensions-l-1];
            //hindsight's 20-20
            if(answer<0&&lastanswer>0&&answer<=vecone[l]*vectwo[dimensions-l-1]) fout << "Fuck I overflew\n";
            if(answer>0&&lastanswer<0&&answer>=vecone[l]*vectwo[dimensions-l-1]) fout << "Fuck I overflew\n";
        }
        fout << "Case #" << i+1 << ": " << answer << endl;
    }
    return 0;
}

