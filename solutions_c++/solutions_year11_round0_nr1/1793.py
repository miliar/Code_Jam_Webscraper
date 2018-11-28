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

int T, N, robot_o, robot_b;

int main(){
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out","w", stdout);
     
     scanf("%d",&T);
     for(int t = 1; t <= T; t++){
          int robot_o = 1;
          int robot_b = 1;
          int time_o = 0;
          int time_b = 0;
          
          scanf("%d",&N);
          for(int i = 0; i < N; i++){
               char robot[3];
               int position;
               scanf("%s",robot);
               scanf("%d", &position);
               if(robot[0] == 'O'){
                    time_o = max(time_o + abs(position - robot_o), time_b) + 1;
                    robot_o = position;
               }
               else{
                    time_b = max(time_b + abs(position - robot_b), time_o) + 1;
                    robot_b = position;
               }
               //printf("Debug: %d:%d  %d:%d\n", robot_o, time_o, robot_b, time_b);
          }
          printf("Case #%d: %d\n", t, max(time_o, time_b));
     }


     //system("pause");
     return 0;
}
