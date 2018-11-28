#include <vector>
#include <set>
#include <deque>
#include <string>

using namespace std;

int ni() {
    int foo;
    scanf("%d", &foo);
    return foo;
}
char board[64][64];
int main() {
   int c = ni();

   for(int i=0;i<c;i++) {
     int r,c;
     scanf("%d %d", &r, &c);

     for(int j=0;j<r;j++) {
       scanf("%s", board[j]);
     }

     for(int j=0;j<r;j++) {
       for(int k=0; k<c;k++) {
         if(board[j][k] == '#') {
           if(k+1< c && board[j][k+1] == '#' && j+1 < r && board[j+1][k] == '#' && board[j+1][k+1] == '#') {
             // make subs
             board[j][k] = '/';
             board[j][k+1] = '\\';
             board[j+1][k] = '\\';
             board[j+1][k+1] = '/';
           } else {
             printf("Case #%d: \nImpossible\n", i+1);
             goto next_test;
           }
         }
       }
     }
             
         

 
     printf("Case #%d: \n", i+1);
     for(int j=0;j<r;j++) {
       printf("%s\n", board[j]);
     }
   next_test:
     i=i;
   }
}

