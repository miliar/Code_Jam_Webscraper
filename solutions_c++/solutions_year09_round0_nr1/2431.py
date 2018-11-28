#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

using namespace std;

int L,D,N;
char diccionario[5000][17];
char palabra[1000];

int estaLetra(char letra,int pos)
{
    int pospalabra=0;
    int p=0;
    
    
    while(pos>p)
    {
        if(palabra[pospalabra]=='(')
        {
            while(palabra[pospalabra]!=')')
            {
                pospalabra++;
            }
        }
        pospalabra++;
        p++;
    }
    //interpreto letra
    if(palabra[pospalabra]!='(')
    {
        if(letra==palabra[pospalabra])
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        pospalabra++;
        while(palabra[pospalabra]!=')')
        {
            if(letra==palabra[pospalabra])
            {
                return 1;
            }
            pospalabra++;
        }
        return 0;
    }

}

int calcularResultado()
{
    int i,j;
    int resultado=0;
    
    // Cogemos palabra del diccionario y miramos si vale
    
    for(i=0;i<D;i++)
    {
        int encontrado=1;
        for(j=0;j<L && encontrado==1;j++)
        {
            
            if(!estaLetra(diccionario[i][j],j))
                encontrado=0;
        }
        if(encontrado==1)
        {
            resultado++;
            //cout << "Encuentro " << palabra << " en " << diccionario[i]<<endl;
        }
    }
    
    return resultado;
}

int main()
{
    
    int i,j,k;
    int res;
    
    close (0); 
    open ("A.in", O_RDONLY);
    
    
    cin >> L;
    cin >> D;
    cin >> N;
    
    for(int i=0;i<D;i++)
    {
        cin >> diccionario[i];
        //cout << diccionario[i]<<endl;
    }
    
    for(i=1;i<=N;i++)
    {
        cin >> palabra;       
        //cout << palabra<<endl; 
        res=calcularResultado();
        cout << "Case #"<<i<<": "<< res<<endl;
    }
    
    return 0;
}
