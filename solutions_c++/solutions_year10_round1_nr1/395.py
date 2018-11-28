#include <iostream>
#include <fstream>

using namespace std;

int main()
{
 ifstream fin("D:\A-large.in");
    ofstream fout("D:\A-large.out");
    int T, K, N;
    fin >> T;
    char  table [50][50];
    char  newtable[50][50];
    
    for (int i = 1 ; i <= T ; i++)
    {
        fin>> N >> K;   
        
        char c;
        for (int a = 0 ; a < N ; a++)
            for (int b = 0 ; b < N ; b++)
            {
                
                fin >> table[a][b];
//                if ( c == '.')
//                   table[j][k] = 0;
//                else if (c == 'B')
//                     table[j][k] = 1;
//                else if (c == 'R')
//                     table[j][k] = -1;
//                fout << table[a][b];
            }
            
       for (int a = 0 ; a < N ; a++)       
           for (int b = 0 ; b < N ; b++)
           {
               newtable[a][b] = table[N-1-b][a];
           }
           
       memset(table, '.', sizeof(char)*50*50);
       for (int a = 0 ; a < N ; a++)
       {
           int count = 0;    
           for (int b = N-1 ; b>= 0 ;b--)
               if (newtable[b][a] != '.')
               {
                  count++;
                  table[N-count][a] = newtable[b][a];
               }                      
       }
               
       bool bluecheck = false;
       bool redcheck = false;
       
       for (int a = 0 ; a < N ; a++)
       {
           for (int b = 0 ; b <= N-K; b++)
           {
               char who = table[N-1-b][a];
               if (who == '.') break;
               
               bool check = true;
               for (int c = b ; c < b+K ; c++)
               {
                   if (table[N-1-c][a] != who)
                   {
                      check = false;
                      break;
                   } 
               }
               if (check)
               {
                  if (who == 'B') bluecheck = true;          
                  if (who == 'R') redcheck = true;
               }                                           
           }               
       }  
       for (int a = 0 ; a < N ; a++)
       {
           for (int b = 0 ; b <= N-K; b++)
           {
               char who = table[N-1-a][b];
               if (who == '.') break;
               
               bool check = true;
               for (int c = b ; c < b+K ; c++)
               {                   
                                   
                   if (table[N-1-a][c] != who)
                   {
                    
                      check = false;
                      break;
                   } 
               }
               if (check)
               {
                         
                  if (who == 'B') bluecheck = true;          
                  if (who == 'R') redcheck = true; 
               }                                           
           }               
       }      
       
       for (int a = K-1 ; a < N ; a++)
       {
           for (int b = 0 ; b <= N-K; b++)
           {
               char who = table[a][b];
               if (who == '.') break;
               
               bool check = true;
               for (int c = 0 ; c < K ; c++)
               {
                   if (table[a-c][b+c] != who)
                   {
                      check = false;
                      break;
                   } 
               }
               if (check)
               {
                  if (who == 'B') bluecheck = true;          
                  if (who == 'R') redcheck = true;
               }                                           
           }               
       } 

       for (int a = K-1 ; a < N ; a++)
       {
           for (int b = K-1 ; b < N ; b++)
           {
               char who = table[a][b];
               if (who == '.') break;
               
               bool check = true;
               for (int c = 0 ; c < K ; c++)
               {
                   if (table[a-c][b-c] != who)
                   {
                      check = false;
                      break;
                   } 
               }
               if (check)
               {
                  if (who == 'B') bluecheck = true;          
                  if (who == 'R') redcheck = true;
               }                                           
           }               
       }                          
        
       fout << "Case #" << i << ": ";
       if (bluecheck && redcheck) fout << "Both" << endl;
       else if (!bluecheck && !redcheck) fout << "Neither" << endl;
       else if (bluecheck && !redcheck) fout << "Blue" << endl;
       else if (!bluecheck && redcheck) fout << "Red" << endl;                     

    }
       
}
