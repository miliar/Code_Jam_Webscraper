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
    in.open("A-large(3).in",ios::in);
    out.open("ap.out",ios::out);
    int T,A[1000],B[1000],result,i,j,t,N;
    
    in >> T;
    for (t=1;t<=T;t++)
    {
        in>>N;
        for (i=0;i<N;i++) in>>A[i]>>B[i];
        result=0;
        for (i=0;i<N;i++) for (j=i+1;j<N;j++)
        if (((A[i]<A[j])&&(B[i]>B[j]))||((A[i]>A[j])&&(B[i]<B[j]))) result++;
        out<<"Case #"<<t<<": "<<result<<"\n";
        
    };

    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
