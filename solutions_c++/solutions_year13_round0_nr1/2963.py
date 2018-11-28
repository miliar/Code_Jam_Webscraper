//Auther: Mohamed Asaker
//Task: Problem A. Tic-Tac-Toe-Tomek   Codejam qualification 2013
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
const int N=4;
char board[N+4][N+4];
int main()
{
    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        fout<<"Case #"<<t<<": ";
        bool filled=1;
        for(int i=0;i<N;i++)
        {
           for(int j=0;j<N;j++)
           {
              fin>>board[i][j];
              if(board[i][j]=='.')
              filled=0;
           }
        }
       char w='-';
       char diag;
       bool col,row;
       //win row col
       char W[]={'X','O'};
       for(int k=0;k<2;k++)
       {
            //row
            
            for(int i=0;i<N;i++)
            {
                row=1;
                for(int j=0;j<N;j++)
                {
                      if(board[i][j]!=W[k]&&board[i][j]!='T')
                      {
                         row=0;
                         break;
                      }
                }
                if(row)
                {
                   fout<<W[k]<<" won\n";
                   break;
                }
            }
            if(row)break;
            //col
            
            for(int i=0;i<N;i++)
            {
                col=1;
                for(int j=0;j<N;j++)
                {
                      if(board[j][i]!=W[k]&&board[j][i]!='T')
                      {
                         col=0;
                         break;
                      }
                }
                if(col)
                {
                   fout<<W[k]<<" won\n";
                   break;
                }
            }
            if(col)break;
            //diag 1
            diag=1;
            for(int i=0;i<N;i++)
            {
                
                if(board[i][i]!=W[k]&&board[i][i]!='T')
                {
                     diag=0;
                     break;
                }
            }
            if(diag)
            {
               fout<<W[k]<<" won\n";
               break;
            }
            //diag 2
            diag=1;
            for(int i=0;i<N;i++)
            {
                
                if(board[i][N-1-i]!=W[k]&&board[i][N-1-i]!='T')
                {
                     diag=0;
                     break;
                }
            }
            if(diag)
            {
               fout<<W[k]<<" won\n";
               break;
            }
            
       }
       if(row||col||diag)continue;
       if(filled)
       fout<<"Draw\n";
       else
       fout<<"Game has not completed\n";
    }
}
