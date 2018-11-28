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

char table[100][100];

int main(){
     int T, R, C;
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out","w", stdout);
     cin >> T;
     For(t,T){
          cin >> R >> C;
          For(r,R){
               scanf("%s",table[r]);
          }
          For(r,R){
               For(c,C){
                    if(table[r][c] == '#'){
                         if(r + 1 < R && c + 1 < C){
                              if(table[r+1][c] == '#' && table[r][c+1] == '#' && table[r+1][c+1] == '#'){
                                   table[r][c] = '/';
                                   table[r+1][c] = '\\';
                                   table[r][c+1] = '\\';
                                   table[r+1][c+1] = '/';
                              }     
                         }
                    }
               }
          }
          bool possible = true;
          For(r,R){
               if(possible)
                    For(c,C){
                         if(table[r][c] == '#'){
                              possible = false;
                              break;                         
                         }
                    }
          }
          if(!possible)
               printf("Case #%d:\nImpossible\n",t+1);
          else{
               printf("Case #%d:\n",t+1);
               For(r,R){
                    printf("%s\n",table[r]);
               }
          }
     }

     //system("pause");
     return 0;
}
