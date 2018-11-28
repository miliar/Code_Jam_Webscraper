#include <iostream>
#include <fstream>
#include <stdlib>
using namespace std;

void swap(int &a, int &b)
{
    int temp=a;
    a=b;
    b=temp;
}

int main()
{
    ifstream in("A-small-attempt1.in");
    ofstream out("A.out");
    
    long x[800];
    long y[800];        
    int X;
    long Y;
    int T,n;
        
    long temp,aux;
    int i,j;
    
    
    in>>T;
    for (X=1; X<=T; X++)
    {
        Y=0;
        in>>n;
        for (i=0; i<n; i++)
            in>>x[i];
        for (i=0; i<n; i++)
            in>>y[i];
        for (i=0; i<n-1; i++)
        {
            aux=i;
            for (j=i+1; j<n; j++)
            {
                if (x[j]<x[aux])
                    aux=j;                
            }
            temp=x[aux];
            x[aux]=x[i];
            x[i]=temp;
        }

        for (i=0; i<n-1; i++)
        {
            aux=i;
            for (j=i+1; j<n; j++)
            {
                if (y[j]>y[aux])
                    aux=j;                
            }
            temp=y[aux];
            y[aux]=y[i];
            y[i]=temp;
        }
        for (i=0; i<n; i++)
        {
            Y=Y+(x[i]*y[i]);
        }
        out<<"Case #"<<X<<": "<<Y<<endl;
    }
    
	return 0;
}