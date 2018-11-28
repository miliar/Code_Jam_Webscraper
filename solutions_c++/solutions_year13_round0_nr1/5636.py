#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <bitset>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <functional>
#include <utility>
#include <ctime>
#include <numeric>
#include <iomanip>
#include <stdexcept>
#include <cmath>
#include <algorithm>

using namespace std;

#define _PRINT_(a,b) 		printf("Case #%d: %s\n",a,b)

class tic_tac   
{
   char board[4][4];
   int val[4][4][3];   //0-diagonal, 1-row, 2-col
   int dot[4][4][3][2];


   
   public:

   tic_tac()
   {
      for(int i=0; i<4;i++)
      {
           for(int j=0; j<4;j++)
           {
                board[i][j] = '.';
                for(int k =0; k<3;k++)
                {
                   val[i][j][k] = 1;
                }
           } 
      }
   }

   int isComplete()
   {
       int i, j, row=1, col=1, diag=1;

       for(i=0; i< 4; i++)
       {
          row = 1;
          for(j = 1; j<4; j++)
          {
              if(board[i][j] == board[i][j-1] || board[i][j] == '.' || board[i][j-1] == '.' || board[i][j-1] == 'T' || board[i][j] == 'T')
              {
                 row++;
      if(row == 4)
        return 0;
              }
              else 
                row =1;
          }
      }

       for(j=0; j< 4; j++)
       {
          col = 1;
          for(i = 1; i<4; i++)
          {
              if(board[i][j] == board[i-1][j] || board[i][j] == '.' || board[i-1][j] == '.' || board[i-1][j] == 'T' || board[i][j] == 'T')
              {  col++;
      if(col == 4)
        return 0;
              }
              else 
                col =1;
          }
      }

      diag = 0;
      for(i=1,j=1;i<4;i++,j++)
      {
          if(board[i][j] == board[i-1][j-1] || board[i][j] == '.' || board[i-1][j-1] == '.' || board[i-1][j-1] == 'T' || board[i][j] == 'T')
          {  diag++;
      if(diag == 4)
        return 0;
          }
          else 
             diag =1;

      }

      diag =0;  //other diag
       for(i=1,j=2; i<4; i++,j--)
       {
          if(board[i][j] == board[i-1][j+1] || board[i][j] == '.' || board[i-1][j+1] == '.' || board[i-1][j+1] == 'T' || board[i][j] == 'T')  
          {
             diag++;
      if(diag == 4)
        return 0;
          }
          else
             diag = 1;
          
       }

      return 1;
   }

  
   int add(char ch, int i, int j)
   {
      board[i][j] = ch;
 
      if(i > 0)
      {
          if(j>0)
          {   
             //diagonal
             if(val[i-1][j-1][0] == 3 && (board[i-1][j-1] == ch  || ch == 'T'  || board[i-1][j-1] == 'T' ) )
             {
                  int valid = 1;
                  if(i>1 && j >1  && board[i-1][j-1] == 'T')
                     if(board[i-2][j-2] != ch)
                        valid = 0;

                  if((ch == 'X' || board[i-1][j-1] == 'X') && valid == 1)  return 1;  //ch won
                  else if((ch == 'O' || board[i-1][j-1] == 'O') && valid == 1) return 2 ;
             }
              //increment diagoal
             else if( (board[i-1][j-1] == ch  || ch == 'T' || board[i-1][j-1] == 'T' ) && board[i-1][j-1] != '.') 
             {
                  int valid = 1;
                  if(i>1 && j >1  && board[i-1][j-1] == 'T')
                     if(board[i-2][j-2] != ch)
                        valid = 0;

                 val[i][j][0] = valid == 1?val[i-1][j-1][0] + 1:1 ;
             }

             //row
             if(val[i-1][j][1] == 3 && (board[i-1][j] == ch  || ch == 'T' || board[i-1][j] == 'T') )
             {
                  int valid = 1;
                  if(i>1  && board[i-1][j] == 'T')
                     if(board[i-2][j] != ch)
                        valid = 0;

                  if( ( ch == 'X' || board[i-1][j] == 'X') && valid == 1)  return 1;  //ch won
                  else if( ( ch == 'O' || board[i-1][j] == 'O') && valid == 1) return 2 ;

             }
              //increment row
             else if( (board[i-1][j] == ch  || ch == 'T' || board[i-1][j] == 'T') && board[i-1][j] != '.') 
             {
                  int valid = 1;
                  if(i>1  && board[i-1][j] == 'T')
                     if(board[i-2][j] != ch)
                        valid = 0;

                 val[i][j][1] = valid==1?val[i-1][j][1] + 1 :1;
             }

             //column
             if(val[i][j-1][2] == 3 && (board[i][j-1] == ch  || ch == 'T' || board[i][j-1] == 'T') )
             {
                  int valid = 1;
                  if( j >1  && board[i][j-1] == 'T')
                     if(board[i][j-2] != ch)
                        valid = 0;

                  if( ( ch == 'X' || board[i][j-1] == 'X')  && valid == 1) return 1;  //ch won
                  else if( ( ch == 'O' || board[i][j-1] == 'O') && valid == 1) return 2 ;

             }
              //increment column
             else if( (board[i][j-1] == ch  || ch == 'T' || board[i][j-1] == 'T')  && board[i][j-1] != '.' )
             {
                int valid = 1;
                  if( j >1  && board[i][j-1] == 'T')
                     if(board[i][j-2] != ch)
                        valid = 0;

                 val[i][j][2] = valid==1?val[i][j-1][2] + 1 : 1;
             }

             
          }
          else
          {
             //row
             if(val[i-1][j][1] == 3 && (board[i-1][j] == ch  || ch == 'T' || board[i-1][j] == 'T') )
             {
                  int valid = 1;
                  if(i>1  && board[i-1][j] == 'T')
                     if(board[i-2][j] != ch)
                        valid = 0;

                  if ( (ch == 'X' || board[i-1][j] == 'X')  && valid == 1) return 1;  //ch won
                  else if( (ch == 'O' || board[i-1][j] == 'O') && valid == 1) return 2 ;

             }
              //increment row
             else if( ( board[i-1][j] == ch  || ch == 'T' || board[i-1][j] == 'T')  && board[i-1][j] != '.'  )
             {
                  int valid = 1;
                  if(i>1  && board[i-1][j] == 'T')
                     if(board[i-2][j] != ch)
                        valid = 0;

                 val[i][j][1] = valid == 1? val[i-1][j][1] + 1: 1 ;
             }
                            
          }
      }
      else if(j > 0)
      {
             //column
             if(val[i][j-1][2] == 3 && (board[i][j-1] == ch  || ch == 'T' || board[i][j-1] == 'T') )
             {
                  int valid = 1;
                  if( j >1  && board[i][j-1] == 'T')
                     if(board[i][j-2] != ch)
                        valid = 0;

                  if ( (ch == 'X' || board[i][j-1] == 'X')  && valid == 1) return 1;  //ch won
                  else if ( (ch == 'O' || board[i][j-1] == 'O') && valid == 1) return 2 ;

             }
              //increment column
             else if( ( board[i][j-1] == ch  || ch == 'T' || board[i][j-1] == 'T') && board[i][j-1] != '.'  )
             {
                  int valid = 1;
                  if( j >1  && board[i][j-1] == 'T')
                     if(board[i][j-2] != ch)
                        valid = 0;

                 val[i][j][2] = valid==1?val[i][j-1][2] + 1 :1;
             }
      }  
      else
      {
            val[i][j][0] = 1;
            val[i][j][1] = 1;
            val[i][j][2] = 1;
      }

      return 0;

   }
 
