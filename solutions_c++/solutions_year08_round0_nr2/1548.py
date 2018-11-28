#include <string>
#include <iostream>
#include <map>
#include <assert.h>
using namespace std;

#define MYASSERT(a) (assert(a))
#define SIZE(e) ((int)((e).size()))
int const BIG_NUMBER = 1000000000;

int a[24 * 60 + 60 + 1];
int b[24 * 60 + 60 + 1];

void log_array( int *pa ) {
    cout << "array:" << endl;
    for (int i = 0; i < 24*60; ++i)
        if (pa[i] != 0)
            cout << i / 60 << " " << i % 60 <<" "<< pa[i] << endl;
    cout << endl;
}


void processCase( int case_number ) {
    // iniitialize
    int res;
    memset( a, 0, sizeof( a) );
    memset( b, 0, sizeof( b) );

    int T, NA, NB;
    cin >> T;
    cin >> NA;
    cin >> NB;

    for (int i = 0; i < NA; ++i) {
        int h, m;
        char c;

        cin >> h >> c >> m;
        a[h*60+m] --;

        cin >> h >> c >> m;
        b[h*60+m + T] ++;
    }

    for (int i = 0; i < NB; ++i) {
        int h, m;
        char c;

        cin >> h >> c >> m;
        b[h*60+m] --;

        cin >> h >> c >> m;
        a[h*60+m + T] ++;
    }

    //~ log_array( a );
    //~ log_array( b );

    int minA = BIG_NUMBER;
    int trainsA = 0;
    for (int i = 0; i < 24*60; ++i) {
        trainsA += a[i];
        if (trainsA < minA ) minA = trainsA;
    }
    int minB = BIG_NUMBER;
    int trainsB = 0;
    for (int i = 0; i < 24*60; ++i) {
        trainsB += b[i];
        if (trainsB < minB ) minB = trainsB;
    }

    cout << "Case #" << case_number + 1 << ": " << -minA << " " << -minB << endl;
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
