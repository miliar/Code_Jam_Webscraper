#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main(){
    int T, i;
    long val, N, K;

    ifstream fin("A-large.in");
    ofstream fout("large.out");

    fin >> T;

    for(i=1; i <= T; i++){
        fin >> N >> K;

        val = ((long)pow( 2.0, (double)N ) ) - 1;

        if((K >= val) && (val==K || (K-val)%(val+1)==0)){
            fout << "Case #" << i << ": ON" << endl;
        }
        else {
            fout << "Case #" << i << ": OFF" << endl;
        }
    }
}