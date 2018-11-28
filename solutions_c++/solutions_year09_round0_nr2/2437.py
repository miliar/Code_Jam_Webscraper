#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

using namespace std;

char palabra[600];
int T,H,W;
int mapa[101][101];
int letra[101][101];
char colorin[101][101];


/* Hacia donde va

1 norte
2 oeste
3 este
4 sur
5 Estanque

*/

int iniciaMapa()
{
    int i,j;
    for(i=0;i<101;i++)
    {
        for(j=0;j<101;j++)
        {
            letra[i][j]=0;
            colorin[i][j]=0;
        }
    }
}

void imprimeColorin()
{
    int j,k;
 cout << "Colorin"<< endl;
    for(j=0;j<H;j++)
        {
            for(k=0;k<W-1;k++)
            {
                cout << colorin[j][k]<< " ";
            }   
            cout << colorin[j][k]<<endl;
        }
}

void colorear(int i, int j, char l)
{
    colorin[i][j]=l;
    //if(letra[i][j]==5)
   // {
        // Norte
        if(i>0 && letra[i-1][j]==4 && colorin[i-1][j]==0)
        {
            colorear(i-1,j,l);
        }

        // Sur
        if(i<H-1 && letra[i+1][j]==1 && colorin[i+1][j]==0)
        {
            colorear(i+1,j,l);
        }
        // Oeste
        if(j>0 && letra[i][j-1]==3 && colorin[i][j-1]==0)
        {
            colorear(i,j-1,l);
        }

        // Este
        if(j<W-1 && letra[i][j+1]==2 && colorin[i][j+1]==0)
        {
            colorear(i,j+1,l);
        }
    //}
    
    if(letra[i][j]==1 && colorin[i-1][j]==0)
    {
        colorear(i-1,j,l);
    }
    if(letra[i][j]==2 && colorin[i][j-1]==0)
    {
        colorear(i,j-1,l);
    }
    if(letra[i][j]==3 && colorin[i][j+1]==0)
    {
        colorear(i,j+1,l);
    }
    if(letra[i][j]==4 && colorin[i+1][j]==0)
    {
        colorear(i+1,j,l);
    }
}

void pintar(int alto, int ancho)
{
    int i,j;
    i=alto;
    j=ancho;
    int menor=1000000;
    
    // Norte
    if(i>0)
    {
        if(mapa[i-1][j]<mapa[i][j] && mapa[i-1][j]<menor )
        {
            menor=mapa[i-1][j];
        }
    }
    // Oeste
    if(j>0)
    {
        if(mapa[i][j-1]<mapa[i][j] && mapa[i][j-1]<menor)
        {
            menor=mapa[i][j-1];
        }
    }
    
    // ESTE
    if(j<W-1)
    {
        
        if(mapa[i][j+1]<mapa[i][j] && mapa[i][j+1]<menor)
        {
            menor=mapa[i][j+1];
        }
    }
    // SUR
    if(i<H-1)
    {
        if(mapa[i+1][j]<mapa[i][j] && mapa[i+1][j]<menor)
        {
            menor=mapa[i+1][j];
        }
    }
    
    // Comprobar en orden Norte, Oeste, Este, Sur
    
    
    if(i>0 && mapa[i-1][j]==menor && mapa[i][j]>menor)
    {
        
        letra[i][j]=1;
        //cout << "paso de "<< i << " " << j << " a " <<i-1<<" " <<j <<endl;
        pintar(i-1,j);
        return;
    }
    
    if(j>0 && mapa[i][j-1]==menor && mapa[i][j]>menor)
    {
        letra[i][j]=2;
        //cout << "paso de "<< i << " " << j << " a " <<i<<" " <<j-1 <<endl;
        pintar(i,j-1);
        return;
    }
    if(j<W && mapa[i][j+1]==menor && mapa[i][j]>menor)
    {
        
        letra[i][j]=3;
        //cout << "paso de " <<i << " " << j << " a " <<i<<" " <<j+1 <<endl;
        pintar(i,j+1);
        return;
    }
    
    if(i<H && mapa[i+1][j]==menor && mapa[i][j]>menor)
    {
        
        letra[i][j]=4;
        //cout << "paso de "<< i << " " << j << " a " <<i+1<<" " <<j <<endl;
        pintar(i+1,j);
        return;
    }
    
    // Caso de estanque y no ha pasado antes alguien por el
    if(letra[i][j]==0)
        letra[i][j]=5;
}

int main()
{
    
    int i,j,k;
    int res;
    
    
    close (0); 
    open ("B.in", O_RDONLY);
    
    
    cin >> T;
    
    for(i=0;i<T;i++)
    {
        char ultLetra='a';
        iniciaMapa();
        cin >> H;
        cin >> W;
        
        for(j=0;j<H;j++)
        {
            for(k=0;k<W;k++)
            {
                cin >> mapa[j][k];
            }   
        }               

        
        //Aqui se comienza a pintar
        
        for(j=0;j<H;j++)
        {
            for(k=0;k<W;k++)
            {
                if(letra[j][k]==0)
                {
                    pintar(j,k);
                }
                
            }
        }
        
        //Aqui se comienza a COLOREAR
        
        for(j=0;j<H;j++)
        {
            for(k=0;k<W;k++)
            {
                if(colorin[j][k]==0)
                {
                    colorear(j,k,ultLetra);
                    ultLetra++;

                }
            }
        }
        cout << "Case #"<<i+1<<":"<<endl;
       /*
        for(j=0;j<H;j++)
        {
            for(k=0;k<W-1;k++)
            {
                cout << letra[j][k]<< " ";
            }   
            cout << letra[j][k]<<endl;
        }*/
        
   /*
        for(j=0;j<H;j++)
        {
            for(k=0;k<W-1;k++)
            {
                cout << mapa[j][k]<< " ";
            }   
            cout << mapa[j][k]<<endl;
        }
        
     */        
        for(j=0;j<H;j++)
        {
            for(k=0;k<W-1;k++)
            {
                cout << colorin[j][k]<< " ";
            }   
            cout << colorin[j][k]<<endl;
        }
        
        
    }
    
    
    return 0;
}
