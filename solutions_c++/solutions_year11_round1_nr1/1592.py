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

int T , x , y , z , cases ; 

int gcd(int x , int y){
    if (x % y == 0) return y; else return (gcd(y , x % y)) ;
}

int main(){
    //freopen("A.in" , "r" , stdin);
   // freopen("A.out" , "w" , stdout);
    scanf("%d" , &T);
    while (T--){
          scanf("%d%d%d" , &x , &y , &z);
          printf("Case #%d: " , ++cases);
          if (y != 100 && z == 100){ 
                puts("Broken");
                continue ;
          }
          if (y != 0 && z == 0){
                puts("Broken");
                continue ;
          }
          if (y == 0){ puts("Possible"); continue ;}
          if (x >= 100){
                puts("Possible");
                continue ;
          }
          bool flag = 0 ;
          int tmp = gcd(100 , y);
          tmp = 100 / tmp ;
          if (x >= tmp) flag = 1 ;
          
          if (flag) puts("Possible"); else puts("Broken");
    }
}
