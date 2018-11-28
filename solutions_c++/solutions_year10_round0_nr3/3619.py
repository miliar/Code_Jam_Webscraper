#include <fstream.h>
#include <stdlib.h>
#include <queue>
#include<iostream>
#include<conio.h>
using namespace std;

int main ()
{
 
  int T;  
  long long R,k,N,amount,temp,temp_sum,c,i,j,counter;
  
  ifstream fin("C-small-attempt2.in");

  ofstream fout("C-small-attempt2.out");
      
  if(!fin)
       exit(0);
  
  fin >> T;
  
  for(c = 1; c <= T; c++)
  {
         
          
          fin >> R >> k >> N;
          amount = 0;
          queue<long long> coaster;
          
          for(i = 1; i <= N; i++)
          {
              fin >> temp;
              coaster.push(temp);
          }
       
          for(j = 1; j <= R; j++)
          {
             
                
                    temp_sum = 0; 
                    temp = coaster.front();
                    counter = 1;
                    do
                    {     
                                                 
                         coaster.pop();
                         coaster.push(temp);
                          
                                     
                          temp_sum += temp;   
                          
                          temp = coaster.front();
                
                    counter++;
                           
                                  
                    }while(temp_sum + temp <= k && counter <= coaster.size());
                      
                   
                
                    
                 
                
                   amount += temp_sum;
              
                    
                    
           }              
              
                
                   
          
          fout <<"Case #" <<c << ": " << amount <<"\n";    
    }

  return 0;
}
