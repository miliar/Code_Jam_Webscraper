#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sstream>

using namespace std;

int T;
char cadena[70];
char solucion[70];
char men[70];
char tmp[70];
long long int simbolos[256];
unsigned long long int menor=0;
char dig[40] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

void fromDec(unsigned long long int n, unsigned long long int b, char *s) {
	char digitos[40] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	unsigned long long int p = 0;

	if (n == 0)
		s[p++] = '0';
	
	
	while (n != 0) {
		s[p] = digitos[n%b];
		n /= b;
		p++;
	}

	// invertir la cadena
	for (int i = 0; i < p/2; i++) {
		int t = s[i];
		s[i] = s[p-i-1];
		s[p-i-1] = t;
	}
	s[p] = '\0';
}

// convierte un número a decimal
int toDec(char *s, unsigned long long int b) {
	unsigned long long int res = 0;
	unsigned long long int p = 0;

	while (s[p] != '\0') {
		int digito;
		if (s[p] >= '0' && s[p] <= '9')
			digito = s[p] - '0';
		else
			digito = s[p] - 'A' + 10;

		res = res*b + digito;
		p++;
	}
	return res;
}


/*
void resuelve()
{
    int i,j;
    int numact=1;
    int x=0;
    cout <<cadena<< endl;
    int tam=strlen(cadena);
    for(i=0;i<256;i++)
    {
        simbolos[i]=-1;
    }
    int nzero=0;
    
    for(i=0;i<tam;i++)
    {
        if(simbolos[cadena[i]]==-1)
        {
            if(i>0 && nzero==0)
            {
                nzero=1;
                simbolos[cadena[i]]=0;

            }
            else
            {
                simbolos[cadena[i]]=numact;
                numact++;
            }
        }
        
        solucion[x]=dig[simbolos[cadena[i]]];
        x++;    
    }
    solucion[x]=0;
    
    
    int num=toDec(solucion,numact);
    cout << "el numero es "<< num << endl;
    fromDec(num,37,solucion);
    
    
}
*/

void resuelve()
{
    int i,j;
    unsigned long long int numact=1;
    unsigned long long int x=0;
    //cout <<cadena<< endl;
    unsigned long long int tam=strlen(cadena);
    for(i=0;i<256;i++)
    {
        simbolos[i]=-1;
    }
    unsigned long long int nzero=0;
    
    for(i=0;i<tam;i++)
    {
        if(simbolos[cadena[i]]==-1)
        {
            if(i>0 && nzero==0)
            {
                nzero=1;
                simbolos[cadena[i]]=0;

            }
            else
            {
                simbolos[cadena[i]]=numact;
                numact++;
            }
        }
        solucion[x]=dig[simbolos[cadena[i]]];
        x++;    
                
    }
    solucion[x]=0;
    menor=200000000;
    for(i=numact;i<=37;i++)
    {
        int num=toDec(solucion,i);
       // cout << "el numero es "<< num << " en base " << i << endl;
        if(num<menor)
        {
            fromDec(num,i,men);
            menor=num;
        }
        else
        {
            break;
        }
    }
    
    
    
}



int main()
{
    
    int i,j,k;
    int res;
    
    
    close (0); 
    open ("A.in", O_RDONLY);
    
    cin >> T;
    
    for(i=0;i<T;i++)
    {
        cin >> cadena;
        resuelve();
       /* for(j=0;j<strlen(cadena);j++)
        {
            cout << solucion[j]<< endl;
        }*/
        cout <<"Case #"<<i+1<<": "<<menor<<endl;
    }
    
    return 0;
}
