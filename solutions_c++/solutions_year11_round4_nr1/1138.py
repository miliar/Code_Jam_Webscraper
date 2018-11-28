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
        istringstream iss(strbuf);
        long X, W, R, T, N;
        iss >> X >> W >> R >> T >> N;
        double sw = 0.0;
        map<long,double> m;
        for ( long i = 0; i < N; i++ ) {
            getline(ifs, strbuf);
            istringstream iss2(strbuf);
            long s, e, w;
            iss2 >> s >> e >> w;
            m[w] += e-s;
            sw += e-s;
        }
        m[0] = X-sw;

        double rr = T;
        double ans = 0.0;
        map<long,double>::iterator it = m.begin();
        for ( ; it != m.end(); ++it ) {
            double dist = it->second;
            double s = it->first;
            if ( (R+s)*rr > dist ) {
                ans += dist / (R+s);
                rr -= dist / (R+s);
            } else {
                ans += rr;
                ans +=(dist-rr*(R+s)) / (W+s);
                rr = 0;
            }
        }

        printf( "Case #%d: %.10f\n", t, ans );
    }
    return 0;   
}