   int check_other_diagonal()
   {
       int yes = 1;
       char ch;

       for(int i=1,j=2; i< 4; i++,j--)
       {
          if(board[i][j] == board[i-1][j+1] || board[i-1][j+1] == 'T' || board[i][j] == 'T')  
          {
            yes++;
             if(board[i][j] != 'T')
               ch = board[i][j];
          }
          else
             yes = 1;
          
       }

       if(yes == 4 && ch == 'X')
          return 1;
       else if(yes == 4 && ch == 'O')
          return 2;

       return 0;
         
   }

};

int main()
{
   freopen("A-small-attempt3.in","r",stdin);
	  freopen("test6.out","w",stdout);
  
  int T;
  cin>>T;
 
  //cout<<T;

  for(int k = 0; k < T; k++ )
  {
    tic_tac OBJ;
    char won = 'Z';
    char ch;
    int dot = 0;

    for(int i=0; i<4;i++)
    {
       for(int j=0;j<4;j++)
       {
         
          cin>>ch;
//          cout<<i<<j<<ch;
          if(ch!='.')
          {
             if(won != 'X' && won != 'O')
             {
//                cout<<"NOT win"<<endl;
                int who = OBJ.add(ch,i,j);
             if ( who == 1 )
             {
                 won = 'X';
  //               cout<<"win win : "<<won<<endl;
             }
             else if (who == 2)
             {
                 won = 'O';
             }
             }
          }
          else
             dot++;
       }
    }
   if(won != 'X' && won != 'O')
   {
               int who = OBJ.check_other_diagonal();
             
 
    //            cout<<"other not win"<<endl;
                if ( who == 1 )
                {
                 won = 'X';
      //           cout<<"other win win : "<<won<<endl;
                }
                else if (who == 2)
                {
                   won = 'O';
                }
    }


    if(won == 'Z' && dot == 0)
       won = 'D';
    else if(won == 'Z' && dot > 0)
    { 
       if( !OBJ.isComplete() )
         won = 'N';
       else
         won = 'D';
    }



   switch(won)
   {
     case 'X':  //_PRINT_(k+1, "X won");
                cout<<"Case #"<<k+1<<": X won"<<endl;
//                cout<<"1"<<endl;
                break;
     case 'O':  //_PRINT_(k+1, "O won");
                cout<<"Case #"<<k+1<<": O won"<<endl;
                break;
     case 'N':  //_PRINT_(k+1, "Game has not completed");
                cout<<"Case #"<<k+1<<": Game has not completed"<<endl;
                break;
     case 'D':  //_PRINT_(k+1, "Draw");
                cout<<"Case #"<<k+1<<": Draw"<<endl;         
                break;
   }

//getchar();
   
  }
  return 0;
	}

