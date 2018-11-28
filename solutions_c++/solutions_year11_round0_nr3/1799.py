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

int N,T;
int price[1000];
int sum;
bool state[1000];

//int gen(int pos){
//     if(pos < N){
//          state[pos] = 0;
//          int temp = gen(pos+1);
//          state[pos] = 1;
//          return max(temp, gen(pos+1));
//     }
//     
//     int ret = 0;
//     int condition1 = 0;
//     int condition2 = 0;
//     For(i, N)
//          if(state[i]){
//               ret += price[i];
//               condition1 ^= price[i];
//          }else{
//               condition2 ^= price[i];
//          }
//          
//     return (condition1 == condition2 && ret != sum)? ret : -1;
//}

int main(){
     
     
     freopen("C-large.in", "r", stdin);
     freopen("C-large.out","w", stdout);
     scanf("%d",&T);
     for(int t = 1; t <= T; t++){
          sum = 0;
          int condition = 0;
          scanf("%d",&N);
          for(int i = 0; i < N; i++){
               scanf("%d",&price[i]);
               condition ^= price[i]; 
               sum += price[i];
          }
          if(condition != 0){
               printf("Case #%d: NO\n",t);
          }
          else{
               int mn = inf;
               for(int i = 0; i < N; i++){
                    mn = min(mn, price[i]); 
               }
               printf("Case #%d: %d\n",t,sum-mn);
          }
     }

     return 0;
}
