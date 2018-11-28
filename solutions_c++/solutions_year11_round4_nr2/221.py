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
const double eps = 0.00000001 ;
double w[15][15] ;
char s1[101] ;
int testcases , cases  ,  n , m , k1 , ans ;

int main(){
    freopen("B-small-attempt0.in" , "r" , stdin);
    freopen("B-small-attempt0.out" , "w" ,stdout);
    scanf("%d" , &testcases);
    while (testcases--){
          ans = 0 ;
          scanf("%d%d%d" , &n , &m , &k1);
          for (int i = 1 ; i <= n ; i++){
              scanf("%s" , s1);
              for (int j = 1 ; j <= m ; j++){
                  w[i][j] = double(s1[j-1] - '0');
              }
          } 
          for (int i = 1 ; i < n ; i++)
              for (int j = 1 ; j < m ; j++)
                  for (int k = 2 ; k + j <= m && k + i <= n ; k++){
                      double MidX = k * 1.0 / 2 + i * 1.0 , MidY = k * 1.0 / 2 + j * 1.0 ;
                      double SX = 0 , SY = 0 ;
                      for (int l = i ; l <= k + i ; l++)
                          for (int v = j ; v <= k + j ; v++) if ((l != i && l != k + i) || (v != j && v != k + j)){
                              SX = SX + (l * 1.0 - MidX) * w[l][v] ;
                              SY = SY + (v * 1.0 - MidY) * w[l][v] ;
                          }
                      if (fabs(SX) < eps && fabs(SY) < eps) ans = max(ans , k);
                  }
          printf("Case #%d: " , ++cases);
          if (ans == 0) puts("IMPOSSIBLE") ; else printf("%d\n" , ans+ 1);
    }
}
