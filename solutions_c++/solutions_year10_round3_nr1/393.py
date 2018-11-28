#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

#define f first
#define s second
#define MAXN 1000005

int BIT[MAXN+10];

void update( int x ){
     for(;x <= MAXN; x += x & -x)
       BIT[x]++;
}

int read( int x ){
    int ret = 0;
    for(; x > 0; x -= x & -x)
     ret += BIT[x];
    return ret;
} 


int main(){
    
    FILE *in = fopen("A-large(2).IN", "r");
    FILE *out = fopen("sol.txt", "w");
    
    int t;
    fscanf(in,"%d", &t );
    
    for(int T = 1; T <= t; ++T ){
          
          int n;
          fscanf(in,"%d", &n );
          
          memset(BIT, 0, sizeof(BIT) );
          vector < pair<int,int> > V;
          
          for(int i = 0; i < n; ++i){
              int a, b;
              fscanf(in,"%d %d", &a, &b );
              V.push_back( make_pair(a,b) );
          }
          
          sort( V.begin(), V.end() );
          
          int sol = 0;
          for(int i = V.size()-1; i >= 0; --i){
                int cross = read( V[i].s );
                sol += cross;
                update( V[i].s );
          }
          
          fprintf(out,"Case #%d: %d\n", T, sol ); 
    }
     system("Pause");
     return 0;
} 
