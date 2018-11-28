#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define FOR(i,a,n) for(int i=a,_n=n; i<_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

int min_val(int x){
    if ( x == 0 || x == 1 ) return x;
    if ( x % 3 == 0 ) return x/3;
    else if ( x % 3 == 1 ) return (x/3)+1;
    else if ( x % 3 == 2 ) return (x/3)+1;    
}

int max_val(int x){
    if ( x == 0 || x == 1 ) return x;
    if ( x % 3 == 0 ) return (x/3)+1;
    else if ( x % 3 == 1 ) return (x/3)+1;
    else if ( x % 3 == 2 ) return (x/3)+2;    
}

int main(){
    freopen("inputb.in", "r", stdin);
    freopen("outputb.out", "w", stdout);
    int t; scanf("%d", &t);
    int tcase = 0;
    
    while (t--){
          int n, s, p; scanf("%d %d %d", &n, &s, &p);
          int ret = 0;
          FOR (i, 0, n){
              int x; scanf("%d", &x);
              if ( min_val(x) >= p ) ++ret;
              else if ( max_val(x) >= p ){
                   if ( s > 0 ){
                      ++ret;
                      --s;     
                   }     
                   else continue;
              }   
          }
          
          printf("Case #%d: %d\n", ++tcase, ret);
    }
    return 0;
}
