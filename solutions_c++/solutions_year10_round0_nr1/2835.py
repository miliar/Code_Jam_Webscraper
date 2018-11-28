//Source code is in C++
#include<iostream>
#include<fstream.h>

//i have used the fact that a snapper basically acts like a modulo 2^N counter and can supply 
//power to the device only when all outputs are 1 i.e. only if
// K=(2^N)-1 + x*(2^N) where x is a whole no.

long power(int n)
{   
    long r=1;
    for(int i=0;i<n;i++)
    r=2*r;
    return (r);        
}

int main()
{   
    int *o;
    int *N;
    long *K,c,d;
    int T,i,j;
    ifstream fin;
    fin.open("inputfile.txt");
    fin>>T;
    N=new int[T];
    K=new long int[T];
    o=new int[T];
    for(i=0;i<T;i++)
    {       
            o[i]=0;
            fin>>N[i];
            fin>>K[i];
            c=power(N[i]);
            d=K[i]-c+1;
            if(d%c==0)
            o[i]=1;
    }
    fin.close();
    ofstream fout;
    fout.open("outfile.txt");
    
    for(j=0;j<T;j++)
    {               
          if(o[j]==0)
          fout<<"Case #"<<j+1<<": OFF\n";
          else
          fout<<"Case #"<<j+1<<": ON\n";
    }
    fout.close();
    delete []N;
    delete []K;
    delete []o;
    return (0);
}