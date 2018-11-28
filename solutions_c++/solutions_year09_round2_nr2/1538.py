#include <iostream>
#include <conio.h>
#include <fstream>
#include <stdlib.h>
#include <algorithm>

using namespace std;
int compareAsc (const void * a, const void * b)
{
  return ( *(char*)a - *(char*)b );
}

uint64_t processNum(uint64_t num, int N)
{
   char buffer[25];
   sprintf(buffer,"%I64u",num);
   int len = strlen(buffer);
   
   for(int i=len-2;i>=0;i--)
   {
           //i is the corrent index corresponding to which we are deciding
           // if we swap anything..we break out of this loop and print
           int last = len-1;
           /*10029393993939393993*/
           while(last > i)
           {
                      //if(buffer[i+1]==buffer[last] && 
                      if(buffer[i]<buffer[last])
                      {
                           swap(buffer[i],buffer[last]);
                           qsort(buffer+i+1,len-i-1,sizeof(char),compareAsc);
                           cout<<"Case #"<<N+1<<": "<<buffer<<endl;
                           return 0;
                      }
                      last--;
           }
                        
   }
   qsort(buffer,len,sizeof(char),compareAsc);
   if(buffer[0]=='0')
   {
    //find out the first non zero digit and swap with it 
    for(int i=0;i<len;i++)
    {
            if(buffer[i]!='0')
            {
             swap(buffer[0],buffer[i]);
             break;
             }
    }
  }
   cout<<"Case #"<<N+1<<": ";
   for(int i=0;i<strlen(buffer);i++)
   {
           cout<<buffer[i];
           if(i==0)
           cout<<'0';
   }
   cout<<endl;
}
int main(int argc, char** argv)
{
/* Code to parse input file */
   if(argc!=2)
   {
              cout <<"\n Please enter input file name ";
              getch();
              return 0;
   }
   fstream infile(argv[1]);
   int N;
   infile>>N;
   uint64_t num;

   for(int i=0;i<N;i++)
   {
           infile>>num;
           processNum(num,i);
   }
   
   
   return 0;
}
