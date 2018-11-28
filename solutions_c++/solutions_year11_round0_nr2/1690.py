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

int D, C, T, N;
char combine[100][5];
char oppose[100][5];
char str[150];

set<char> waiting;

void print(vector<char> v){
     printf("[");
     if(!v.empty())
          printf("%c",v[0]);
     for(int i = 1; i < v.size(); i++){
          printf(", %c", v[i]);
     }
     printf("]\n");
}

int main(){
     freopen("B-large.in", "r", stdin);
     freopen("B-large.out","w", stdout);
     scanf("%d", &T);
     for(int t = 1; t <= T; t++){
          scanf("%d", &C);
          for(int i = 0; i < C; i++){
               scanf("%s", combine[i]);            
          }
          for(int i = 0; i < C; i++){
               combine[i + C][0] = combine[i][1];
               combine[i + C][1] = combine[i][0];
               combine[i + C][2] = combine[i][2];
          }
          
          scanf("%d", &D);
          for(int i = 0; i < D; i++){
               scanf("%s", oppose[i]);          
          }
          for(int i = 0; i < D; i++){
               oppose[i + D][0] = oppose[i][1];
               oppose[i + D][1] = oppose[i][0];
          }
          
          C*=2;
          D*=2;
          
          scanf("%d", &N);
          scanf("%s", str);
          vector<char> item;
          for(int i = 0; i < N; i++){
               bool isCombined = false;

               if(!item.empty()){
                    char back = item.back();
                    for(int j = 0; j < C; j++){
                         if(combine[j][0] == back && combine[j][1] == str[i]){
                              item.pop_back();
                              item.pb(combine[j][2]);
                              isCombined = true;
                              break;
                         }
                    }
               }    
               
               if(isCombined) continue;
               
               bool isOppose = false;
               for(int j = 0; j < D; j++){
                    if(oppose[j][0] == str[i]){
                         for(int k = 0; k < item.size(); k++){
                              if(oppose[j][1] == item[k]){
                                   item.clear();
                                   isOppose = true;
                                   break;
                              }
                         }
                         if(isOppose)   break;
                    }     
               }
               if(isOppose) continue;
               
               item.pb(str[i]);
          }
          printf("Case #%d: ",t);
          print(item);
     }
     
     //system("pause");
     return 0;
}
