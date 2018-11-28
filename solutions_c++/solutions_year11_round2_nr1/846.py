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

int T, n;
char table[101][101];
double wp[101], owp[101], oowp[101];
int match[101], win[101];

int main(){
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out","w", stdout);
     
     cin >> T;
     For(t,T){
          cin >> n;
          For(i,n){
               win[i] = match[i] = wp[i] = owp[i] = oowp[i] = 0;
          }
          For(i,n){
               scanf("%s", table[i]);
               For(j,n){
                    match[i] += (table[i][j] != '.');
                    win[i] += (table[i][j] == '1');
               }
               wp[i] = ((double) win[i]) / match[i];
          }
          
          For(i,n){
               double temp = 0;
               For(j,n){
                    if(table[i][j] == '.' || match[j] <= 1)   continue;
                    if(table[i][j] == '1'){
                         temp += ((double)(win[j]))/(match[j]-1);
                    }
                    else{
                         temp += ((double)(win[j]-1))/(match[j]-1);
                    }
               }
               owp[i] += temp/match[i];
          }
          
          For(i,n){
               double temp = 0;
               For(j,n){
                    if(table[i][j] != '.')
                         temp += owp[j];
               }
               oowp[i] = temp/match[i];
          }
          
          printf("Case #%d:\n",t+1);
          For(i,n){
               //printf("%lf %lf %lf\n",wp[i],owp[i],oowp[i]);
               printf("%lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
          }
     }






     //system("pause");
     return 0;
}
