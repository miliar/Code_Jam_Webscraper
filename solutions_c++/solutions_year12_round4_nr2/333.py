/*
     Author : Akai
     Problem :
     Time :
*/
#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
#include<cmath>
#include<algorithm>
#define PI acos(-1.0)

using namespace std ;

struct dx{
       int r , s ,x , y ;
}a[1007] ;
int n , w , l ;
int ansx[1007] , ansy[1007] ;
int d[1007] ;

int T , t , cases , cnt , now , next ;

bool cmp(const dx &a , const dx &b){
     return a.r  > b.r ;
}

double dis(int x , int y , int x2 , int y2){
       return (sqrt(1.0*((long long)(x-x2)*(long long)(x-x2)+(long long)(y-y2)*(long long)(y-y2)))) ;
}

int main(){ 
    freopen("B-large.in" , "r" , stdin);
    freopen("B-large.out" , "w" , stdout);
    scanf("%d" , &T);
    while (T--){
          scanf("%d%d%d" , &n , &w , &l);
          memset(a,  0, sizeof(a)) ;
          printf("Case #%d: ", ++cases);
          int t = 0 ;
          if (w < l){
                t = 1 ;
                swap (w , l);
          }   
          for (int i = 1 ; i <= n ; i++){
              scanf("%d" ,&a[i].r) ;
              a[i].s = i ;
          }
          for (int i = 1 ; i <= n ; i++) d[i] = a[i].r ;
              sort(a + 1 , a + n + 1 , cmp);
          next = 0 ;
          cnt = 0 ; now = 0 ;
          for (int i = 1 ; i <= n ; i++){
              if (cnt > w) puts("no science!");
              if (now == 0){
                   //   printf("%d %d XXX\n" , a[i].r , next); 
                   //   if (next + a[i].r > w) puts("no science!") ;
                      next += a[i].r ;
              }
          //   printf("%d\n" , next);
         //    printf("%d\n" ,cnt);
           //   if (a[i].r + now > r) return ;
            //  if (a[i].r + cnt > l) puts("no science!");
              a[i].x = cnt ; 
              a[i].y = now ;
              now += a[i].r ;
              now += a[i+1].r  ;
              //printf("%d %d\n" , now , a[i].r); 
              if (now  > l){
                      now = 0 ;
                      next += a[i+1].r ;
                      cnt = next ;
              }
           }
           for (int i = 1 ; i <= n ; i++) if (t != 1){
               ansx[a[i].s] = a[i].x ;
               ansy[a[i].s] = a[i].y ;
               }else {
               ansy[a[i].s] = a[i].x ;
               ansx[a[i].s] = a[i].y ;
               }
               for (int i = 1 ; i < n ; i++)
           printf("%d.0 %d.0 " , ansx[i] , ansy[i]) ;
           printf("%d.0 %d.0\n" , ansx[n] , ansy[n]);
         /*  for (int i = 1 ; i <= n ; i++)
               for (int j = i + 1;  j<= n ; j++) if (dis(ansx[i] , ansy[i] , ansx[j] , ansy[j]) < 1.0*(d[i] + d[j])-0.000001)
                   printf("%d %d %d %d %d %d %d %d\n" , i , j , ansx[i] , ansy[i] , ansx[j] , ansy[j], d[i] , d[j]);*/
    }
}            
              
              
