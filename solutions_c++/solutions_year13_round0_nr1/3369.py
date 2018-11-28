#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>

using namespace std;
const char X = 'X', O='O';
char grid[4][4];
int checkRow(int row, char c)
{

   int countc = 0, countt = 0;
   for(int col = 0; col < 4; col++) {
      if(grid[row][col]==c) countc++;
      if(grid[row][col]=='T') countt++;
   }

   return (countc+countt==4);
}

int checkCol(int col, char c)
{
   int countc = 0, countt = 0;
   for(int row = 0; row < 4; row++) {
      if(grid[row][col]==c) countc++;
      if(grid[row][col]=='T') countt++;
   }
   return (countc+countt==4);
}

int checkLeftD(char c)
{
   int row=0,col=0,countc=0,countt=0;
   for(int i = 0; i < 4; i++) {
      if(grid[row][col]==c)countc++;
      if(grid[row][col]=='T')countt++;
      row++;col++;
   }
   return (countc+countt==4);
}

int checkRightD(char c)
{
   int row = 3,col=0,countc=0,countt=0;
   for(int i = 0; i < 4; i++) {
      if(grid[row][col]==c)countc++;
      if(grid[row][col]=='T')countt++;
      row--;
      col++;
   }
   return (countc+countt==4);
}

int isWinner(char c)
{
   int ok = 0;
   for(int row = 0; row < 4; row++) {
      ok = ok || checkRow(row,c);
   }
   for(int col = 0; col < 4; col++) {
      ok = ok || checkCol(col,c);
   }
   ok = ok || checkLeftD(c);
   ok = ok || checkRightD(c);

   return ok;
}



char getWinner()
{
   char c = '1';
   if(isWinner(X)) c = X;
   if(isWinner(O)) c = O;
   return c;

}

int isCompleted()
{
   for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
         if(grid[i][j]=='.') return 0;
      }
   }
   return 1;
}
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large-out.txt","w",stdout);
   int T;
   cin>>T;
   for(int tc = 1; tc <= T; tc++) {
      for(int i =0; i < 4; i++) {
         for(int j = 0; j < 4; j++) {
            cin>>grid[i][j];
         }
      }
      char c = getWinner();
      cout<<"Case #"<<tc<<": ";
      if(c==X||c==O) {
         cout<<c<<" "<<"won"<<endl;
      }else {
          if(isCompleted()) {
            cout<<"Draw"<<endl;
          }else {
            cout<<"Game has not completed"<<endl;
          }
      }
   }
   return 0;
}
