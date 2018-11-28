#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
int t;
int counter=1;
ifstream in("A-large.in");
ofstream out("output.txt");
in>>t;
while(t > 0)
{
   int r,c,cb = 0;
   bool yes = true;
   in>>r;
   in>>c;
   char **array;
   array = new char*[r];
   for(int a=0; a<r; a++)
   array[a] = new char[c];        

   for(int a=0; a<r; a++)
   {
      for(int b=0; b<c; b++)
      {
        in>>array[a][b];
        if(array[a][b]=='#')
        cb++;
      }        
   }
   if(cb%4 == 0)
   {
      for(int a=0; a<r; a++)
      {
          for(int b=0; b<c; b++)
          {
               if(array[a][b] == '#')
               {
                   if((a+1)<r && (b+1)<c && array[a+1][b]=='#' && array[a][b+1]=='#' && array[a+1][b+1]== '#')
                   {
                       array[a][b] = '/';
                       array[a+1][b] = '\\';
                       array[a][b+1] = '\\';
                       array[a+1][b+1] = '/';
                   }
                   else
                   {
                      yes = false;
                      break;
                   }
               }        
           } 
           if(yes == false)
           {
                break;         
           }       
       }             
     }
      else
       yes = false;
     
          
if(yes == false)
{
      out<<"Case #"<<counter<<":"<<endl;
      out<<"Impossible"<<endl;                
 }
  else
  {
     out<<"Case #"<<counter<<":"<<endl;
     for(int a=0; a<r; a++)
     {
       for(int b=0; b<c; b++)
       {
           out<<array[a][b];        
       }
       out<<endl;        
     }
  }
   t--;
   counter++;
}   
in.close();
out.close();
return 0;    
}

