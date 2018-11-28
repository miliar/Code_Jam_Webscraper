// @BEGIN_OF_SOURCE_CODE
// Small input verdict : Correct!
// *** Do not Copy the code *** //
// *** Valid, Only for Learning purpose *** // 

#include <iostream>
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
using namespace std;

struct snapper {
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
    FILE *infile=    freopen ("A-large.in", "r", stdin);
	FILE *outfile=    freopen ("A-large.out", "w", stdout);




    int T;
    fscanf (infile,"%d", &T);
    int cases = 0;

    while ( T-- ) {
        int n;
        int k;
        fscanf (infile,"%d %d", &n, &k);

        
        if (((k + 1) % ((int)pow(2,n))) == 0)
            fprintf (outfile,"Case #%d: ON\n", ++cases);
        else
            fprintf (outfile,"Case #%d: OFF\n", ++cases);
    }

    return 0;
}

// @END_OF_SOURCE_CODE
