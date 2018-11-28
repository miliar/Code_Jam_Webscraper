#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sstream>
#include<algorithm>

using namespace std;

int N;
int P,Q;

int vP[10000];
int vQ[100];


unsigned long long int calculaSoborno(int posQ)
{
    int i,j;
    unsigned long long int sob=0;
    if(posQ>0)
    {
        for(i=posQ-1;i>=0;i--)
        {
            if(vP[i]==1)
                sob++;
            else
                break;
        }
    }
    if(posQ<P-1)
    {
        
        for(i=posQ+1;i<P;i++)
        {
            if(vP[i]==1)
                sob++;
            else
                break;
        }
    }
    return sob;
}

unsigned long long int resuelve()
{
    int i,j,k;
    unsigned long long int soborno=0;
    unsigned long long int menor=0;
    int primero=0;
    do{
        
        for(j=0;j<P;j++)
        {
            vP[j]=1;
        }
        soborno=0;
        //cout << "Permu" << endl;
        for(i=0;i<Q;i++)
        {
            //cout << vQ[i]<<endl;
            vP[vQ[i]-1]=0;
            soborno=soborno+calculaSoborno(vQ[i]-1);
        }
        //cout << "res: "<< soborno<<endl;
        if(primero==0)
        {
            menor=soborno;
            primero=1;
        }
        if(menor>soborno)
        {
            menor=soborno;
        }
    }while ( next_permutation(vQ,vQ+Q ) );
    
    return menor;
}

int main()
{
    
    int i,j,k;
    int res;
    
    close (0); 
    open ("C.in", O_RDONLY);
    
    cin >> N;
    
    for(i=0;i<N;i++)
    {
        cin >> P;
        cin >> Q;
        for(j=0;j<Q;j++)
        {
            cin >> vQ[j];
        }
        unsigned long long int solucion=resuelve();
        
        cout <<"Case #"<<i+1<<": "<<solucion<<endl;
        
    }
    return 0;
}
