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

int A,B;
char upBound[10];
set <int> ans[2000005];

void tes(int x){
     char n[10], m[10];
     sprintf(n, "%d", x);
     vector <string> v;
     
     FOR (i, 1, strlen(n)){
         int a = 0;
         if ( n[i] == '0' ) continue;
         FOR (j, i, strlen(n)){
             a *= 10;
             a += (n[j]-'0');    
         }    
         FOR (j, 0, i){
             a *= 10;
             a += (n[j]-'0');    
         }
         sprintf(m, "%d", a);
         if ( strcmp(m, n) > 0 ){
            ans[x].insert(a);
         }
     }               
}

int main(){
    freopen("inputcb.in", "r", stdin);
    freopen("outputcb.out", "w", stdout);
    int tcase = 0;
    int t; scanf("%d", &t);
    
    FOR (i, 1, 2000001) tes(i);
    
    while (t--){
          scanf("%d %d", &A, &B);
          int ret = 0;
          FOR (i, A, B+1){
              FOREACH (it, ans[i]){
                      if ( (*it) <= B ) ret++;        
              }    
          }       
          
          printf("Case #%d: %d\n", ++tcase, ret);
    }
    return 0;
}
