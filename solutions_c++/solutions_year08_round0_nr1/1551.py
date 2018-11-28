#include <string>
#include <iostream>
#include <map>
#include <assert.h>
using namespace std;

#define MYASSERT(a) (assert(a))
#define SIZE(e) ((int)((e).size()))
int const BIG_NUMBER = 1000000000;

int array1[100], array2[100];
int *a1, *a2;

typedef map<string, int> MyMap;
typedef MyMap::iterator MyIterator;
MyMap se_map;

void log_array( int S ) {
    cout << "array:";
    for (int i = 0; i < S; ++i)
        cout << a1[i] << " ";
    cout << endl;
}

void processCase( int case_number ) {
    // iniitialize
    int res;
    se_map.clear();

    int S;
    cin >> S;

    string seName;
    // read trailing end-of-line
    getline( cin, seName );
    for (int k = 0; k < S; ++k) {
        getline( cin, seName );
        se_map.insert( make_pair( seName, k )  );
    }

    // initilaize arrays
    for (int k = 0; k < S; ++k )
        array1[k] = 0;
    a1 = array1;
    a2 = array2;

    int Q;
    cin >> Q;
    // read trailing end-of-line
    getline( cin, seName );
    for ( int k = 0; k < Q ; ++k ) {
        getline( cin, seName );
        MyIterator found = se_map.find( seName );
        MYASSERT( found != se_map.end() );

        int curI = found->second;

        //cout << "i: " << curI << endl;
        //log_array( S );

        for ( int i = 0; i < S; ++i ) {
            // set a2[i] here
            int minv = BIG_NUMBER;
            for ( int j = 0; j < S; ++j) {
                if ( a1[j] + 1 < minv )
                    minv = a1[j] + 1;
            }
            if ( a1[i] < minv )
                minv = a1[i];

            if ( i == curI)
                a2[i] = BIG_NUMBER;
            else
                a2[i] = minv;
        }
        // switch array pointers
        swap( a1, a2 );
    }
    //log_array( S );
    res = BIG_NUMBER;
    for (int k = 0; k < S; ++k)
        if ( a1[k] < res ) res = a1[k];

    cout << "Case #" << case_number + 1 << ": " << res << endl;
}

int main() {
    //cout << "hello world" << endl;
    int case_num;

    cin >> case_num;

    //cout << case_num;
    for (int i = 0; i < case_num; ++i ) {
        processCase(i);
    }
}
