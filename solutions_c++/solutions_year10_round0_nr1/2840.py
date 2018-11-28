#include <sys/types.h> 
#include <sys/stat.h> 
#include <fcntl.h> 
#include <stdio.h> 
#include <math.h> 
#include <string.h>
#include <stdlib.h> 
#include <iostream>
using namespace std;

long long int T,N,k;


long long int res[31]= {1 , 3 , 7 , 15 , 31 , 63 , 127 , 255 , 511 , 1023 , 2047 , 4095 , 8191 , 16383 , 32767 , 65535 , 131071 , 262143 , 524287 , 1048575 , 2097151 , 4194303 , 8388607 , 16777215 , 33554431 , 67108863 , 134217727 , 268435455 , 536870911 , 1073741823 };


long long conexiones[31];
long long marcadas[31];


int estaConectadas(int n)
{
    for(int i=0;i<n;i++)
    {
        if(conexiones[i]==0)
            return 0;
    }
    return 1;
}

long long int simular( int num)
{
    int i;
    long long int pos=1;
    for(i=0;i<num;i++)
    {
        conexiones[i]=0;
    }
    
    while(1)
    {
        
        for(i=0;i<num;i++)
        {
           marcadas[i]=0;
        }
        
        marcadas[0]=1;
        for(i=0;i<num;i++)
        {
            if(conexiones[i]==1)
            {
                marcadas[i+1]=1;
            }
            else
            {
                break;
            }
        }
        
        for(i=0;i<num;i++)
        {
            if(marcadas[i]==1)
            {
                if(conexiones[i]==0)
                {
                    conexiones[i]=1;
                }
                else
                {
                    conexiones[i]=0;
                }
            }
        }
        
        //cambio
    
        if(estaConectadas(num))
        {
            return pos;
        }
        pos++;
    }
}

int main()
{
    
    
    
    
    long long int i,j,x;
    
    
        close (0); open ("a.in", O_RDONLY); 
        close (1); open ("a.out", O_WRONLY | O_CREAT, 0600); 

    /*
    cout << "long long int res[31]= {";
    for(i=1;i<31;i++)
    {
        res[i]=simular(i);
        cout << res[i] << " , ";
    }
    cout << "};"<< endl;
    */
        cin >> T;
    for(i=0;i<T;i++)
    {
        cin >> N;
        cin >> k;
        
        //cout << "K : " <<k << " res [N-1] " << res[N-1] << " N " << N << endl;

        k=k-res[N-1];
        
        /* Alternativo al While
        if(k>0)
        {
            k=k%(res[N-1]+1);
        }
        */
        while(k>0)
        {
            k=k-(res[N-1]+1);
        }
        if(k==0 )
           cout << "Case #"<<(i+1)<<": ON" << endl;
        else
           cout << "Case #"<<(i+1)<<": OFF" << endl;
    }
    
    
}

/*

L 0 0 0 0 0 B
L 1 0 0 0 0 B
L 0 1 0 0 0 B
L 1 1 0 0 0 B
L 0 0 1 0 0 B
L 1 0 1 0 0 B
L 0 1 1 0 0 B
L 1 1 1 0 0 B
L 0 0 0 1 0 B
L 1 0 0 1 0 B
L 0 1 0 1 0 B
L 1 1 0 1 0 B
L 0 0 1 1 0 B
L 1 0 1 1 0 B
L 0 1 1 1 0 B
L 1 1 1 1 0 B



L 1 0 0 0 0 B
L 0 1 0 0 0 B
L 1 1 0 0 0 B
L 0 0 1 0 0 B
L 1 0 1 0 0 B
L 0 1 1 0 0 B
L 1 1 1 0 0 B
L 0 0 0 0 0 B



*/
