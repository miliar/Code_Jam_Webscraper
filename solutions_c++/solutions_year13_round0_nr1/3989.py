#include <cstdio>
#include <iostream>
#include <istream>
#include <ostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>

using namespace std;

bool end;

char board[4][4];

ofstream outfile;

void checkdiag(){
      short xcount = 0;
     short ocount = 0;
     for (int i = 0; i < 4; i++){
               switch ( board[i][i] ) {
                    case 'X':
                         xcount++;
                         break;
                    case 'O':
                         ocount++;
                         break;
                    case 'T':
                         {
                                  xcount++;
                                  ocount++;
                         }
                         break;
                    }
             }
         if (xcount == 4){
            outfile <<"X won"<<endl;
            return;
            }
         else
             if (ocount == 4){
                outfile <<"O won"<<endl;
                return;
             }
         xcount = 0;
         ocount = 0;
          for (int i = 0; i < 4; i++){
               switch ( board[3-i][i] ) {
                    case 'X':
                         xcount++;
                         break;
                    case 'O':
                         ocount++;
                         break;
                    case 'T':
                         {
                                  xcount++;
                                  ocount++;
                         }
                         break;
                    }
             }
         if (xcount == 4){
            outfile <<"X won"<<endl;
            return;
            }
         else
             if (ocount == 4){
                outfile <<"O won"<<endl;
                return;
             }
             
         if (end)
         outfile << "Draw"<<endl;
         else
         outfile << "Game has not completed"<<endl;
         return;
         }
         
void checkrow(){
      short xcount;
     short ocount;
     for (int i = 0; i < 4; i++){
         xcount = 0;
         ocount = 0;
         for (int j = 0; j < 4; j++){
             switch ( board[j][i] ) {
                    case 'X':
                         xcount++;
                         break;
                    case 'O':
                         ocount++;
                         break;
                    case 'T':
                         {   
                                  xcount++;
                                  ocount++;
                         }
                         break;
                    }
             }
         if (xcount == 4){
            outfile <<"X won"<<endl;
            return;
            }
         else
             if (ocount == 4){
                outfile <<"O won"<<endl;
                return;
             }
         }
         checkdiag();
         return;
}

void checkcolumn(){
     short xcount ;
     short ocount ;
     short tcount ;
     short totalcount = 0;
     for (int i = 0; i < 4; i++){
         xcount = 0;
         ocount = 0;
         for (int j = 0; j < 4; j++){
             switch ( board[i][j] ) {
                    case 'X':
                         xcount++;
                         break;
                    case 'O':
                         ocount++;
                         break;
                    case 'T':
                         {        tcount = 1;
                                  xcount++;
                                  ocount++;
                         }
                         break;
                    }
             }
         if (xcount == 4){
            outfile <<"X won"<<endl;
            return;
            }
         else
             if (ocount == 4){
                outfile <<"O won"<<endl;
                return;
             }
             else
         totalcount = totalcount + xcount+ocount;
         }
         if (totalcount-tcount == 16)
            end = true;
            else end = false;
         checkrow();
         return;
}

int main () {
  ifstream myfile;
  string line;
  outfile.open("outputA.txt");
  myfile.open("exampleA.txt");
  getline(myfile,line);
  int n;
  istringstream(line) >> n;
  for (int i = 0; i < n; i++){
      for (int j = 0; j < 4; j++){
          getline(myfile,line);
          for(int k = 0; k < 4; k++){
                  board[j][k] = line[k];
                  }
          }
          getline(myfile,line);
          end = false;
          outfile <<"Case #"<<i+1<<": ";
      checkcolumn();
      }
  myfile.close();
  outfile.close();
  system("pause");
  return 0;
}
