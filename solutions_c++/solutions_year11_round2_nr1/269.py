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

double WP[1001] , OWP[1001] , OOWP[1001] ;
char s[201][201] ;
int T , n ,cases ;

double get(int x , int i){
       int Cnt = 0 , Sum = 0 ;
       for (int j = 0 ; j < n ;j++) if (j + 1 != x){
           if (s[i][j] != '.')
           Sum ++ ;
           if (s[i][j] == '1') Cnt ++ ;
       }
       return (double)Cnt / Sum ;
}
           

int main(){
    freopen("A-large.in" , "r" ,stdin);
    freopen("A-large.out" ,"w" ,stdout);
    scanf("%d" , &T);
    while (T--){
          scanf("%d" , &n);
          for (int i = 1 ; i <= n ; i++) scanf("%s" , s[i]);
          for (int i = 1 ; i <= n ; i++)
              WP[i] = get(0 , i);
          double Sum = 0 ;
          for (int i = 1 ; i <= n ; i++){
              double sum = 0 , cnt = 0 ;
              for (int j = 1 ; j <= n ; j ++) if (j != i && s[i][j-1]!='.'){
                  
                  cnt += get(i , j);
             //     if (i == 4) printf("%lf %d\n" , get(i , j) , j);
                  sum += 1 ;
              }
              OWP[i] = cnt / sum ; 
          }
          for (int i = 1 ; i <= n ; i++){
              double sum = 0 , cnt = 0 ;
              for (int j = 1 ; j <= n ; j ++) if (j != i && s[i][j-1]!='.'){
                  cnt += OWP[j] ;
                  sum += 1 ;
              }
              OOWP[i] = cnt / sum ; 
          }
         // for (int i = 1 ; i <= n ;i++) printf("%lf %lf %lf\n" ,
         //    WP[i], OWP[i] , OOWP[i]);
          printf("Case #%d:\n" , ++cases);
          for (int i = 1;  i <= n ;i++) printf("%.8lf\n" ,
              WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25);
    }
  //  system("pause");
} 
