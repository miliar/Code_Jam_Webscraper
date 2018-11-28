
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <stdio.h>
#include <math.h>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)

/* @BEGIN_OF_SOURCE_CODE */
/* ID:   carloxavier86   "A.Snapper Chain"   C++   "Hanoi Towers Recurrence Relation" */

#define NAME "A-large"
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)


int main(int argc, char** argv) {
    freopen(NAME ".in","r",stdin);
    freopen(NAME ".out","w",stdout);
    int tests;
    scanf("%d",&tests);
    REP(i, tests) {
        int n,k;
        scanf("%d%d",&n,&k);
        
        double rsol = pow((double)2,(double)n)-1;

        if(k == rsol) cout << "Case #" << i+1 << ": " << "ON" << endl;
        else if ( k > rsol){
            int j = rsol
            , posible; //almacena el valor posible de encender la lampara mas cercano a k

            while(j <= k) {
                posible = j;
                j += rsol + 1;
            }
            
            if( posible == k) cout << "Case #" << i+1 << ": " << "ON" << endl;
            else cout << "Case #" << i+1 << ": " << "OFF" << endl;
        }else
            cout << "Case #" << i+1 << ": " << "OFF" << endl;

    }


    return (EXIT_SUCCESS);
}

