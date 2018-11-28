#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int t,n,k,r;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
            cin>>r>>k>>n;
            int cola[n];
            int estoy=0;
            int resp=0;
            //leo el input
            for(int j=0; j<n; j++)
            cin>>cola[j];
            //simulo
            int contador; //gente q está entrando
            int inicio; //pos en el q se inicia a meter gent
            for(int j=0; j<r; j++)
            {
                    inicio=estoy;
                    contador=0;
                    while(1)
                    {
                              contador+=(cola[estoy++]);
                              estoy%=n;
                              if((contador+cola[estoy])>k) break;
                              if(inicio==estoy) break;
                    }
                    //cout<<"gent "<<contador<<endl;
                    resp+=contador;
            }
            cout<<"Case #"<<i<<": "<<resp<<endl; 
            
    }
 
    return 0;    
}
