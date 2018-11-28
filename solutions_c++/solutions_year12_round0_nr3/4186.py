/* C. Recycled Numbers [filename: C_small.cpp]

           Codejam :: Qualification Round 2012
          ---------------------------------------------

                      Written in C++ Programming
       Tested and Compiled - Microsoft Windows 7 / Dev-C++ v4.9

*/

/******************************************************
           WRITTEN BY K21G [K-piXjuv-G]
           
         [ nepal.mountpk@msdnnepal.net ]
               [ puncoz@live.com ]
       [ http://www.facebook.com/puncoz ]
*******************************************************/

#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int rotate(int,int);

int main()
 {
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  
  int T;
  cin>>T;
  
  for(int i=0; i<T; i++)
   {
    int A,B;
    cin>>A>>B;
    
    if(A<10 && B<10)
     cout<<"Case #"<<(i+1)<<": 0"<<endl;
     
    else
     {
      int len = (B-A) +1;
      int range[len+1];
      int n,m;
      
      for(int j=0; j<len; j++)
       {
        range[j] = A+j;   
       } 
       
       int count = 0; 
      for(int j=0; j<len; j++)
       {
        n = range[j];
        m = range[j];
        
        int length = int(log10(float(range[j])) +1); 
        
        for(int k=0; k<length; k++)
         {
          m = rotate(range[j],(k+1));
          
          if ((A <= n) && (n < m) && (m <= B))
            {
             count++;
            }    
         }    
       }
      cout<<"Case #"<<(i+1)<<": "<<count<<endl;   
     }   
   }
      
  return 0;    
 }
 
int rotate(int num, int n)
 {
  int len = int(log10(float(num)) +1); //to find length of number
     
  int digit[len+1];
  
  for(int i=0; i<len; i++)
   {
    digit[i] = num%10;
    num = num/10;    
   }
   
  int temp;
  for(int k=0; k<n; k++)
   {
    temp = digit[0];
    for(int i=0; i<(len-1); i++)
     {
      digit[i] = digit[i+1];    
     } 
    digit[len-1] = temp;
   }    
  
  int numF = 0;
  for(int i=0; i<len; i++)
   {
    numF += digit[i] * int(pow(float(10),float(i)));    
   }
     
  return numF;
 }
