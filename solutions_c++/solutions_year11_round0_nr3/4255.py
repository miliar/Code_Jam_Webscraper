#include<iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>

using namespace std;



int main()
{
    int T=0,i=0;
    ifstream ifptr;
    ofstream ofptr;   
    ifptr.open ("C-large.in");
    ofptr.open ("A-large.out");
    ifptr>>T;
    

    
    for( i = 0; i < T; i++ )
    {
         int j=0,N=0;
         ifptr >> N;
         int min,sum,sum_xor;
         min=1000100;
         sum=0;
         sum_xor = 0;
         for( j = 0; j < N ;j++ )
         {
                   int C=0;
                   ifptr>>C;
                   sum = sum+ C;
                   sum_xor = sum_xor ^ C;
                   if ( C < min)
                    min = C;
         }
         if (sum_xor !=  0)
            ofptr<<"Case #"<<i+1<<": NO\n";
         else
            ofptr<<"Case #"<<i+1<<": "<<sum-min<<"\n";;      
          
    }
    
    ifptr.close();
    ofptr.close();
    
    getchar();
return 0;    
}
