#include <iostream>

using namespace std;

int ntest;


int nbut;
char colores[200];
int botones[200];
int azul,naranja;
int nar[200],az[200];


int resuelve()
{
    int contA=0,contN=0;
    int posA=1,posN=1;
    int pulsado=0;
    int i,j,k;
    int tiempo=0;
    for(i=0;i<nbut;tiempo++)
    {
        pulsado=0;
        // Cosas del naranja
        if(nar[contN]==posN && colores[i]=='O')
        {
            contN++;
            pulsado=1;
        }
        else if(nar[contN]>posN)
        {
            posN++;    
        }
        else if(nar[contN]<posN)
        {
            posN--;    
        }
        
        
        // Cosas del azul
        if(az[contA]==posA && colores[i]=='B')
        {
            contA++;
            pulsado=1;
        }
        else if(az[contA]>posA)
        {
            posA++;    
        }
        else if(az[contA]<posA)
        {
            posA--;    
        }
        
        if(pulsado==1)
        {
            i++;
        }
        
    }
    return tiempo;
}

int main()
{
    int i,j,k;
    int res;
    cin >> ntest;
    
    for(i=0;i<ntest;i++)
    {
        cin >> nbut;
        naranja=0;
        azul=0;
        for(j=0;j<nbut;j++)
        {
            cin >> colores[j];
            cin >> botones[j];
            if(colores[j]=='O')
            {
                nar[naranja]=botones[j];
                naranja++;
            }
            else
            {
                az[azul]=botones[j];
                azul++;
            
            }
        }
        res=resuelve();
        cout <<"Case #"<<(i+1)<<": "<<res<< endl;
        
    }
    return 0;
}
