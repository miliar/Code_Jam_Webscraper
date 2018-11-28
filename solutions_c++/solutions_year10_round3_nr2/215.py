#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
using namespace std;


int main ( )
{
    int t; scanf("%d", &t);
    for(int it=0; it<t; it++)
    {
              int lo, hi, c; scanf("%d%d%d", &lo, &hi, &c);
              if( c == 8 ) fprintf(stderr,"%d %d %d\n", lo, hi, c);
              int kol = 1;
              long long h = lo; while( h < hi ) { h *= c; kol++; }
              lo = 1; hi = kol;
              int s = 0;
              while( hi-lo > 1 )
              {
                     s++;
                     lo = (lo+hi)/2;
              }
             // fprintf(stderr,"gotov\n");
if( c==8 )                           fprintf(stderr,"Case #%d: %d\n", it+1, s);
              printf("Case #%d: %d\n", it+1, s);
    }
    return 0;
}
