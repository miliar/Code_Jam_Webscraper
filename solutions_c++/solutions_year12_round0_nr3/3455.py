#include<iostream>
#include<fstream>
using namespace std;
int main()
{
     int n,a,b,i,x,y,count=0,j,z,g;
     ifstream fil;
    ofstream dd;
    fil.open("E:\\google\\q3\\C-small-attempt0.in");
    dd.open("E:\\google\\q3\\abc.out");
     fil>>n;
     for (i=0;i<n;i++)
         {count=0;
                      fil>>a>>b;
                      if (b<100)
                      for (j=a;j<b;j++)
                      {
                          y=j%10;
                          x=j/10;
                          x+=(y*10);
                          if ( x<b && x>j)
                             count++;
                      }
                      
                      else
                      {
                         
                         
                           for (j=a;j<b;j++)
                         {
                          z=j%10;
                          g=j/10;
                          g+=(z*100);
                          if ( g<=b && g>j)
                            count++;
                       
                          y=j%100;
                          x=j/100;
                          x+=(y*10);
                          if ( x<=b && x>j)
                                count++;
                         }
                         
                      }
           dd<<"Case #"<<i+1<<": "<<count<<endl;           
         }
 fil.close();
 dd.close();
return 0;
}
                         
