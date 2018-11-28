#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
    ofstream out;
    out.open("out.txt");
    ifstream in;
    in.open("A-large.in");
    double x,y,z,a,b;
    
    in>>x;
    
    for(double i=0;i<x;i++)
    {
            
            in>>y;
            in>>z;
            
            a=pow(2.0,y);
            
            b=a-1;
            
            if((int)z%(int)a==b)
            out<<"Case #"<<(i+1)<<": ON\n";
            
            else
            out<<"Case #"<<(i+1)<<": OFF\n";
            
    }
    
    system("pause");
    
    return 0;
    
}

    
