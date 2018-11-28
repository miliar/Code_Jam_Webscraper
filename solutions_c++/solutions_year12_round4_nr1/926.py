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
#include <utility>
#define LIMIT 0.0000001
#define inf 2000000001
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef pair<int,int> pii;

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

int position[10000], len[10000], d;
int state[10000];

int main(){
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out","w", stdout);

     int T, N;
     cin >> T;
     for(int t = 1; t <= T; t++){
          cin >> N;
          For(i, N){
               cin >> position[i];
               cin >> len[i];
          }
          cin >> d;
          For(i, N){
               state[i] = 0;
          }
          state[0] = position[0];
          for(int i = 0; i < N-1; i++){
               int j = i + 1;
               while(position[j] <= position[i] + state[i] && j < N){
                    state[j] = max(state[j], min(len[j], position[j] - position[i]));
                    j++;
               }
          }
          
          bool ans = false;
          For(i, N){
               if(position[i] + state[i] >= d)
                    ans = true;
          }
          
          printf("Case #%d: ", t);
          if(ans)
               cout << "YES" << endl;
          else
               cout << "NO" << endl;
     }

     //system("pause");
     return 0;
}
