
                #include<iostream.h>
                #include<fstream.h>
                #include <math.h>




int  main()
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
                      outFile<<"Case #"<<i<< ": ON  \n";
                                  
                      }          
                      else 
                     {
                      outFile<<"Case #"<<i<< ": OFF \n";
                          
                      } 
                      
             
    }
    
    
    
    
    
system("pause")    ;
}




