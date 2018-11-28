#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <fstream>

using namespace std;

map<int, set<int> > visited_cache;

bool is_happy(int value, int base, set<int>& visited ) {
    //vector<int> numbers;
    int square = 0;
    while ( value > 0 ) {
        int r = value % base;
        square += r * r;
        value /= base;
        //cout << r << " " << square << " ";
    }
    //cout << " = " << square << endl;
    if ( square == 1 ) {
        return true;
    }
    if ( visited.find( square ) != visited.end() ) {
        return false;
    }
    visited.insert( square );
    return is_happy( square, base, visited );
}

int find_happy(int num, const int* bases, map<int, int>& cache ) {
    int n = 2;
    for ( int i = 0; i < num; i++ ) {
        int b = bases[ i ];
        if ( cache.find( b ) != cache.end() ) {
            if ( cache[ b ] > n ) {
                n = cache[ b ];
            }
        } else {
            int test = 2;
//             if ( visited_cache.find( b ) == visited_cache.end() ) {
//                 set<int> visited_;
//                 visited_cache[ b ] = visited_;
//             }
            set<int> visited = visited_cache[ b ];
            for ( ;; test ++ ) {
                if ( is_happy( test, b, visited_cache[ b ] ) ) {
                    cache[ b ] = test;
                    if ( test > n ) {
                        n = test;
                    }
                    break;
                }
            }
        }
    }
    int happy_number = n;
    for ( int hv = n; ; hv++ ) {
        bool flag = true;
        for ( int i = 0; i < num; i++ ) {
            int b = bases[ i ];
            set<int> visited;// = visited_cache[ b ];
            if ( is_happy( hv, b, visited ) == false ) {
                flag = false;
                break;
//             } else {
//                 cout << hv << " is happy for base " << b << endl;
            }
        }
        if ( flag ) {
            happy_number = hv;
            break;
        }
    }
    return happy_number;
}

int main( int argc, char** argv ) {
//     set<int> c;
//     cout << is_happy( 6393, 8, c ) << endl;
//     exit( 0 );
    ifstream file_in( argv[ 1 ] );
    int N;
    string line;
    map<int, int> cache;
    getline( file_in, line );
    N = atoi( line.c_str() );
    //file_in >> N;
    for ( int cn = 1; cn <= N; cn++ ) {
        string line;
        getline( file_in, line );
        int n = 0;
        vector<int> pos;
        pos.push_back(0);
        for ( int i = 0; i < (int)line.size(); i++ ) {
            if ( line.c_str()[ i ] == ' ' ) {
                pos.push_back(i);
                n ++;
            }
        }
        int* bases = new int[ n + 1 ];
        for ( int i = 0; i <= n; i++ ) {
            bases[ i ] = atoi( line.c_str() + pos[ i ] );
            cerr << bases[ i ] << " ";
        }
        cerr << endl;
        int happy = find_happy( n + 1, bases, cache );
        cout << "Case #" << cn << ": " << happy << endl;
        delete[] bases;
        //file_in >> line;
    }
    return 0;
}

