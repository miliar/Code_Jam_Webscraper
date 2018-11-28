#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <math.h>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second

typedef pair <int,int> par;
typedef long long ll;
typedef double llf;

int main(){

     freopen("A-large.IN", "r", stdin );
     freopen("sol.txt", "w", stdout );

    int test, k = 0;
    scanf("%d", &test );

    while( test-- ){
        ++ k;
        int x, s, r, n;
        double t;
        scanf("%d %d %d %lf %d", &x, &s, &r, &t, &n );

        vector <par> V;

        int p = 0;
        for(int i = 0; i < n; ++i ){
            int s, e, w;
            scanf("%d %d %d", &s, &e, &w );
            V.push_back( par( w, e - s ) );
            V.push_back( par( 0, s - p ) );
            p = e;
        }

        V.push_back( par( 0, x - p ) );
        sort( V.begin(), V.end() );

        double sol = 0.;
        for(int i = 0; i < V.size(); ++i ){
             double put = (V[i].f + r) * t;

             if( put > V[i].s ) {
                sol += V[i].s / (llf)(V[i].f + r);
                t   -= V[i].s / (llf)(V[i].f + r);
             }else{
                sol += t;
                sol += (V[i].s - put) / (llf)(V[i].f + s);
                t   = 0;
             }
        }

        printf("Case #%d: %.7lf\n", k, sol );
    }

    return 0;
}




