#include<iostream>
#include<fstream>
using namespace std;
int main()
{
     int n,a,b,i,x,y,count=0,j,z,g,f,k,u;
     ifstream fil;
    ofstream dd;
    
                                
                         y=j%1000;
                          x=j/1000;
                          x+=(y*1000);
                          if ( x<=b && x>j && x!=g)
                                count++;
                                
                         y=j%10000;
                          u=j/10000;
                          u+=(y*100);
                          if ( u<=b && u>j)
                                count++;
                                
                         y=j%100000;
                          k=j/100000;
                          k+=(y*10);
                          if ( k<=b && k>j && k!=x)
                                count++;
                         } 
                          else 
                        for (j=a;j<b;j++)
                         {
                          z=j%10;
                          g=j/10;
                          g+=(z*1000000);
                          if ( g<=b && g>j)
                            count++;
                       
                          y=j%100;
                          x=j/100;
                          x+=(y*100000);
                          if ( x<=b && x>j)
                                count++;
                                
                         y=j%1000;
                          x=j/1000;
                          x+=(y*10000);
                          if ( x<=b && x>j && x!=g)
                                count++;
                                
                         y=j%10000;
                          u=j/10000;
                          u+=(y*1000);
                          if ( u<=b && u>j)
                                count++;
                         y=j%100000;
                          k=j/100000;
                          k+=(y*100);
                          if ( k<=b && k>j && k!=u)
                                count++;
                          y=j%1000000;
                          x=j/1000000;
                          x+=(y*10);
                          if ( x<=b && x>j)
                                count++;       
                         } 
                  
                         
          dd<<"Case #"<<i+1<<": "<<count<<endl;           
         }
 fil.close();
 dd.close();
return 0;
}
                         
