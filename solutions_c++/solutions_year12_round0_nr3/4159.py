#include<stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int esReciclado(int num1,int num2)
{
    int i,j;
    char cad[100],nuevacad[100];
    sprintf(cad,"%d",num2);
    
    for(i=1;i<strlen(cad);i++)
    {
        int pos=0;
        // Genero la nueva cadena
        for(j=i;j<strlen(cad);j++)
        {
            nuevacad[pos]=cad[j];
            pos++;
        }
        for(j=0;j<i;j++)
        {
            nuevacad[pos]=cad[j];
            pos++;    
        }
        nuevacad[pos]=0;
        // Convertimos a numero
        
        int numtmp=atoi(nuevacad);
        if(num1==numtmp)
        {
            return 1;
        }
        
        
    }
    
    return 0;
    
}

int main()
{
    int i,j,k;
    int n;
    int res;
    cin >> n;
    for(i=0;i<n;i++)
    {
        int A,B;
        cin >> A >> B;
        if(A>B)
        {
            int aux=A;
            A=B;
            B=aux;
        }
        res=0;
        for(j=A;j<B;j++)
        {
            for(k=j+1;k<=B;k++)
            {
                if(esReciclado(j,k))
                {
                    res+=1;
                }
            }
        }
        
        
        cout << "Case #"<<i+1<<": "<<res << endl;
    }
    return 0;
}
