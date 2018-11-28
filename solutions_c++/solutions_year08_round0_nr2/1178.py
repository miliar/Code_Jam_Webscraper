#include <iostream>
#include <fstream>
using namespace std;

#define other(i) i == 0 ? 1 : 0

#define MAX_MINUTOS 1440
#define MAX_VIAJES  100


typedef struct {
    int salida;
    int llegada;
} viaje;

typedef struct {
    int cantViajes;
    viaje viajes[MAX_VIAJES];
    int disponibles[MAX_MINUTOS];
} estacion;


int cantCasos;
int turnaround;

estacion estaciones[2];


int comparar(const void* v1, const void* v2) {
    return ((viaje*) v1) -> salida - ((viaje*) v2) -> salida;
}

int parseHora(string hora) {
    return (hora[0] - '0') * 600 + (hora[1] - '0') * 60 +
            (hora[3] - '0') * 10 + (hora[4] - '0');
}

int main() {
    ifstream entrada("train.in");
    ofstream salida("train.out");
    
    entrada >> cantCasos;
    for(int c = 0; c < cantCasos; c++) {
        entrada >> turnaround;
        entrada >> estaciones[0].cantViajes >> estaciones[1].cantViajes;
        
        for(int e = 0; e < 2; e++) {
            for(int v = 0; v < estaciones[e].cantViajes; v++) {
                string hora;
                
                entrada >> hora;
                estaciones[e].viajes[v].salida = parseHora(hora);
                entrada >> hora;
                estaciones[e].viajes[v].llegada = parseHora(hora);
                
                int disponible = estaciones[e].viajes[v].llegada + turnaround;
                if(disponible < MAX_MINUTOS) {
                    estaciones[ other(e) ].disponibles[ disponible ] ++;
                }
            }
        }
        
        for(int e = 0; e < 2; e++) {
            for(int m = 1; m < MAX_MINUTOS; m++) {
                /*if(estaciones[e].disponibles[m] > 0)
                        cout << e << ", " << m << ": " << estaciones[e].disponibles[m] << endl;*/
                
                estaciones[e].disponibles[m] += estaciones[e].disponibles[m - 1];
            }
        }
        
        qsort(estaciones[0].viajes, estaciones[0].cantViajes, sizeof(viaje), comparar);
        qsort(estaciones[1].viajes, estaciones[1].cantViajes, sizeof(viaje), comparar);
        
        int trenesDesde[2] = { 0, 0 };
        
        for(int e = 0; e < 2; e++) {
            for(int v = 0; v < estaciones[e].cantViajes; v++) {
                if(estaciones[e].disponibles[ estaciones[e].viajes[v].salida ] <= v - trenesDesde[e]) {
                    trenesDesde[e]++;
                }
                
                //cout << estaciones[e].viajes[v].salida << " -> " << estaciones[e].viajes[v].llegada << endl;
            }
            //cout << endl;
        }
        
        cout << "Case #" << c + 1 << ": " << trenesDesde[0] << " " << trenesDesde[1] << endl;
        salida << "Case #" << c + 1 << ": " << trenesDesde[0] << " " << trenesDesde[1] << endl;
        
        //if(c == 5
        
        for(int i = 0; i < MAX_MINUTOS; i++) {
            estaciones[0].disponibles[i] = 0;
            estaciones[1].disponibles[i] = 0;
        }
    }
    
    entrada.close();
    
    
    salida.close();
    cin.get();
    return 0;
}
