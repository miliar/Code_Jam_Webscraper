/*
IN THE NAME OF ALLAH THE MOST BENEFICENT THE MOST MERCIFUL



*/


                #include<iostream>
                #include<fstream>
                #include <math.h>
using namespace std;



int main()
{
    long T=0,N=0,K=0,Power=0;
   ifstream inputFile("A-large.in");
   ofstream outFile("A-large.out");
   inputFile>>T;
   
    for(long i=1;i<=T;i++)
    {
             
         inputFile>>N;
         inputFile>>K;
         Power=pow(2,N);
         Power--;
         long result=Power&K;
         
         if(result==Power)
                      {
                      outFile<<"Case #"<<i<< ": ON"<<endl;
                                  
                      }          
                     else 
                     {
                      outFile<<"Case #"<<i<< ": OFF"<<endl;
                          
                     } 
                      
             
    }
    
    
    
    
    
system("pause")    ;
}




