#include <iostream>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
using namespace std;

class Existance {
    map< pair<unsigned int,unsigned int>, bool > lookup;
    public:
    bool exists( pair<unsigned int,unsigned int> thing ) {
        pair<map<pair<unsigned int,unsigned int>,bool>::iterator,bool> ret = lookup.insert( pair<pair<unsigned int,unsigned int>,bool>( thing, true ) );
        return !ret.second;
    }
};

int main() {
    unsigned int testcases;
    cin >> testcases;
    for ( int i = 1; i <= testcases; i++ ) {
        unsigned int A,B;
        cin >> A;
        cin >> B;
        unsigned int count = 0;
        Existance check;
        for ( unsigned int j = A; j <= B; j++ ) {
            char * cstr = (char *) malloc( 10 );
            sprintf ( cstr, "%d", j );
            string str( cstr );
            if ( str.length() <= 1 ) break;
            unsigned int num = atoi( str.c_str() );
            for ( unsigned int k = 1; k < str.length(); k++ ) {
                string newstr;
                if ( str.substr( str.length() - k, 1 ) == "0" ) continue;
                newstr.append ( str.substr( str.length() - k ) );
                newstr.append ( str.substr( 0, str.length() - k ) );
                unsigned int m,n;
                unsigned int newnum = atoi(newstr.c_str());
                if ( newnum < A || newnum > B ) continue;
                if ( newnum > num ) {
                    m = newnum;
                    n = num;
                } else {
                    m = num;
                    n = newnum;
                }
                if ( m != n && !check.exists( pair<unsigned int,unsigned int>( n, m ) ) ) {
                    count++;
                }
            }
            free( cstr );
        }
        cout << "Case #" << i << ": " << count << endl;
    }
    return 0;
}
