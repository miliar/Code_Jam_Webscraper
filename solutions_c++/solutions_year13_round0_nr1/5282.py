#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    int t, i, j, k, p, p1;
    char a[4][4];
    int x1, o1, t1;
    freopen("A-large.in","r",stdin);
    
    freopen("output.txt","w",stdout);
    scanf("%d", &t);
    
    
    for (k = 1; k <= t; k++){
         p = 0;
         p1 = 0;
          for (i = 0; i < 4; i++) {
              for (j = 0; j < 4; j++) {
                  cin >> a[i][j];
                  if (a[i][j] == '.') {
                              p = 1;
                  }
              }
          }
          for (i = 0; i < 4; i++) {
              x1= 0;
              o1 = 0;
              t1 = 0;
              for (j = 0; j < 4; j++) {
                  if (a[i][j] == 'X') {
                              x1++;
                  } else if (a[i][j] == 'T') {
                         t1++;
                  } else if (a[i][j] == 'O') {
                         o1++;
                  } else {
                  }                         
              }
              if (o1 == 4 || (o1 == 3 && t1 == 1)) {
                     printf("Case #%d: O won\n", k); 
                      p1 = 1;
                  //   goto end;
              } else if (x1 == 4 || (x1 == 3 && t1 == 1)) {
                     printf("Case #%d: X won\n", k); 
                      p1 = 1;
                   //  goto end;
              } else {
              }
          }
          if (p1 == 0) {
           for (i = 0; i < 4; i++) {
              x1= 0;
              o1 = 0;
              t1 = 0;
              for (j = 0; j < 4; j++) {
                  if (a[j][i] == 'X') {
                              x1++;
                  } else if (a[j][i] == 'T') {
                         t1++;
                  } else if (a[j][i] == 'O') {
                         o1++;
                  } else {
                  }                         
              }
              if (o1 == 4 || (o1 == 3 && t1 == 1)) {
                     printf("Case #%d: O won\n", k); 
                      p1 = 1;
                    // goto end;
              } else if (x1 == 4 || (x1 == 3 && t1 == 1)) {
                     printf("Case #%d: X won\n", k); 
                      p1 = 1;
                  //   goto end;
              } else {
              }
          }
         }
         
         if (p1 == 0) {
              x1= 0;
              o1 = 0;
              t1 = 0;
           for (i = 0; i < 4; i++) {
              
             
             if (a[i][i] == 'X') {
                x1++;
             } else if (a[i][i] == 'T') {
                t1++;
             } else if (a[i][i] == 'O') {
                o1++;
               
             } else {
             }                         
              
              if (o1 == 4 || (o1 == 3 && t1 == 1)) {
                     printf("Case #%d: O won\n", k); 
                     p1 = 1;
                //     goto end;
              } else if (x1 == 4 || (x1 == 3 && t1 == 1)) {
                     printf("Case #%d: X won\n", k); 
                      p1 = 1;
              //       goto end;
              } else {
              }
          }
         }
          
         if (p1 == 0) { 
              x1= 0;
              o1 = 0;
              t1 = 0;
          for (i = 0; i < 4; i++) {
             
             
             if (a[i][3-i] == 'X') {
                x1++;
             } else if (a[i][3-i] == 'T') {
                t1++;
             } else if (a[i][3-i] == 'O') {
                o1++;
             } else {
             }                         
              
              if (o1 == 4 || (o1 == 3 && t1 == 1)) {
                     printf("Case #%d: O won\n", k); 
                      p1 = 1;
            //         goto end;
              } else if (x1 == 4 || (x1 == 3 && t1 == 1)) {
                     printf("Case #%d: X won\n", k); 
                      p1 = 1;
          //           goto end;
              } else {
              }
          }
         }
        
         if (p1 == 0) {
          if (p != 1) {
                
                printf("Case #%d: Draw\n", k); 
          } else {
                 printf("Case #%d: Game has not completed\n", k); 
          }
         }
        
    }
    
 
    return 0;
}
