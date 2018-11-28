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

int T,C,D,V,P;
int position[200];
int value[200];

bool isPossible(double val){
     double last_position = -inf;
     for(int i = 0; i < C; i++){
          if(last_position + D > position[i] - val){
               last_position = last_position + D * value[i];
               if(last_position - position[i] > val){
                    //cout << "abort" << last_position - position[i] << endl;
                    return false;
               
               }
          }else{
               last_position = position[i] - val + D * (value[i]-1);
               if(last_position - position[i] > val){
                    //cout << "abort" << last_position - position[i] << endl;
                    return false;
               }
          }
        //  cout << last_position << endl;
     }
     return true;
}

int main(){
     freopen("B-small-attempt1.in", "r", stdin);
     freopen("B-small-attempt1.out","w", stdout);
     cin >> T;
     For(t,T){
          double ans = 1000000000;
          double last_ans = 0;
          double dif = 500000000;
          cin >> C >> D;
          For(c,C){
               cin >> position[c] >> value[c];
          }
          while(fabs(ans-last_ans) > 0.0000001){
               last_ans = ans;
               if(isPossible(ans)){
                    ans -= dif;
               }else{
                    ans += dif;
               }
               dif /= 2;
          }



         printf("Case #%d: %lf\n",t+1,ans);
         //printf("..%d\n",isPossible(0.9));
     }

     //system("pause");
     return 0;
}
