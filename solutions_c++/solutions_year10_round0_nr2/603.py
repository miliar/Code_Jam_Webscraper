#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
#include <math.h>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int gcd(int a, int b)
{
  int c=1;
  while (b>0)
  {
        c=a;
        a=b;
        b=c%b;        
   };
   return a;
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("B-small-attempt0.in",ios::in);
    out.open("ap.out",ios::out);
    int c,C,t[3],N,i,j,d,result;
    in >> C;
    for (c=1;c<=C;c++)
    {
        in>>N;
        for (i=0;i<N;i++) in>>t[i];
        if (N==3)
        {
            d=gcd(gcd(abs(t[0]-t[1]),abs(t[1]-t[2])),abs(t[0]-t[2]));
        }
        else
        {
          d=abs(t[0]-t[1]);
        };
//        out<<"d="<<d<<"\n";
        if ((t[1]%d)==0)
        {
          result=0;  
        }
        else
        {
            result=d-(t[1]%d);           
        };
        out<<"Case #"<<c<<": "<<result<<"\n";
        

    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
