#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        int N, curO=1, curB=1, totalT=0;
        int sO=0, sB=0;
        in >> N;
        for( int i=0; i<N; i++ ) {
            char R;
            int B;
            in >> R >> B;
            if( R=='O' ) {
                int diff=max(0,abs(curO-B)-sO)+1;
                totalT += diff;
                sO=0;
                sB+=diff;
                curO = B;
            }
            else {
                int diff=max(0,abs(curB-B)-sB)+1;
                totalT += diff;
                sB=0;
                sO+=diff;
                curB = B;
            }
        }
        //cout << "Case #" << test << ": " << totalT << endl;
        out << "Case #" << test << ": " << totalT << endl;
    }

    return 0;
}



