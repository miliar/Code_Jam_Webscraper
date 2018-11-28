#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
    if( argc != 2 )
        return 0;

    ifstream in( (string(argv[1])+".in").c_str() );
    ofstream out( (string(argv[1])+".out").c_str() );

    int T;
    in >> T;
    for( int i=1; i<=T; ++i ) {
        unsigned int N;
        unsigned long long K;
        in >> N >> K;
        bool result = true;
        for( int j=0; j<N; ++j ) {
            if( !( K & (1<<j)) ) {
                result = false;
                break;
            }
        }
        out << "Case #" << i << ": " << ((result) ? "ON" : "OFF") << endl;
    }
    return 0;
}
