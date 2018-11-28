#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

template <class T>
T NOD(const T& a, const T& b) {
    T n = (a>b) ? a : b;
    T m = (a<b) ? a : b;
    T tmp;
    while( m != 0 ) {
        tmp = n % m;
        n = m;
        m = tmp;
    }
    return n;
}

int main(int argc, char** argv) {
    if( argc != 2 )
        return 0;

    ifstream in( (string(argv[1])+".in").c_str() );
    ofstream out( (string(argv[1])+".out").c_str() );

    int C;
    in >> C;
    for( int i=1; i<=C; ++i ) {
        int N;
        long long ti;
        in >> N;
        vector<long long> t;
        for( int j=0; j<N; ++j) {
            in >> ti;
            t.push_back( ti );
        }
        sort(t.begin(),t.end());

        long long nod;
        if( N==2 )
            nod = t[1] - t[0];
        if( N==3 )
            nod = NOD( t[1] - t[0], t[2] - t[1] );

        long long T = 0;
        if( t[0] % nod != 0 ) {
            T = ((t[0] / nod) + 1) * nod - t[0];
        }
        out << "Case #" << i << ": " << T << endl;

    }

    return 0;
}
