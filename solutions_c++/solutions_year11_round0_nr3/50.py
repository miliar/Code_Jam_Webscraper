#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ifstream ifs( "C-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int i = 0; i < test; i++ ) {
        getline(ifs, strbuf);
        int N = atoi(strbuf.c_str());
        getline(ifs, strbuf);
        istringstream iss(strbuf);
        int m = 10000000, sum = 0, x = 0;
        for ( int j = 0; j < N; j++ ) {
            int c;
            iss >> c;
            x ^= c;
            sum += c;
            if ( c < m ) m = c;
        }

        if ( x ) {
            printf( "Case #%d: NO\n", i+1 );
        } else {
            printf( "Case #%d: %d\n", i+1, sum - m );
        }
    }
    return 0;   
}
