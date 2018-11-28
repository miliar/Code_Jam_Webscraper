#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

#define pb push_back
#define fs first
#define sc second

using namespace std;

#define FOUT


int main( void ){

#ifdef FOUT
    freopen ( "A-small-practice.in", "r", stdin);
    freopen ( "A-small.out", "w", stdout);
#endif

    int num_cases, curr_case = 1;

    scanf ("%d\n", &num_cases);


    while ( num_cases -- ){
            int n, m;

            scanf ("%d %d", &n, &m);



            if ( (m + 1) % ( ( 1 << n ) ) == 0 )
                printf ("Case #%d: ON\n", curr_case);
            else
                printf ("Case #%d: OFF\n", curr_case);

            curr_case ++;
        }



    return 0;
    }
