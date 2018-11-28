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

int T, note[10001],n,l,h;

int main(){
     freopen("C-small-attempt0.in", "r", stdin);
     freopen("C-small-attempt0.out","w", stdout);
     scanf("%d",&T);
     For(t,T){
          scanf("%d%d%d",&n,&l,&h);
          for(int i = 0; i < n; i++)
               scanf("%d",&note[i]);
          printf("Case #%d: ",t + 1);
          bool isEnd = false;
          for(int freq = l; freq <= h; freq++){
               bool canUse = true;
               for(int i = 0; i < n; i++){
                    if(note[i] % freq == 0 || freq % note[i] == 0){
                    }
                    else{
                         canUse = false;
                         break;
                    }
               }
               if(canUse){
                    isEnd = true;
                    printf("%d\n",freq);
                    break;
               }
          }
          if(!isEnd)
          printf("NO\n");
     }    






     //system("pause");
     return 0;
}
