#include <iostream>
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
#include "stdio.h"
#define N 1000000
using namespace std;

struct snapper {
    bool powr;
    bool on;
} a [10 + 2];

void reset (int n)
{
    for ( int i = 0; i < n; i++ ) {
        a [i].powr = false;
        a [i].on = false;
    }
    a [0].powr = true;
}

int main ()
{

FILE *sf,*rf;

sf=fopen("i:\\abc.txt","r");
rf=fopen("i:\\output1781.txt","w+");
    int T;
    fscanf (sf,"%d", &T);
    int cases = 0;

    while ( T-- ) {
        int n;
        int k;
        fscanf (sf,"%d %d", &n, &k);

        reset (n);

        for ( int i = 0; i < k; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].powr )
                    a [j].on = a [j].on ? false : true;
            }
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].powr && a [j].on )
                    a [j + 1].powr = true;
                else
                    a [j + 1].powr = false;
            }
        }

        if ( a [n - 1].powr && a [n - 1].on )
            fprintf (rf,"Case #%d: ON\n", ++cases);
        else
            fprintf (rf,"Case #%d: OFF\n", ++cases);
    }
fclose(rf);
fclose(sf);

    return 0;
}


