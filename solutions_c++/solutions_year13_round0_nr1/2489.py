#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#define DEBUG printf("TEST\n")

using namespace std;

char board[5][5];
int TC, itc, i, j, counter;

bool cek(char ch){
   int i, j, c;
   bool skip = false;
   for(i = 0; i < 4 && !skip; ++i){
      c = 0;
      for(j = 0; j < 4; ++j){
         if(board[i][j] == 'T' || board[i][j] == ch) c++;
      }
      if(c == 4){
         printf("%c won\n", ch);
         skip = true;
      }
      
      c = 0;
      for(j = 0; j < 4; ++j){
         if(board[j][i] == 'T' || board[j][i] == ch) c++;
      }
      if(c == 4){
         printf("%c won\n", ch);
         skip = true;
      }
   }
   
   c = 0;
   for(i = 0; i < 4 && !skip; ++i){
      if(board[i][i] == 'T' || board[i][i] == ch) c++;
   }
   if(c == 4){
      printf("%c won\n", ch);
      skip = true;
   }
   
   c = 0;
   for(i = 0; i < 4 && !skip; ++i){
      if(board[i][3 - i] == 'T' || board[i][3 - i] == ch) c++;
   }
   if(c == 4){
      printf("%c won\n", ch);
      skip = true;
   }
   
   return skip;
}

int main(){
   
   scanf("%d", &TC);
   for(itc = 1; itc <= TC; ++itc){
      for(i = 0; i < 4; ++i) scanf("%s", board[i]);
      printf("Case #%d: ", itc);
      
      if(cek('X'));
      else if(cek('O'));
      else{
         counter = 0;
         for(i = 0; i < 4; ++i)
            for(j = 0; j < 4; ++j)
               if(board[i][j] == '.') counter++;
         
         if(counter > 0) printf("Game has not completed\n");
         else printf("Draw\n");
      }
   }
   
   return 0;
}
