#include<vector>
#include<iostream>
#include<conio.h>
#include<string>
#include<algorithm>
#include<fstream>
#include<stdlib.h>

using namespace std;

class mytime
{
      
      public:
             int h, m;
             
             mytime()
             {
                     h = 0; m =0;
                     
                     }
              mytime( int x, int y)
             {
                     h = x; m =y;
                     
                     }
             void add( mytime & b)
             {
                  h = h+ b.h;
                  m= m+b.m;
                  
                  if(m>=60)
                  {
                           h++;
                           m-=60;
                           }
                  }
             
             int great( mytime & b )
             {
                 if(h > b.h)
                      return 1;
                 else if( h<b.h)
                      return -1;
                 
                 if( m> b.m)
                     return 1;
                 else if ( m< b.m)
                      return -1;
                 
                 return 0;
                 
                 }
             mytime diff( mytime & b)
             {
                    mytime res;
                    
                    res.h = h- b.h;
                    res.m = m - b.m;
                    if(res.m<0){
                            res.m+=60;
                            res.h--;}
                    return res;
                            
                    }
      };


class train{
      
      public:
             mytime dep, arr, readytime;
             bool prev, next;
             
             train()
             {
                     prev = false;
                     next = false;
                     //dep = mytime(0,0);
                     
                     }
                   };

int main( int argc, char* argv[])
{
    
    ifstream inf;
    //inf.open(argv[1]);
	inf.open("sec1.in");
    ofstream outf;
    //outf.open( argv[2]);
	outf.open( "sec1.out");
    
    char c;
    
    int total, caseno;
    const int size=1000;
    char line[size];
    
    
         inf>>total;
         caseno=0;

             
           
       while(total>caseno)
       {
                    //inf.getline(line, size);
                    //cout<<caseno<<" "<< line<<endl;      
                    //outf<<line<<endl;
                    
                    inf.getline(line, size);
                    
                    int readytm;
                    inf>> readytm;
                          
                    mytime ready( 0, readytm);
                    
                    int na, nb;
                    
                    inf>>na>>nb;
                                        
                    
                    int h1,m1, h2, m2;
                    
                    train a[100], b[100];
                    int i, j;
                    for(  i=0; i<na; i++)
                    {                          
												inf.getline(line, size);
                                               inf>> h1;
                                               inf.get();
                                               inf>> m1>> h2;
                                               inf.get();
                                               inf>> m2;
                                               
                                               
                                               a[i].arr = mytime(h1,m1);
                                               a[i].dep = mytime(h2,m2);
                                               a[i].readytime= a[i].dep;
                                               a[i].readytime.add( ready);
                                       
                    }
                    
                    for(  i=0; i<nb; i++)
                    {                          
                                               inf.getline(line, size);
												inf>> h1;
                                               inf.get();
                                               inf>> m1>> h2;
                                               inf.get();
                                               inf>> m2;
                                               
                                               
                                               b[i].arr = mytime(h1,m1);
                                               b[i].dep = mytime(h2,m2);
                                               b[i].readytime= b[i].dep;
                                               b[i].readytime.add( ready);
                                       
                    }
            
//                    cout<< h1<< endl<< m1<< endl<< h2<< endl << m2;
                    
                    for(  i=0; i < na; i++)
                    {
                        mytime mintime, diff;
                        mintime = mytime(23,60);
                        int minj=-1; bool found;
                        found =false;
                         for(j=0; j < nb  ; j++)
                         {
                                  
                                  if( !b[j].prev)
                                  {
                                      diff = b[j].arr.diff(a[i].readytime);
                                      if(mintime.great(diff)>=0 && diff.h>=0 && diff.m>=0)  
                                      {                          mintime = diff;
                                                                 minj=j;
                                                                 found = true;
                                                                 }
                                      
                                      }
                                  }
                                  
                         if(found){
                                   
                                   a[i].next = true;
                                   b[minj].prev= true;
                                   
                                   }
                         
                         
                         }

                         for(  i=0; i < nb; i++)
                    {
                        mytime mintime, diff;
                        mintime = mytime(23,60);
                        int minj=-1; bool found;
                        found =false;
                         for(j=0; j < na  ; j++)
                         {
                                  
                                  if( !a[j].prev)
                                  {
                                      diff = a[j].arr.diff(b[i].readytime);
                                      if(mintime.great(diff)>=0 && diff.h>=0 && diff.m>=0)
                                      {                          mintime = diff;
                                                                 minj=j;
                                                                 found = true;
                                                                 }
                                      
                                      }
                                  }
                                  
                         if(found){
                                   
                                   b[i].next = true;
                                   a[minj].prev= true;
                                   
                                   }
                         
                         
                         }
                         
                    int avla=0, avlb=0;
                    avla=0;
                    avlb = 0;
					
					for( i = 0; i < na; i++)
                    {
                            if(!a[i].prev)
                                          avla++ ;
                            
                            }

                    for( i = 0; i < nb;i++)
                    {
                            if(!b[i].prev)
                                          avlb++ ;
                            
                            }                                            
                    
                    outf<<"Case #" << caseno+1<< ": "<<avla<< " "<<avlb <<endl;
                    cout<<"Case #" << caseno+1<< ": "<<avla<< " "<<avlb <<endl;
                    
                    caseno++;
                          
					
                          }    
       
       getch();
           
           
    inf.close();
    outf.close();
    
    
	return 0;    
    }
