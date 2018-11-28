#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

using namespace std;
int N;

int formaN[10];
int formaX[10];

void formaNum(long long int num)
{
    char cadena[30];
    for(int i=0;i<=9;i++)
        formaN[i]=0;

    sprintf(cadena,"%lld",num);
    
    for(int i=0;i<strlen(cadena);i++)
    {
        formaN[cadena[i]-'0']++;
    }
}

void formaXNum(long long int num)
{
    char cadena[30];
    for(int i=0;i<=9;i++)
        formaX[i]=0;

    sprintf(cadena,"%lld",num);
    
    for(int i=0;i<strlen(cadena);i++)
    {
        formaX[cadena[i]-'0']++;
    }
}

int misma_forma()
{
    for(int i=1;i<=9;i++)
    {
        if(formaN[i]!=formaX[i])
            return 0;
    }
    return 1;
}

long long int calculaNum(long long int num)
{
    long long int x=num;
    //long long int z=100000000000000000000;
    long long int z=1000000000;
    formaNum(num);
    
    for(x=num+1;x<=z;x++)
    {
        formaXNum(x);
        
        if(misma_forma())
        {
            return x;
        }
    }
    return num;
}


int main()
{
    
    int i,j,k;
    long long int num;
    long long int res;
    
    close (0); 
    open ("B.in", O_RDONLY);
    
    cin >> N;
    
    for(i=0;i<N;i++)
    {
        cin >> num;
        res=calculaNum(num);
        cout <<"Case #"<< i+1<<": "<<res<< endl;
    }    
    
    return 0;
}
