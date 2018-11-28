#include <stdio.h>
#include <iostream>

using namespace std;

int absolute(int x)
{
    if(x<0)
        x=x*-1;
    return x;
    
}
int mayorSinSorpresa(int valor)
{
    if(valor<3)
    {
        if(valor==2)
            return 1;
        return valor;
    }
    
    int i,j;
    int masAlta=1;
    for(i=1;i<=valor;i++)
    {
        int tmp=valor-i;
        int vtmp=(int)(tmp/2);
        
        if(absolute(i-vtmp)<=1)
        {
            masAlta=i;
        }
        
        
    }
    return masAlta;
}
int mayorConSorpresa(int valor)
{


    if(valor<3)
    {
        if(valor==2)
            return 1;
        return valor;
    }
    
    int i,j;
    int masAlta=1;
    for(i=1;i<=valor;i++)
    {
        int tmp=valor-i;
        int vtmp=(int)(tmp/2);
        if(absolute(i-vtmp)<=2)
        {
            masAlta=i;
        }
        
        
    }
    return masAlta;
}

int main()
{
    int T,N,S,p;
    int puntuaciones[40];
    int res;
    cin >> T;
    
    int i,j,k;
    
    for (i=0;i<T;i++)
    {
    res=0;
        cin >> N;
        cin >> S;
        cin >> p;
        for (j=0;j<N;j++)
        {
            cin >> puntuaciones[j];
        }
        
        
        
        for (j=0;j<N;j++)
        {
            int m=mayorSinSorpresa(puntuaciones[j]);
            //cout <<"M vale " << m << endl;
            if(m>=p)
            {
                res++;
            }
            else if(S>0)
            {
                int m2=mayorConSorpresa(puntuaciones[j]);
                //cout <<"M2 vale " << m2 << endl;
                if(m2>=p)
                {
                    S--;
                    res++;
                }
            }
        }
        
        cout << "Case #"<< i+1<<": "<<res<< endl;
    }
    return 0;
}
