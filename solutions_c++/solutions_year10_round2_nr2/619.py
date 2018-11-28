#include <iostream>
#include <sstream>
#include <set>
#include <string>
#include <vector>

using namespace std;
int main()
{
    int casos,n,k,b,t,estanDentro;
    vector<int> posInicial, posFinal;
    vector<int> velocidades,minimos;
    cin>>casos;
    int buffer,resp;
    long long mayor=1<<30;
    
    for(int i=1; i<=casos; i++)
    {
            cin>>n>>k>>b>>t;
            estanDentro=0;
            posInicial=posFinal=velocidades=vector<int>();
            for(int j=0; j<n; j++) 
            {
                    cin>>buffer;
                    posInicial.push_back(buffer);
            }

            for(int j=0; j<n; j++)
            {
                    cin>>buffer;
                    velocidades.push_back(buffer);
            }

            for(int j=0; j<n; j++)
                    posFinal.push_back(posInicial[j]+velocidades[j]*t);
            //cout<<" llega minimos "<<endl;
            minimos=vector<int>(n);

            for(int j=0; j<n; j++)
            {
                    if(posFinal[j]>= b)
                    {
                             int aux2=j;                             
                             for(int k=0; k<n; k++) 
                                     if(posInicial[k]>= posInicial[aux2] && posFinal[k]<b)
                             minimos[aux2]++;
                    }
                    else minimos[j]=mayor;
            }
            //cout<<" llega sort "<<endl;
            sort(minimos.begin(),minimos.end());
            resp=0;

            bool si=true;
            for(int a=0; a<k;a++)
            {
                    if(minimos[a]>=mayor) 
                    si=false;
                    else 
                    resp+=minimos[a];
            }

            cout << "Case #"<<i<<": ";

            if(si) cout<<resp<<endl;
            else cout <<"IMPOSSIBLE"<<endl;
   }          
   
   
   return 0;
}
