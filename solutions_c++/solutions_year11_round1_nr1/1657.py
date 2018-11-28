#include<iostream>
#include<string>
#include<fstream>

using namespace std;


typedef unsigned int uint ;


int GCD( int a , int b )
{
    if( a<b )return GCD(b,a);
    if( b==1 )return 1;
    if( a%b==0 )return b ;
    
    int x ;
    
    while( b>=1 )
     {
         x=a;
         
         if( a%b==0 )return b;
         
         a=b;
         b=x%b;
         
         }
         
        return -1;
        
        }

     
int main()
{
    int numcase=0;
    int i ;
    
    int N,Pd,Pg;
    
    int num,den;
    int c=1,x=1;
    
    int win,total,p,q,r,den2;
    
    bool done;
    
    ifstream in("GCJ1.txt");
    ofstream outp("GCJO.txt");
    in>>numcase;
    //cin>>numcase;
    
    
    for( i=0;i<numcase;i++ )
     {
       N=Pd=Pg=win=total=p=q=r=0;
       c=1;
       in>>N>>Pd>>Pg;
        //cin>>N>>Pd>>Pg; 
        
        done=false;
        
        num=Pd;den=100;
        
        if( Pg==0 && Pd==0 )
         {
            outp<< "Case #" << (i+1) << ": " << "Possible" << endl;
           	cout<< "Case #" << (i+1) << ": " << "Possible" << endl;
           	continue;
           	
            }
        
        if( Pg==0 && Pd>0 )
         {
            outp<< "Case #" << (i+1) << ": " << "Broken" << endl;
           	cout<< "Case #" << (i+1) << ": " << "Broken" << endl;
           	continue;
           	
            }
        
        if( Pg==100 && Pd<100 )
         {
        outp<< "Case #" << (i+1) << ": " << "Broken" << endl;
           	cout<< "Case #" << (i+1) << ": " << "Broken" << endl;
           	continue;
           	
            }
        
                
        while( (x=GCD(Pd,den))!=1 )
         {
               x=GCD(Pd,den);
               Pd/=x;
               den/=x;
               
               }
               
        c=1;
        den2=100;
        
        while( (x=GCD(Pg,den2))!=1)
         {
               Pg/=x;den2/=x;
               
               }
               
               
               
         while( den*c<=N && !done )
          {
             
             win=c*Pd;
             total=den*c;
             c++;
                
             
            p=den2*win;q=Pg*total;r=Pg*total-den2*win;
            if( r<0 )r=-r;
            
            if( (r%GCD(p,q))==0 )
             { 
             outp<< "Case #" << (i+1) << ": " << "Possible" << endl;
             cout<< "Case #" << (i+1) << ": " << "Possible" << endl;
             done=true;
             
             }
              
              }
            
                  if(!done)    
                  {
                   outp<< "Case #" << (i+1) << ": " << "Broken" << endl;
                   cout<< "Case #" << (i+1) << ": " << "Broken" << endl;
                   }
                  
                  
                  
                  }
             
           
         
     
    
   system("pause");
    return 0;
    
}
          
