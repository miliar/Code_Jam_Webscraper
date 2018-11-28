#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

#define MAX_N           55
#define N_DIRECTION     4
#define RED             2
#define BLUE            8
#define EMPTY           0
#define BOTH            (RED | BLUE)

#define HORIZONTAL      0
#define VERTICAL        1
#define LEFT_DIAG       2
#define RIGHT_DIAG      3

int nTest;
int result;

int N, K;
int **table;
int cTable[MAX_N][MAX_N][N_DIRECTION];

int checkTable(int** table, int n, int k)
{
    memset(cTable, 0, sizeof(cTable));
    for(int i = 0; i < n; i++)
      for(int j = 0; j < n; j++) {
          // ----
          if(j > 0 && table[i][j] == table[i][j-1] && table[i][j] != EMPTY) 
               cTable[i][j][HORIZONTAL] = cTable[i][j-1][HORIZONTAL] + 1;
          if(i > 0 && table[i][j] == table[i-1][j] && table[i][j] != EMPTY) 
               cTable[i][j][VERTICAL]   = cTable[i-1][j][VERTICAL]   + 1;
          if(i > 0 && j > 0 && table[i][j] == table[i-1][j-1] && table[i][j] != EMPTY)
               cTable[i][j][LEFT_DIAG]  = cTable[i-1][j-1][LEFT_DIAG]+ 1;
          if(i > 0 && j + 1 < N && table[i][j] == table[i-1][j+1] && table[i][j] != EMPTY)
               cTable[i][j][RIGHT_DIAG] = cTable[i-1][j+1][RIGHT_DIAG]+1;
      }
    //for(int i = 0 ; i < N; i++) {
//             for(int  j = 0 ; j < N; j++)
//                 cout << cTable[i][j][HORIZONTAL] << " " ;
//             cout << endl;        
//         }
//         cout << endl; 
//    for(int i = 0 ; i < N; i++) {
//             for(int  j = 0 ; j < N; j++)
//                 cout << cTable[i][j][VERTICAL] << " " ;
//             cout << endl;        
//         }
//         cout << endl; 
//    for(int i = 0 ; i < N; i++) {
//             for(int  j = 0 ; j < N; j++)
//                 cout << cTable[i][j][LEFT_DIAG] << " " ;
//             cout << endl;        
//         }
//         cout << endl; 
//    for(int i = 0 ; i < N; i++) {
//             for(int  j = 0 ; j < N; j++)
//                 cout << cTable[i][j][RIGHT_DIAG] << " " ;
//             cout << endl;        
//         }
    int result =  0;
    for(int i = 0 ; i < n; i++)
       for(int j = 0; j < n; j++)
           for(int l = 0; l < N_DIRECTION; l++)
               if(cTable[i][j][l] == k-1) 
                   result |= table[i][j];
                   
    return result;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &nTest);
    for(int curTest = 1; curTest <= nTest; curTest++) {
         scanf("%d %d", &N, &K);
         table = new int*[N];
         for(int i = 0 ; i < N; i++) {
             char c;
             char str[MAX_N];
             int count = 0;  
             table[i] = new int[N];
             scanf("%s", &str);
             for(int j = N - 1; j >=0; j--) {
                 c = str[j];       
                 if(c == 'R') {
                      table[i][count] = RED;
                      count++;
                 } else if(c == 'B') {
                      table[i][count] = BLUE;
                      count++;
                 }
             } 
             for(int j = count; j < N; j++) table[i][j] = EMPTY;    
         }
         
         //for(int i = 0 ; i < N; i++) {
//             for(int  j = 0 ; j < N; j++)
//                 cout << table[i][j] << " " ;
//             cout << endl;        
//         }
         
         result = checkTable(table, N, K);        
         if(result == 0)     
             printf("Case #%d: Neither\n", curTest);
         else if(result == BLUE)
             printf("Case #%d: Blue\n", curTest);
         else if(result == RED)
             printf("Case #%d: Red\n", curTest);   
         else if(result == BOTH)
             printf("Case #%d: Both\n", curTest);
             
    }
 return 0;    
}
