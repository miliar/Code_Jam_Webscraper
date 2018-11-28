#include<iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;




int main()
{
    
   ifstream myfile("GCJ2.txt");
   ofstream outp("GCJfout.txt");   
  
  string X;
  int numCases=0,i,j,k;
  int C,D,N,r;
  
  char ch,prev,x,y,z;
  bool done;
  

  myfile>>numCases;
  
  for(i=0;i<numCases;i++ )
   {
         
      myfile>>C;
      j=k=0;
      X.clear();
      D=N=r=0;
      done=false;
      
      ch=prev=x=y=z=0;
     
      pair<char,char>p;
      map<pair<char,char>,char> M;
      map<char , char > V;
      
                 
      if( C>0 )
      {
          
          for(j=0;j<C;j++ )
           {
               myfile>>x>>y>>z;
               p.first=x;
               p.second=y;
               
               M[p]=z;
               
              
              p.first=y;
              p.second=x;
              
               M[p]=z;
               
               }}
               
       myfile>>D;
       
       if( D>0 )
        {
           for( j=0;j<D;j++ )
            {
                myfile>>x>>y;
                
                V[x]=y;
                V[y]=x;
                
                }
                
                }
                
       myfile>>N ;
       for( j=0;j<N;j++ )
       {
        myfile>>ch;
        X.push_back(ch); 
        }
        
      
     
       
       
    /*--------------------------------------------------------------------*/   
       
       for( j=1;j<N;j++ )
        { 
         prev=X[j-1];
        
         while( j<N && ( prev=='0') )
          {
             prev=X[j];
             j++;
             
             }
             
         
            
           ch=X[j];
           p.first=prev;
           p.second=ch;
               
          
         
             
             
           if( M[p]>='A' && M[p]<='Z' )
           {
               X[j]=M[p];
               X[j-1]='0';
               
              
             
               continue;
               }
               
         
          p.first=ch;
          p.second=prev;
          
            
         
          
          if( M[p]>='A' && M[p]<='Z' )
          {
             X[j]=M[p];
             X[j-1]='0';
            
             continue;             
             }
         
         done=false;    
          for( k=j-1;k>=0;k-- )
           {
              
               if( V[X[k]]==X[j] )
                {
                    for( r=j;r>=0;r-- )  /*>=k*/
                     X[r]='0';
                     
                    done=true;
                     }
                     
                    
                    
                    if(done)
                    {
                       j++;
                       break;
                       } 
                     }
                     
                     }
                    
                    
              
     /*------------------------------------------------------------------------------*/
     
    int c=0;
    
    outp<< "Case #" << (i+1) << ":  " << "[" ; 
    
     for(j=0;j<X.size();j++ )
      {
          if( X[j]!='0' )
           {
             if( c==0 )
              outp<<X[j];
             else
              outp<<", "<<X[j];
                                         
              c++;
              
              }
              
              }
              
                            
          outp<<"]"<<endl;
          
          }
         
         myfile.close();
         outp.close(); 
         system("pause");
         return 0;
          
            
          
          }                  
        
         
                
                
       
               
           
               
               
               
               
      
        
  
  
  
  
  
                 
           
                 
         
