/*
    Author : Akai
    Problem : B
*/

#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

struct node{
       double x ; int s ;
}w[10001] ;
int r[10001] ;

double d ;
int n , cases , T ;

bool cmp(const node &a , const node &b){
     return a.x < b.x ;
}

bool check(double mid){
     double Lmax = -200000000000001.0 ;
     memset(r , 0 ,sizeof(r)) ;
     for (int i = 1 ; i <= n ;i++){
         while (r[i] < w[i].s){
               r[i] ++ ;
               double lm = w[i].x - mid ;
               double rm = w[i].x + mid ;
               if (Lmax + d > rm) return 0 ;
               Lmax = max(Lmax + d , lm);
         }
     }
     return 1 ;
}

int main(){
    freopen("B-large.in" ,"r" , stdin);
    freopen("B-large.out" , "w" ,stdout);
    scanf("%d" , &T);
    while (T--){
          scanf("%d%lf" , &n , &d);
          for (int i = 1 ; i <= n ; i++) scanf("%lf%d" , &w[i].x , &w[i].s);
          sort(w + 1 , w + n + 1 , cmp);
          double L = 0 , R = 200000000000001.0 ; 
          while (L < R - 0.001){
                double mid = (L + R) / 2 ;
                if (!check(mid)) L = mid + 0.001 ; else R = mid ;
          }
          printf("Case #%d: %.2lf\n" , ++cases, R);
    }
}
