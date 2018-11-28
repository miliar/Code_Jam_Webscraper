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


long dist( long c, long target, long N ) {
    return ( c<target ? c+N-target : c-target  );
}

bool check( long col, const vector<vector<long> > poly, long N, long cur, long cols[] )
{
    if ( cur == N+1 ) {
        bool ok = true;
        for ( long i = 0; i < poly.size(); i++ ) {
            set<long> s;
            for ( long j = 0; j < poly[i].size(); j++ ) {
                s.insert(cols[poly[i][j]]);
            }
            if ( s.size() != col ) {
                ok = false;
                break;
            }
        }
        if ( ok ) {
            for ( long i = 1; i <= N; i++ ) {
                printf( "%d", cols[i] );
                if ( i != N ) printf( " " );
                else puts("");
            }
        }
        return ok;
    }

    for ( long i = 1; i <= col; i++ ) {
        cols[cur] = i;
        bool ok = check( col, poly, N, cur+1, cols );
        if ( ok ) return ok;
    }
    return false;
}

int main()
{
    ifstream ifs( "C-small-attempt0.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int t = 1; t <= test; t++ ) {
        getline(ifs,strbuf);
        istringstream iss(strbuf);
        long N, M;
        iss >> N >> M;

        vector<pair<long,long> > v(M);
        getline(ifs,strbuf);
        istringstream iss2(strbuf);
        for ( long i = 0; i < M; i++ ) {
            iss2 >> v[i].first;
        }
        getline(ifs,strbuf);
        istringstream iss3(strbuf);
        for ( long i = 0; i < M; i++ ) {
            iss3 >> v[i].second;
        }

        vector<vector<long> > vv( N+1 );
        for ( long i = 0; i < v.size(); i++ ) {
            vv[v[i].first].push_back( v[i].second );
            vv[v[i].second].push_back( v[i].first );
        }
        for ( long i = 1; i <= N; i++ ) {
            vv[i].push_back(i==N?1:i+1);
        }

        vector<vector<long> > polys;
        for ( long i = 1; i <= N; i++ ) {
            for ( long j = 0; j < vv[i].size(); j++ ) {
                vector<long> poly;
                poly.push_back(i);
                long cur = vv[i][j], prev = i;
                while ( cur != i ) {
                    poly.push_back(cur);
                    long dmin = N, next = cur;
                    long dp = dist( cur, prev, N );
                    for ( long k = 0; k < vv[cur].size(); k++ ) {
                        long d = dist( cur, vv[cur][k], N );
                        if ( d < dmin && d > dp ) {
                            dmin = d;
                            next = vv[cur][k];
                        }
                    }
                    prev = cur;
                    cur = next;
                }
                polys.push_back(poly);
            }
        }

        long col = N;
        for ( long i = 0; i < polys.size(); i++ ) {
            if ( col > polys[i].size() ) {
                col = polys[i].size();
            }
        }

        printf( "Case #%d: %d\n", t, col );
        long cols[10000];
        check( col, polys, N, 1, cols );

        long aa = 0;

    }
    return 0;   
}
