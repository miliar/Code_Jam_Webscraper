/*
    Author : Akai
    Problem :
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

int testcases , w , s1 , s2 , n , tot , t1 , t2 , r1 , r2 ;
int a[102] , b[102] , a1[102] , b1[102] ;

int main(){
   // freopen("A.in","r" , stdin);
  //  freopen("A.out", "w" , stdout);
    scanf("%d" , &testcases);
    for (int cases = 1 ; cases <= testcases ; cases++){
        scanf("%d" , &n);
        s1 = 0 ; s2 = 0;
        for (int i = 1 ; i <= n ; i++){
            char sx[3] ; 
            scanf("%s" , sx);
            scanf("%d" , &w);
            if (sx[0] == 'O') { a[++s1] = w ; a1[s1] = i ;}
             else {b[++s2] = w; b1[s2] = i ;}
        }
    a1[s1 + 1] = n + 1 ; b1[s2 +1] = n + 1; 
    a[s1+1]= n ; b[s2+1] = n ;
    t1 = 1 ; t2 = 1 ; 
    r1 = 1 ; r2 = 1 ;
    tot = 0 ;
   // system("pause");
    while (r1 <= s1 || r2 <= s2){
          tot ++ ;
          if (a1[r1] < b1[r2]){
                     if (t1 == a[r1]){
                            r1 ++ ;
                            if (t2 < b[r2]) t2 ++ ; else if 
                               (t2 > b[r2]) t2 -- ;
                     }
                     else {
                          if (t1 < a[r1]) t1 ++ ;else if 
                          (t1 > a[r1]) t1 -- ; 
                            if (t2 < b[r2]) t2 ++ ; else if 
                               (t2 > b[r2]) t2 -- ;
                     }
          }
          else {
               if (t2 == b[r2]){
                      r2 ++ ;
                          if (t1 < a[r1]) t1 ++ ;else if 
                          (t1 > a[r1]) t1 -- ;
               }else {
                          if (t1 < a[r1]) t1 ++ ;else if 
                          (t1 > a[r1]) t1 -- ; 
                            if (t2 < b[r2]) t2 ++ ; else if 
                               (t2 > b[r2]) t2 -- ;
                     }
          }
    }
    printf("Case #%d: %d\n" , cases , tot);
    }
}
