#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;


int main()
{
   
   ifstream myfile("GCJ1.txt");
   ofstream outp("GCJout.txt"); 
   
   long long numCase=0,nBut=0;
   char color;
   long long num=0,i,j;
    
   long long Olead=0;
   long long Blead=0;
   
   long long Opos=1;
   long long Bpos=1;
   
   long long t=0;
   long long total=0;
   
  myfile>>numCase;
  //cin>>numCase;
   
   for( i=0;i<numCase;i++ )
   {
        myfile>>nBut ;
        
        //cin>>nBut;
        
        Olead=0,Blead=0 ;
        Opos=1,Bpos=1;
        total=0,t=0;
        num=0;
       
        
        for( j=0;j<nBut;j++ )
         {
             myfile>>color>>num ;
             //cin>>color>>num;
             
             if( color=='O' )
              {
               
               if( num>=Opos )
               {             
                 if( Opos + Olead >=num )          
                 t=1 ;
                 else
                 t=num-(Opos+Olead) + 1 ;
                 
                 }
                 
               if( num <  Opos )
               {
                if( Opos - Olead <= num )
                t= 1 ;
                else
                t=Opos - Olead-num +1 ;
                
                } 
                   
                    
                  
                 Blead+=t ; 
                 Olead=0;
                 Opos=num;
                 
                 total+=t;
                 t=0;
                 }  
                 
               if( color=='B' )
                {
                  if( num >=Bpos )
                  {            
                    if( Bpos + Blead >=num )
                     t=1;
                     else
                      t=num-(Bpos + Blead ) +1 ;
                      
                      }
                      
                     if( num < Bpos )
                      {
                         if( Bpos - Blead <= num )
                          t=1;
                          
                         else
                          t=Bpos-num - Blead +1 ;
                          
                          }
                      
                     Olead+=t;
                     Blead=0;
                     Bpos=num;
                     
                     total+=t;
                     t=0;
                     
                     }
                     
                     }
                     
                  	outp<< "Case #" << (i+1) << ": " << total << endl;
                  
	}
	
    myfile.close();	
    system("pause");
    
	return 0;
}    
        
       
          
