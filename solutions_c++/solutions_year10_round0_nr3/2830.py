/*
IN THE NAME OF ALLAH THE MOST BENEFICENT THE MOST MERCIFUL



*/



#include<iostream>
#include<fstream>
using namespace std;

void circulate(long* intPtr, long len,long num)
{
     
 long temp=0;
 
 for(long i=0;i<num;i++ )
 {    
   temp=intPtr[0];            
  for(long j=0;j<len-1;j++)     
         {
         intPtr[j]=intPtr[j+1];                            
         }
   intPtr[len-1]=temp;      
  
  }    
   

}



int main()
{
   
   
   long R=0,K=0,N=0,T=0;
   
   
      ifstream inputFile("C-small-attempt0.in");
      ofstream outFile("C-small-attempt0.out");
      inputFile>>T;
   
    for(long c=1;c<=T;c++)
    {
       
    inputFile>>R;inputFile>>K;inputFile>>N;
    
    
   
    long g[N];
    for(long i=0;i<N;i++)
    {
       inputFile>>g[i];
        
    }
    
    
    long money=0;
    for(long i=0;i<R;i++)
             {
                         
             long hold=0,j=0;
               do
                 {                 
                 hold+=g[j];j++;                                       
                 }while(hold<=K);
             hold-=g[j-1];
             money += hold;
             circulate(g,N,j-1);                                                             
                         
             }
    
    
     outFile<<"Case #"<<c<<": "<<money<<endl;
    
    
   }
    
    
    
    
    
system("pause")    ;
}
