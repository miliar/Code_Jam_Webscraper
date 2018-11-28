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
    in.open("C-large.in",ios::in);
    out.open("ap.out",ios::out);
    int N,k,R,g[1000],i,j,next[1000],sum[1000],t,T,c;
    long long result;
    in >> T;
    for (t=1;t<=T;t++)
    {
        in>>R>>k>>N;
        for (i=0;i<N;i++) in>>g[i];
        for (i=0;i<N;i++)
        {
            sum[i]=g[i];
            for (j=0;(j+1<N)&&(sum[i]+g[(i+j+1)%N]<=k);j++)
            {
                sum[i]+=g[(i+j+1)%N];
            };
            next[i]=(i+j+1)%N;
             
        };
        result=0;
        c=0;
        for (i=0;i<R;i++)
        {
            result+=sum[c];
            c=next[c];
        };

        out<<"Case #"<<t<<": "<<result<<"\n";


    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
