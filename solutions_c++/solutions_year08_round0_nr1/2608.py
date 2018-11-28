#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    vector<string> servers;
    vector<string> querys;
    
    string aux;
    
    int testCases, nServers, nQuerys;
    int i,j,k;
    int mejor,reps,contador,swaps, salir, quiebre, indice,contMejor, primero;
    int cases = 0;
    
    ifstream fcin("A-large.in");
    ofstream fcout("A-large.out");
    
    fcin >> testCases;
    cout << testCases << endl;
    
    for(i= 0; i < testCases; i++)
    {
        
        fcin >> nServers;
        cout << "nServers = " << nServers << endl;
        getline(fcin, aux);
        for(j = 0; j < nServers; j++)
        {
            getline(fcin, aux);
            servers.push_back(aux);
            cout << "server[" << j << "]" << servers[j] << endl;
        }
        fcin >> nQuerys;
        getline(fcin, aux);
        for(k = 0; k < nQuerys; k++)
        {
            getline(fcin, aux);
            querys.push_back(aux);
            cout << querys[k] << endl;
        }
        
        mejor = 0;
        swaps = 0;
        salir = 0;
        contador = 0;
        quiebre = 0;
        contMejor = 0;
        primero = 1;
        indice = 0;
        while(salir != 1)
        {
            quiebre = -1;
            contMejor = 0;
            for(j = 0; j < nServers; j++)
            { 
                contador = indice;
                while(contador < nQuerys && servers[j] != querys[contador])
                {
                    contador++;
                }
                if(contador > contMejor)
                {
                    quiebre = contador;
                    contMejor = contador;
                    mejor = j;
                }
                cout << "mejor " << mejor << endl;
                cout << "quiebre " << quiebre << endl;
            }
            if(quiebre == nQuerys) 
            {   
                if(!primero)
                    swaps++;
                
                salir = 1; 
            }
            
            if(quiebre == -1) salir = 1;
            
            if(quiebre < nQuerys)
            {
                if(primero) primero = 0;
                else swaps++;
            }
            indice = quiebre;
            mejor = 0;
        }
        cout << "swaps " << swaps<<endl;
        querys.clear();
        servers.clear();
        fcout << "Case #" << i + 1 << ":" << " " << swaps << endl;
        
    }
    
    
    
    system("pause");
}
