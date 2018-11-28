#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>

using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)

ifstream in("A-large.in"); ofstream out("A-large.out");

int T[10][3], N, l=1;
string game[4], result, s;
bool flag = false;


int main()
{
   map<char, int> M;
   M['T']=0, M['O']=1, M['X']=2;
   
   in>>N;
   while(N--)
   {
     if(flag) out<<endl; flag = true;
     in>>game[0]>>game[1]>>game[2]>>game[3];
     result = "Draw";
     
     REP(i,4) REP(j,4) 
              {
              if(game[i][j] =='.') result = "Game has not completed";
              else 
              {T[i][M[game[i][j]]]++; T[j+4][M[game[i][j]]]++; 
              if(i==j) T[8][M[game[i][j]]]++; 
              if(i+j==3) T[9][M[game[i][j]]]++;
              }
              }
     REP(i,10) { 
               if(T[i][1]==4 || (T[i][1]==3 && T[i][0] == 1)) {result = "O won"; break;}
               if(T[i][2]==4 || (T[i][2]==3 && T[i][0] == 1)) {result = "X won"; break;}
               }
     out<<"Case #"<<l<<": "<<result;
     memset(T,0, sizeof T);
     getline(in,s); l++;
     
              
}
}
