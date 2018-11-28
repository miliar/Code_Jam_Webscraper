#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <list>
using namespace std;
typedef long long int64;
#define showbit(a, b) (((a) >> (b)) & 1)
#define move(n) ((1) << (n))
#define sz(x) (int)x.size()
const double eps = 1e-8;
int sgn(double x)  { return (x > eps) - (x < -eps); }


int d[105][105],Arr[105];

int dp(int l,int r) {
     if (d[l][r] != -1) {
                 return d[l][r];
     }
     
     if (l + 1 == r) {
           d[l][r] = 0;
           return d[l][r];
     }
     d[l][r] = 0x7ddddddd;
     
     for(int k = l + 1 ; k < r ; k++) {
             d[l][r] = min(d[l][r],dp(l,k) + dp(k,r) + Arr[r] - Arr[l] - 2);
     }
     return d[l][r];
}

int main() {
    freopen("C.out","w",stdout);
    
    int T,N,M;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
            memset(d,-1,sizeof(d));
            scanf("%d%d",&N,&M);
            for(int i = 1 ; i <= M ; i++) {
                    scanf("%d",&Arr[i]);
            }
            
            sort(&Arr[1],&Arr[M + 1]);
            Arr[0] = 0,Arr[M + 1] = N + 1;
            
            
            printf("Case #%d: %d\n",t + 1,dp(0,M + 1));
   
    }
    
    return 0;
}


