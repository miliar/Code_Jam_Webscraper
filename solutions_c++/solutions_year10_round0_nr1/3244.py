#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;


int main(){
    
    FILE *in  = fopen("A-large.IN", "r");
    FILE *out = fopen("sol.txt", "w"); 
    
    int T;
    fscanf(in,"%d", &T );
    
    for(int t = 1; t <= T; ++t ){
    
       int n, k;
       fscanf(in,"%d %d", &n, &k );
    
       int pot_light = 1;
       for(int i = 0; i < n; ++i) pot_light <<= 1;
       -- pot_light;
    
       k -= (pot_light);
       while( k > 0 ) k -= pot_light + 1;
    
       if( k == 0 )fprintf(out,"Case #%d: ON\n", t);
       else fprintf(out,"Case #%d: OFF\n", t);
    }
    
    return 0;
} 
