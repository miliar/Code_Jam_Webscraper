#include <iostream>
#include <sstream>
#include <string>
#include <vector>
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
    in.open("B-large(2).in",ios::in);
    out.open("ap.out",ios::out);
    long long T,result,i,j,t,L,P,C,tm;
    
    in >> T;
    for (t=1;t<=T;t++)
    {
        in>>L>>P>>C;
        tm=0;
        do {L*=C; tm++;} while (L<P);
        result=0;
//        out<<"tm="<<tm<<"; ";
        while (tm>1)
        {
          result++;
          if (tm%2) {tm/=2; tm++;}
          else tm/=2;
        };
        out<<"Case #"<<t<<": "<<result<<"\n";
    };

    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
