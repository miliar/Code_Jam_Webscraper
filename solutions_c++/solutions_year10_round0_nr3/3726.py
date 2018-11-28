#include <iostream>
#include <queue>
#include <fstream>
using namespace std;
int main(){
    int testCases;
    ifstream in("C-small-attempt0.in");
    ofstream out("resultados.out");
    in >> testCases;
        
    for(int cases = 0; cases<testCases ; ++cases )
    {
        int r , k ,n;
        in >> r >> k >> n;
        queue<int> cola;
        for(int num_groups = 0; num_groups < n; ++num_groups)
        {
            int g;
            in >> g;
            cola.push(g);        
        }
       int eurosTotal = 0;          
       for(int rides = 0; rides < r; ++rides ){
            int euros = 0;
            int capacidad = 0;
            int count = 0;
            while( (capacidad + cola.front()) <= k && count < n ){
                int group = cola.front();
                capacidad += group;
                euros = capacidad; 
                cola.pop();
                cola.push(group);
                count++;             
            }
            eurosTotal+= euros;
            
       }
       out << "Case #"<< cases+1 <<": " << eurosTotal << endl;
       
                
    }
    out.close();
    in.close(); 
    return 0;     
}
