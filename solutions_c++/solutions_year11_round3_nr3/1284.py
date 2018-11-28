#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{   
    
    ifstream  in(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;//cout<<"test cases---------->"<<t<<endl;;
    int cases=0;
    while(cases<t)
          {   
          int n,l,h,m;    
          in>>n;
          in>>l;
          in>>h;
          int array[n];
          for(int i=0;i<n;i++)
              { 
                  in>>array[i];//cout<<array[i];
              }
          int flag=0;
          for( m=l;m<=h;m++)
            {
              flag=0;
              for(int i=0;i<n;i++)
              {  
                      
                 if((array[i]%m!=0)&&(m%array[i]!=0)){flag=1;break;}
              }
              if(flag==0)break;
            }
          
          if(flag!=0)
          {out<<"Case #"<<cases+1<<": NO"<<endl;} 
          if(flag==0)
          {out<<"Case #"<<cases+1<<": "<<m<<endl;}   
          cases++; 
          }

    
    return 1;
    
}
