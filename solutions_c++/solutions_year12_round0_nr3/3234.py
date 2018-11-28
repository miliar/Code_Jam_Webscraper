#include <fstream>
#include <iostream>
#include <conio.h>
#include <strings.h>
using namespace std;
char * rotates(int len, char *s)
{
          char temp; 
          temp=s[0];   
          for(int j=0;j<len-1;j++)
             s[j]=s[j+1];
          s[len-1]=temp;
          return s;   
}
int main()
{
     int T;     
     int len,a,b,count;     
     ifstream fi("qualify3.in");
     ofstream fo("qualify3.out");     
     char A[10],B[10];
     char temp[10];
     fi>>T;
     for(int i=0;i<T;i++)
     {
          fi>>A>>B;
          a=atoi(A);
          b=atoi(B);
          count=0;
          len=strlen(A);     
          for(int n=a;n<b;n++)// for each n
          {   
               itoa(n,A,10);   
               for(int m=n+1;m<=b;m++) // and a given 'm' which is equal to B's value  , we check if m or any rotation of m gives n   (provided m>n initially)
               {                   
                   if(strcmp(A,itoa(m,B,10))==0) 
                   {
                        count++;     
                   }
                   else
                   {                        
                        strcpy(temp,B); //store B's original value
                        do
                        {
                               if(strcmp(A,rotates(len,B))==0)
                               {
                                   count++;
                                    break;         
                               }                              
                        }while(strcmp(temp,B));         
                   }      
               }               
          }
     fo<<"Case #"<<i+1<<": "<<count<<endl;
     }
     fi.close();
     fo.close();
     cout<<"completed";          
     getch();     
     return 0;     
}
