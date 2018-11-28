#include<iostream>
#include<string>
#include<fstream>

using namespace std;


int SubsetGen( int V[] , int sz  )
{
     int n=1<<sz ;
     int i,j;
     
     long long x,y,sum,max;
     
     x=sum=max=0;
     
     for( i=0;i<n;i++ )
      {
          sum=x=y=0;
         
          for( j=0 ; j<sz ; j++ )
           {
               if( i& (1<<j) )
                 {
                    x^=V[j] ;
                    sum+=V[j];
                 }
                else 
                y^=V[j]; 
                 }
                 
       if( (x!=0) && ( x==y ) )
        {
            if( max < sum )
             max=sum;
             
             }          
       
      
       
        
        }
        
        return max;
        
        }
        
int main()
{
    
    
    
    int numCases,T=0,i,j=0,k,n;
    int S[15];
    
    
    ifstream myfile("GCJ3.txt");
    ofstream outp("GCJ3out.txt"); 
    
    
    myfile>>numCases;
    //cin>>numCases;
    
    for(i=0;i<numCases;i++ )
    {
      myfile>>n;
      //cin>>n;
      
      for( k=0;k<n;k++ )
       {
          myfile>>S[k];
          //cin>>S[k];
          }
       
            
    for( j=0;j<n;j++ )
     T^=S[j];
      
        
          
    int retv=SubsetGen( S ,n);
    
    if( retv==0 )
    outp<< "Case #" << (i+1) << ": " <<"NO" << endl;
    else
    outp<< "Case #" << (i+1) << ": " <<retv << endl;
      //cout<< "Case #" << (i+1) << ": " <<retv << endl;
     }
     
     
    myfile.close();
    outp.close();
   
  
    return 0;
    
}
                  
