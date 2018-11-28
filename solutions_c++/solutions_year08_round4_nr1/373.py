#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int gates [ 15000];
int change [ 15000];
int cost0 [ 15000];
int cost1 [15000];

int min ( int a, int b) {
    if ( a < b )
    return a;
    return b;
}

int main(int argc, char *argv[])
{
    
    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        int M, V;
        cin >> M >> V;
        
        // dane
        int i;
        for ( i = 1; i <= (M-1)/2; i++) {
            int gat, chan;
            cin >> gat >> chan;
            gates[i] = gat;
            change [i] = chan;    
        }
        for ( ; i <= M; i ++) {
            int val; cin >> val;
            if ( val == 0 ) {
               cost0[i] = 0;
               cost1[i] = 99999;
               }
            else {
               cost0[i] = 99999;
               cost1[i] = 0;
            }    
        }
        for (  i = (M-1)/2 ; i > 0 ; i -- ) {
            // cost0
            int costAND0 = 99999;
            if ( gates[i] == 1) {
               costAND0 = min ( cost0 [ i *2 + 1], cost0[i*2] );     
            } 
            if ( gates[i] == 0 && change[i] == 1 ) {
               costAND0 = min ( costAND0,    1 + min (cost0[2*i], cost0[2*i+1]) );
                    
            }
            int costOR0 = 99999;
            if ( gates[i] == 0 && cost0 [ i * 2] < 99999 && cost0[i*2 + 1] < 99999 ) {
               costOR0 = min ( costOR0, cost0 [ i * 2] + cost0 [ i * 2+1] );      
            }
            if ( gates[i] == 1 && change[i] == 1 ) {
               costOR0 = min ( costOR0, 1 +  cost0 [ i * 2] + cost0 [ i * 2+1] );    
            }
           
            cost0 [ i] = min ( costOR0, costAND0);
            // cost1
            
            int costAND1 = 99999;
            if ( gates[i] == 1 && cost1 [ i * 2] < 99999 && cost1[i*2 + 1] < 99999) {
                costAND1 = cost1 [ i * 2] + cost1[i*2 + 1]  ;   
            }
            if ( gates[i] == 0 && change[i] == 1 ) {
                costAND1 = min ( costAND1,   1 +  cost1[ i * 2]+ cost1[i * 2 + 1] ); 
            }
            int costOR1 = 99999;
            if ( gates[i] == 0 ) {
               costOR1 = min ( cost1 [ i * 2] , cost1[ i * 2 + 1] );
            }   
            if ( gates[i] == 1 && change[i] == 1 ) {
               costOR1 = min ( costOR1, 1 + min ( cost1[ i * 2], cost1[i * 2 + 1] ) );     
            }
            cost1 [ i ] = min ( costOR1, costAND1 );
           // cout << " XXX " << i << " " << costOR0 << " " << costAND0 << " " << costOR1 << " " << costAND1 << endl;
        }
      
        if ( V == 0 ) {
          if ( cost0 [1] == 99999 )
             cout <<   "Case #" << testCase << ": IMPOSSIBLE" << endl;
          else 
             cout << "Case #" << testCase << ": "<< cost0[1] << endl;
          
        }
        if ( V == 1 ) {
             if ( cost1 [1] == 99999 )
             cout <<   "Case #" << testCase << ": IMPOSSIBLE" << endl;
          else 
             cout << "Case #" << testCase << ": "<< cost1[1] << endl;
        }
    }
    //cout << "done";

    
    
    return 0;
}
