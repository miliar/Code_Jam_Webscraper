#include<iostream>
using namespace std;

char board[50][50];

int main()
{
   int k,m,n;
   cin >> k;
   for (int i = 0; i < k; i ++)
   {
     cin >> m >> n;
     for (int j = 0; j < m; j++)
       for (int p = 0; p < n; p++)
         cin >> board[j][p];
     
     for (int j =0; j < m-1 ; j++)
       for (int p = 0 ; p < n-1 ; p++)
       {
         if (board[j][p] == '#' 
          && board[j][p+1] == '#' 
          && board[j+1][p] == '#' 
          && board[j+1][p+1] == '#')
          {
            board[j][p] = '/' ; 
            board[j+1][p] = '\\';
            board[j][p+1]= '\\' ;
            board[j+1][p+1]= '/' ;
          }
        }  
     bool find = false; 
     for (int j = 0; j < m; j++)
       for (int p = 0; p < n; p++)
         if (board[j][p] == '#')
           find = true;
    
    cout << "Case #" << i+1 <<": "<<endl;
     if (find == true)
       cout << "Impossible" << endl;
     else
       for (int j = 0; j < m; j++)
       {
         for (int p = 0; p < n; p++)
           cout << board[j][p]; 
           cout << endl;
       }
   }
}

