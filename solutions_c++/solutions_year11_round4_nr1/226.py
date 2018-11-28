/*
    Author : Akai
    Problem : A
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

int testcases , cases , N ;
double X , S , R , t , st , ed ,tot ;
struct cr{
       double w , s ;
}a[1000007] ; 

bool cmp(const cr &a, const cr &b){
     return (a.w < b.w);
}

int main(){
    freopen("A-large.in" , "r" ,stdin);
    freopen("A-large.out" , "w" ,stdout);
   // freopen("A-small-attempt0.in" , "r" ,stdin);
   // freopen("A-small-attempt0.out" , "w" ,stdout);
    scanf("%d" , &testcases);
    while (testcases --){
          scanf("%lf%lf%lf%lf%d" , &X , &S,  &R , &t , &N);
          for (int i = 1 ; i <= N ; i++){ 
              scanf("%lf%lf%lf" , &st , &ed ,  &a[i].w);
              a[i].s = fabs(ed - st);
          }
          sort(a + 1 , a + N + 1 , cmp) ;
          for (int i = 1 ; i <= N ; i++)X = X - a[i].s ;
          a[0].s = X ;
          tot = 0 ;
          for (int i = 0 ; i <= N ; i++){
              if (t > 0){
                    double tmp = a[i].s / (a[i].w + R);
                    if (tmp <= t){
                             t = t - tmp ;
                             tot = tot + tmp ;
                    }
                    else {
                         tot = tot + t ;
                       //  cout << a[i].s << endl ;
                         double ts = a[i].s - (a[i].w + R) * t ;
                       //  cout << ts << endl ;
                         tot = tot + ts / (a[i].w + S) ;
                         t = 0 ;
                    }
              }
              else tot = tot + a[i].s / (a[i].w + S);
           //    printf("%lf\n" , tot);
          }
          printf("Case #%d: %.8lf\n" , ++cases , tot);
    }
} 
