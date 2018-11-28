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
    ifstream ifs( "A-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int t = 1; t <= test; t++ ) {
        getline(ifs,strbuf);
        long n = atoi( strbuf.c_str() );
        vector<string> v;
        for ( long i = 0; i < n; i++ ) {
            getline(ifs,strbuf);
            v.push_back(strbuf);
        }

        vector<double> WP, OWP, OOWP, RPI;
        for ( long i = 0; i < n; i++ ) {
            long g = 0, w = 0;
            for ( long j = 0; j < v[i].size(); j++ ) {
                if ( v[i][j] == '1' ) w++;
                if ( v[i][j] != '.' ) g++;
            }
            WP.push_back( g?1.0*w/g:0.0 );
        }

        for ( long i = 0; i < n; i++ ) {
            double sum = 0.0;
            long cnt = 0;
            for ( long j = 0; j < v[i].size(); j++ ) {
                if ( v[i][j] == '.' ) continue;
                long g = 0, w = 0;
                for ( long k = 0; k < n; k++ ) {
                    if ( v[j][k] == '.' || k == i ) continue;
                    g++;
                    if ( v[j][k] == '1' ) w++;
                }
                sum += g?1.0*w/g:0.0;
                cnt++;
            }
            OWP.push_back( cnt?sum/cnt:0.0 );
        }

        for ( long i = 0; i < n; i++ ) {
            double sum = 0.0;
            long cnt = 0;
            for ( long j = 0; j < v[i].size(); j++ ) {
                if ( v[i][j] == '.' ) continue;
                sum += OWP[j];
                cnt++;
            }
            OOWP.push_back( cnt?sum/cnt:0.0 );
        }

        for ( long i = 0; i < n; i++ ) {
            RPI.push_back( 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] );
        }

        printf( "Case #%d:\n", t );
        for ( long i = 0; i < n; i++ ) {
            printf( "%.12f\n", RPI[i] );
        }
    }
    return 0;   
}
