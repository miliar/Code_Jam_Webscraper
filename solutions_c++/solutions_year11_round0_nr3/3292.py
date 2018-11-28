#include <cstdlib>
#include <iostream>
#include <fstream>

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
    in>>t;
    
    int cases=0;
    while(cases<t)
           {
            int n;int min=9999999;
            in>>n;
            int sum=0,xum=0;
            for(int i=0;i<n;i++)
                  {
                  
                   int t;
                   in>>t;
                   if(t<min)min=t;
                   xum=xum^t;
                   sum=sum+t;
                  }
                  
            if(xum!=0)out<<"Case #"<<cases+1<<": "<<"NO"<<endl;
              else{
                      out<<"Case #"<<cases+1<<": "<<sum-min<<endl;
                   }
            cases++;
           
           }
    return 1;
    
    
    
    
}
