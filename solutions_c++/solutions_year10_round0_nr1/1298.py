#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("A-large.in",ios::in);
    out.open("ap.out",ios::out);
    int N,K,i,j,T,t;
    bool ON;
	char temp;
    in >> T;
    for (t=1;t<=T;t++)
    {
        in>>N>>K;
        ON=true;
        for (i=0;i<N;i++) if (((K>>i)%2)==0) {ON=false;};
        
        if (ON)
     	{
         	out<<"Case #"<<t<<": "<<"ON"<<"\n";
        }
        else
        {
            out<<"Case #"<<t<<": "<<"OFF"<<"\n";
        };

    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
