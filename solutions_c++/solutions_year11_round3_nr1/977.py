#include <iostream>
#include <fstream>
using namespace std;

int map[50][50];
char m[50][50];

bool checker(int i, int j,int r, int c)
{
     if ((i+1<r)&&(j+1<c))
     {
        if ((m[i][j]=='#')&&(m[i][j+1]=='#')&&(m[i+1][j]=='#')&&(m[i+1][j+1]=='#'))
        { return true; }
     }
     return false;
}       


bool sim(int r, int c)
{
     for (int i=0; i<r; i++)
     {
         for (int j=0; j<c ; j++)
         {
             if ( checker(i,j,r,c) )
             {
                 m[i][j]='/';
                 m[i][j+1]=char(92);
                 m[i+1][j]=char(92);
                 m[i+1][j+1]='/';
             }
             else if (m[i][j]=='#') {return false;}
         } }
     return true;
}

int main(){
    ifstream fin;
    ofstream fout;
    
    fin.open("a.in");
    fout.open("output.txt");
    int test=0;
    int t;
    fin>>t;
    while (test!=t)
    {
          test++;
          int row;
          int col;
          fin>>row>>col;
          memset(map, 0, sizeof(map));
          memset(m, 0, sizeof(m));
          for (int i=0; i<row; i++)
          {
              for (int j=0; j<col; j++)
              {
                  fin>>m[i][j];
                  if (m[i][j]=='#')
                  { map[i][j] = 1;}
              }
          }
          bool poss = sim(row,col);
                                       
          
          if (poss)
          {
          fout<<"Case #"<<test<<":\n";//something to add
          //cout<<"Case #"<<test<<":\n";//something to add
          for (int i=0; i< row ; i++)
          {
              for (int j=0; j<col; j++)
              { fout<<m[i][j]; //cout<<m[i][j]; 
              }
              fout<<endl; //cout<<endl; 
              }
          }
          else  {
          fout<<"Case #"<<test<<":\nImpossible\n";//something to add
          //cout<<"Case #"<<test<<":\nImpossible\n";//something to add
          }
    }
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}
