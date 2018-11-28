#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <fstream>
#include <vector>
#include <deque>
#include <math.h>

using namespace std;

#define pos first
#define val second

int main(){
    
    FILE *in = fopen("C-small-attempt0.IN", "r");
    FILE *out = fopen("out.txt", "w");
    
    int T;
    fscanf(in,"%d", &T );
    
    for(int t = 1; t <= T; ++t ){ 
    
    int R, k, n, group, cnt = 0, tot = 0;
    fscanf(in,"%d %d %d", &R, &k, &n );
    
    deque < pair<int, int> > deq;

    for(int i = 0; i < n; ++i){
       fscanf(in,"%d", &group );
       deq.push_back( make_pair(i,group) );
    }
    
    while( cnt < R ){
           int res = 0;
           pair<int,int> now = deq.front(), init;
           init = now;

           while( res + now.val <= k ) {
                  res += now.val;
                  deq.pop_front();
                  deq.push_back(now);
                  now = deq.front();
                  if( now.pos == init.pos )break;
           }
           tot += res;
           ++ cnt;
    }

    
     fprintf(out,"Case #%d: %d\n", t, tot ); 
  }
  
    
    return 0;
}
    
    
    
    
    
    
