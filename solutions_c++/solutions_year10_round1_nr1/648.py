#include <iostream>
#include <fstream>
using namespace std;

int N,K,T;
char Board[100][100];
int flagR,flagB;
const int Move[4][2] = {{1,0},{0,1},{1,-1},{1,1}};

bool Legal(int tx,int ty)
{
  if (tx<0) return false;
  if (tx>N-1) return false;
  if (ty<0) return false;
  if (ty>N-1) return false;
  return true;
}

int main()
{
    ifstream fin("Alarge.in");
    ofstream fou("Alarge.out");
    fin>>T;
    for (int t=1;t<=T;t++)
    {
      //Input
      fin>>N>>K;
      for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
        fin>>Board[i][j];  
      //ClockWise
      for (int i=0;i<N;i++)
      {
         int ptr,qtr;
         ptr = N-1;qtr = N-1;
         while (qtr>=0)
         {
           if (Board[i][qtr]!='.')
           {
              Board[i][ptr]=Board[i][qtr];
              if (qtr!=ptr) Board[i][qtr]='.';
              ptr--;
           }
           qtr--;
         }
      }
//      for (int i=0;i<N;i++)
//      {for (int j=0;j<N;j++) fou<<Board[i][j];
//      fou<<endl;}
      //Count K
      flagR = 0;flagB = 0; 
      for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
        if (Board[i][j]!='.')
          for (int k=0;k<4;k++)
          {
              int ptrx,ptry,tmpk;
              char key;
              ptrx=i;ptry=j;key=Board[i][j];tmpk=0;
              while (Board[ptrx][ptry]==key)
              {
                 tmpk++;
                 ptrx=ptrx+Move[k][0];
                 ptry=ptry+Move[k][1];
                 if (!Legal(ptrx,ptry))break;
              }
  //            fou<<i<<","<<j<<":"<<tmpk<<endl;
              if (tmpk==K) 
              {
                if (key=='R') flagR=1;
                       else   flagB=1;
              }
          }
      //output
      fou<<"Case #"<<t<<": ";
      if (flagR&&flagB) fou<<"Both"<<endl;
         else if (!(flagR||flagB)) fou<<"Neither"<<endl;
              else if (flagR) fou<<"Red"<<endl;
                   else       fou<<"Blue"<<endl;
    }
    fin.close();
    fou.close();
    return 0;
}
