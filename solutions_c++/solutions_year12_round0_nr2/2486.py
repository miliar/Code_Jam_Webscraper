#include <cstdlib>
#include <iostream>
#include <fstream>
#include<conio.h>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    using std::string;
   using std::cout;
   using std::endl;
   using std::replace;
   
    ifstream  in(argv[1],ios::in| ios::binary);
    ifstream file(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;
    int cases=0;
    string str;
    getline(in, str ); ////appended for newline
    while(cases<t)
          {      
                  int n,s,p,x,num,t2;
                  in>>n;
                  in>>s;
                  in>>p;
                  x=0;
                  for(int c=0;c<n;c++)
                  { 
                         in>>num;
                         
                         t2=num-p;
                         if(t2>=0){
                         t2=t2/2; 
                         if((t2>=p)||(t2==p-1))x++;
                         else{
                              if((s>0)&&(t2==p-2)){x++;s--;}
                              }
                              }
                         
                  }
                  cases++;
                  out<<"Case #"<<cases<<": "<<x<<endl;
                  
          }

    
    return 1;
    
}
