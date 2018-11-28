#include <iostream>

using namespace std;


int N;

int maximo=-1;

unsigned int car[1001];
char usado[1001];


// Truco : suma sin acarreo es xor ^

// SUMA LOS USADOS
unsigned int sumaXOR_bolsa1()
{
    int i,j,k;
    
    unsigned int res=0;
    
    for(i=0;i<N;i++)
    {
        if(usado[i]==1)
        {
            res=res^car[i];
        }   
    }
    return res;
}



// SUMA LOS NO USADOS
unsigned int sumaXOR_bolsa2()
{
    int i,j,k;
    
    unsigned int res=0;
    
    for(i=0;i<N;i++)
    {
        if(usado[i]==0)
        {
            res=res^car[i];
        }   
    }
    return res;
}



// SUMA LOS USADOS
int sumaNormalbolsa1()
{
    int i,j,k;
    
    int res=0;
    
    for(i=0;i<N;i++)
    {
        if(usado[i]==1)
        {
            res=res+car[i];
        }   
    }
    return res;
}



// SUMA LOS NO USADOS
int sumaNormalbolsa2()
{
    int i,j,k;
    
    int res=0;
    
    for(i=0;i<N;i++)
    {
        if(usado[i]==0)
        {
            res=res+car[i];
        }   
    }
    return res;
}




void genera_bolsa(int act,int tam,int ini)
{
    int i,j,k;

    // Bolsa generada
    if(act>tam)
    {
        unsigned int x=sumaXOR_bolsa1();
        unsigned int y=sumaXOR_bolsa2();
     
     
        //cout << "genero la bolsa de tam "<<tam<<" y con valores " << x << " && "<< y << endl;
        
        if(x==y)
        {
            int z=sumaNormalbolsa1();
            if(z>maximo)
            {
                maximo=z;
            }
            z=sumaNormalbolsa2();
            if(z>maximo)
            {
                maximo=z;
            }
            
        }
        return;
    }

    for(i=ini;i<N;i++)
    {
        if(usado[i]==0)
        {
            usado[i]=1;
            genera_bolsa(act+1,tam,i+1);
            usado[i]=0;
        }
    }

}


void resuelve()
{
        int i,j,k;
       maximo=-1;
       
       
       
       
       for(i=1;i<=(N/2);i++)
       {
            genera_bolsa(1,i,0);
       }
       if(N%2!=0)
       {
            genera_bolsa(1,(N/2)+1,0);
       }
       
       
       
}


int main()
{
    int i,j,k;
    int ntest;
    long long int res;
    cin >> ntest;
    
    
    for(i=0;i<ntest;i++)
    {
        cin >> N;
        for(j=0;j<N;j++)
        {
            cin >> car[j];
        }
        
        resuelve();
        
        res=maximo;
        
        cout << "Case #"<<(i+1)<<": ";
        if(res==-1)
        {
            cout << "NO"<< endl;
        }
        else
        {
            cout << res << endl;
        }
            
    }
    
    
    return 0;
}
