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

int testcases , cases , a1 , a2 , L , top ;
bool flag; 
char s1[40][40] , s2[40][40] , s3[400] , ans[400] ;

int main(){
    //freopen("B.in" , "r" , stdin);
    //freopen("B.out" , "w", stdout);
    scanf("%d" , &testcases);
    for (cases = 1 ; cases <= testcases ; cases++){
          scanf("%d" , &a1);
          for (int i = 1 ; i <= a1 ; i++)scanf("%s" , s1[i]);
          scanf("%d" , &a2);
          for (int i = 1 ; i <= a2 ; i++)scanf("%s" , s2[i]);
          scanf("%d" , &L);
          scanf("%s" , s3); 
          memset(ans , 0 ,sizeof (ans));
          top = 0 ;
          for (int i = 0 ; i < L ; i++){
              ans[++top] = s3[i] ;
              while (top > 1){
                    flag = 0 ;
                    for (int j = 1 ; j <= a1 ; j++) if (s1[j][0] == ans[top] && s1[j][1] == ans[top - 1] 
                        || s1[j][0] == ans[top-1] && s1[j][1] == ans[top]){
                              flag = 1 ;
                              top -- ;
                              ans[top] = s1[j][2] ;
                              break; 
                        }
                    if (!flag) break ;
              }
              while (top > 1){
                    flag = 0 ;
                    for (int i = top - 1 ; i >= 1 ; i --){
                        for (int j = 1 ; j <= a2 ; j++) if (s2[j][0] == ans[i] && s2[j][1] == ans[top]
                            || s2[j][0] == ans[top] && s2[j][1] == ans[i]){ 
                                        flag = 1 ;
                                        top = 0 ;
                                        break ;
                            }
                        if (flag) break ;
                    }
                    if (!flag) break ;
              }
          }
          printf("Case #%d: [" , cases);
          if (top > 0)
          for (int i = 1 ; i < top ; i++) printf("%c, " , ans[i]);     
          if (top > 0)printf("%c" , ans[top]);  
          printf("]\n");
    }
}
