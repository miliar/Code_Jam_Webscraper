#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

#define MAX_BUSCADORES 150

int cantCasos;
int cantBuscadores;
int cantBusquedas;

string busc[MAX_BUSCADORES];

map<string, bool> buscadores;

int main() {
    ifstream entrada("saving.in");
    ofstream salida("saving.out");
    
    entrada >> cantCasos;
    for(int c = 0; c < cantCasos; c++) {
        entrada >> cantBuscadores;
        
        char line[150];
        entrada.getline(line, 150);
        for(int b = 0; b < cantBuscadores; b++) {
            entrada.getline(line, 150);
            string s(line);
            
            busc[b] = s;
            buscadores[s] = true;
            
            cout << s << endl;
        }
        
        entrada >> cantBusquedas;
        
        cout << endl;
        
        int restantes = cantBuscadores;
        int switches = 0;
        
        entrada.getline(line, 150);
        for(int b = 0; b < cantBusquedas; b++) {
            entrada.getline(line, 150);
            string s(line);
            cout << s << endl;
            
            if(buscadores[s]) {
                buscadores[s] = false;
                restantes--;
            }
            
            if(restantes == 0) {
                switches++;
                for(int i = 0; i < cantBuscadores; i++) {
                    buscadores[ busc[i] ] = true;
                }
                restantes = cantBuscadores;
                
                buscadores[s] = false;
                restantes--;
            }
        }
        
        cout << endl << "Case #" << c + 1 << ": " << switches << endl << endl;
        salida << "Case #" << c + 1 << ": " << switches << endl;
    }
    
    entrada.close();
    
    salida.close();
    cin.get();
    
    return 0;
}
