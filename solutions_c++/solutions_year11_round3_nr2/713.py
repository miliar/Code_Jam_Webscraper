/*
LANG: C++
TASK:
author: Raviphol Sukhajoti
*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <numeric>
#include <stack>
#include <queue>
#include <set>
#define LIMIT 0.0000001
#define inf 2000000001
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

#define For(i,n) for(int i = 0; i < n; i++)
#define pb push_back
#define Sz(v) v.size()
#define It(v) typeof(v.begin())
#define Forit(it,v) for(It(v) it = v.begin(); it != v.end(); it++)
#define All(v) v.begin(), b.end()
#define getI(n) scanf("%d",&n)
#define getD(n) scanf("%lf",&n)
#define nl cout << endl
#define LL long long

long long int C, t, N, Nbooster;
int T;
long long int a[1001];
long long int normaltime[1000001];

long long int distance(int star){
     return a[star%C];
}

int main(){
     freopen("B-small-attempt4.in", "r", stdin);
     freopen("B-small-attempt4.out","w", stdout);

     scanf("%d",&T);
     For(tt,T){
          scanf("%lld%lld%lld%lld",&Nbooster, &t, &N, &C);
          For(i,C){
               scanf("%lld",&a[i]);
          }
          long long int total = 0;
          For(i,N){
               total += distance(i) * 2;
               normaltime[i+1] = total;
          }
          normaltime[0] = 0;
          long long int mx = 0;
          
          if(Nbooster == 1){
               for(int i = 0; i < N; i++){
                    if(normaltime[i] >= t)
                         mx = max(mx, distance(i));
                    else{
                         long long int buildtime = t - normaltime[i];
                         mx = max(mx, (2 * distance(i) - buildtime)/2);
                    }
               }
          }
          else if(Nbooster == 2){
               long long int savetime;
               For(i,N){
                    if(normaltime[i] >= t)
                         savetime = distance(i);
                    else{
                         long long int buildtime = t - normaltime[i];
                         savetime = (2 * distance(i) - buildtime)/2;
                    }
                    
                    mx = max(mx, savetime);
                    
                    for(int j = i+1; j < N; j++){
                         if(normaltime[j] - savetime >= t)
                              mx = max(mx, distance(j) + savetime);
                         else{
                              long long int buildtime = t - (normaltime[j] - savetime);
                              mx = max(mx, (2 * distance(j) - buildtime)/2 + savetime);
                         }
                    }
               }
          }
               
          
          printf("Case #%d: %lld\n",tt+1, (total - mx));
     }






     //system("pause");
     return 0;
}
