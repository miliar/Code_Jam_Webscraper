#include <iostream>
#include <cstdio>
#include <fstream>

#define size 4
using namespace std;
char arr[size][size+1];

char findRes(void) {
   bool flagT, flagW = false, flagE = false;
   int i, j, count;
   char win;
   
   for(i=0; i<size; i++) {
      count = 0;
      if(arr[i][0] ==  'T')
         win = arr[i][1];
      else
         win = arr[i][0];
      for(j=0; j<size; j++) {
         if(arr[i][j] == '.') {
            flagE = true;
            break;
         }
         if(arr[i][j] == win || arr[i][j] == 'T')
            count++;
         else
            break;
      }
      if(count == 4) {
         flagW = true;
         return win;
      }
   }
   
   for(i=0; i<size; i++) {
      count = 0;
      if(arr[0][i] ==  'T')
         win = arr[1][i];
      else
         win = arr[0][i];
      for(j=0; j<size; j++) {
         if(arr[j][i] == '.') {
            flagE = true;
            break;
         }
         if(arr[j][i] == win || arr[j][i] == 'T')
            count++;
         else
            break;
      }
      if(count == 4) {
         flagW = true;
         return win;
      }
   }
   win = 'T';
   count = 0;
   for(i=0; i<size; i++) {
      if(arr[i][i] != '.' && win == 'T') {
         win = arr[i][i];
         count++;
         continue;
      }
      if(arr[i][i] == win || arr[i][i] == 'T')
         count++;
      else
         break;
   }
   
   if(count == 4) {
      flagW = true;
      return win;
   }
   
   win = 'T';
   count = 0;
   for(i=0; i<size; i++) {
      if(arr[i][size-1-i] != '.' && win == 'T') {
         win = arr[i][size-1-i];
         count++;
         continue;
      }
      if(arr[i][size-1-i] == win || arr[i][size-1-i] == 'T')
         count++;
      else
         break;
   }
   
   if(count == 4) {
      flagW = true;
      return win;
   
   }            
   
   if(flagW == true)
      return win;
   else if(flagE == true)
      return '.';
   else
      return 'k';
}
      

int main(void) {
   freopen("A-small-attempt0.in", "r", stdin);
   freopen("A.out", "w", stdout);
   int T, i, j, k, m;
   char res;
   bool flagT;
   
   
   scanf("%d\n", &T);
   //printf("%d\n", T);
   
   
   for(j=1; j<=T; j++) {
      for(i=0; i<4; i++) {
         for(k=0; k<4; k++)
            scanf("%c", &arr[i][k]);
         scanf("\n");
      }
      
      /*for(i=0; i<4; i++) {
         for(m=0; m<4; m++) 
            printf("%c ", arr[i][m]);
         printf("\n");
      }
      printf("\n");*/
      
      res = findRes();
      printf("Case #%d: ", j);
      
      if(res == '.')
         printf("Game has not completed");
      else if(res == 'k')
         printf("Draw");
      else
         printf("%c won", res);
      printf("\n");
            
      
   }
   
   return 0;
}
