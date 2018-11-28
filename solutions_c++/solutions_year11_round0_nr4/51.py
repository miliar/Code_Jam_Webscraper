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
    ifstream ifs( "D-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int i = 0; i < test; i++ ) {
        getline(ifs, strbuf);
        int N = atoi(strbuf.c_str());

        getline(ifs, strbuf);
        istringstream iss(strbuf);
        int n = 0;
        for ( int j = 0; j < N; j++ ) {
            int x;
            iss >> x;
            if ( x != j+1 ) {
                n++;
            }
        }
        printf( "Case #%d: %.6f\n", i+1, (double)n );
    }
    return 0;   
}
