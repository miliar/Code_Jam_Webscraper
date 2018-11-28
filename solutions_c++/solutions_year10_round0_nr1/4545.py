#include <fstream.h>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>
#define N 1000000

struct snapper 
{
    bool power;
    bool on;
} a [10 + 2];

void reset (int n)
{
    for ( int i = 0; i < n; i++ ) {
        a [i].power = false;
        a [i].on = false;
    }
    a [0].power = true;
}

int main ()
{
    ifstream fin("entrada.in");
    ofstream fout("saida.out");
    int T;
    fin >> T;
    int cases = 0;

    while ( T-- ) {
        int n;
        int k;
        fin >> n >> k;

        reset (n);

        for ( int i = 0; i < k; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].power )
                    a [j].on = a [j].on ? false : true;
            }
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].power && a [j].on )
                    a [j + 1].power = true;
                else
                    a [j + 1].power = false;
            }
        }

        if ( a [n - 1].power && a [n - 1].on )
            fout << "Case #" << ++cases << ": ON\n";
        else
            fout << "Case #" << ++cases << ": OFF\n";
    }

    return 0;
}
