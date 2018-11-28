#include <iostream>

using namespace std;

int i,j,k;


int C,D,N;

char cadC[40][4];

char cadD[40][4];
char cadN[200];

char res[200];
int nres=0;


char COMBINACION;

int combinan(char a,char b)
{
    int i,j,k;
    
    for(i=0;i<C;i++)
    {
        if(cadC[i][0]==a && cadC[i][1]==b)
        {
            COMBINACION=cadC[i][2];
            return 1;
        }
        if(cadC[i][0]==b && cadC[i][1]==a)
        {
            COMBINACION=cadC[i][2];
            return 1;
        }
    }
    return 0;
}


int opuestos(char a,int tam)
{
        int i,j,k;
    
    for(j=0;j<tam;j++)
    {
        for(i=0;i<D;i++)
        {
            //cout <<" Comprueb opuesto " << a << " con " << res[j]<< " en "<< j << endl;
            if(cadD[i][0]==a && cadD[i][1]==res[j])
            {
                return 1;
            }
            if(cadD[i][0]==res[j] && cadD[i][1]==a)
            {
                return 1;
            }
        }
    }
    return 0;
}

void resuelve()
{
    int i,j,k;
    res[0]=cadN[0];
    nres=1;
    
    
    for(i=1;i<N;i++)
    {
        // Caso que combinan
        if(combinan(res[nres-1],cadN[i]))
        {
            //cout << "combinan " << res[nres-1] << " con " << cadN[i]<< " en " << nres-1<< endl;
            res[nres-1]=COMBINACION;
           
        }
        else if(opuestos(cadN[i],nres))
        {
            //cout << "opuestos " << cadN[i] <<" a  la altura de " << nres << endl;
            res[0]=0;
            nres=0;
        }
        else
        {
            //cout << "meto " << cadN[i]<<" en "<<nres << endl;
            res[nres]=cadN[i];
            nres++;
        }
    }
    res[nres]=0;
}


int main()
{
    int ntest;
    int i,j,k;
    
    cin >> ntest;
    
    for(i=0;i<ntest;i++)
    {
        cin >> C;
        for(j=0;j<C;j++)
        {
            cin >> cadC[j];
        }
        cin >> D;
        for(j=0;j<D;j++)
        {
            cin >> cadD[j];
        }
        cin >> N;
        cin >> cadN;
        resuelve();
        
        //Solucion
        cout << "Case #"<<(i+1)<<": [";
        if(nres>0)
        {
            for(j=0;j<nres-1;j++)
            {
                cout << res[j]<<", ";
            }
            cout << res[nres-1];
        }
        cout << "]"<<endl;
        
    }
    return 0;
}
