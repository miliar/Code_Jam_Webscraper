#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define finname "B-large.in"
#define foutname "B-large.out"

using namespace std;

const short MINS_POR_HORA = 60;

struct tiempo { short horas, minutos;};

void Intercambiar(tiempo& t1, tiempo& t2)
{
    tiempo ttemp = t1;
    t1 = t2;
    t2 = ttemp;
}

short Mayor(tiempo t1, tiempo t2)
{
    if(t1.horas > t2.horas) return 1;
    if(t1.horas < t2.horas) return 2;
    else
    {
        if(t1.minutos > t2.minutos) return 1;
        if(t1.minutos < t2.minutos) return 2;
        return 0;
    }
}

int main()
{
    cout << "El programa dira cuantos trenes tiene que haber en A y en B" << endl;
    cout << "para ajustarse a los horarios." << endl << endl;
    ifstream fin(finname);
    ofstream fout(foutname);
    if(!fin)
    {
        cout << "No se pudo abrir el archivo con la entrada de datos." << endl;
        system("PAUSE");
        return 1;
    }
    short limite;
    fin >> limite;  
    for(short actual=1; actual<=limite; actual++)
    {
        short T, NA, NB;
        fin >> T;
        fin >> NA >> NB;
        // Los primero cuatro están ordenados por la salida y para mantener la correspondencia de cual salida es para cual llegada.
        // Los otros dos son para mantener la llegada ordenada
        vector<tiempo> tiempoAB_salida, tiempoAB_llegada, tiempoBA_salida, tiempoBA_llegada, tiempoAB_llegada_ordenada, tiempoBA_llegada_ordenada;
        string temp;
        getline(fin, temp);
        for(short i=0; i<NA; i++)
        {
            string temp;
            getline(fin, temp);
            tiempo ttemp_salida, ttemp_llegada;
            ttemp_salida.horas = atoi(temp.substr(0, 2).c_str());
            ttemp_salida.minutos = atoi(temp.substr(3, 2).c_str());
            ttemp_llegada.horas = atoi(temp.substr(6, 2).c_str());
            ttemp_llegada.minutos = atoi(temp.substr(9, 2).c_str());
            tiempoAB_salida.push_back(ttemp_salida);
            tiempoAB_llegada.push_back(ttemp_llegada);
            tiempoAB_llegada_ordenada.push_back(ttemp_llegada);
        }
        for(short i=0; i<NB; i++)
        {
            string temp;
            getline(fin, temp);
            tiempo ttemp_salida, ttemp_llegada;
            ttemp_salida.horas = atoi(temp.substr(0, 2).c_str());
            ttemp_salida.minutos = atoi(temp.substr(3, 2).c_str());
            ttemp_llegada.horas = atoi(temp.substr(6, 2).c_str());
            ttemp_llegada.minutos = atoi(temp.substr(9, 2).c_str());
            tiempoBA_salida.push_back(ttemp_salida);
            tiempoBA_llegada.push_back(ttemp_llegada);
            tiempoBA_llegada_ordenada.push_back(ttemp_llegada);
        }
        int trenesA=0, trenesB=0;
        if(NA == 0 && NB != 0)
        {
            trenesA = 0;
            trenesB = NB;
        }
        if(NA == 0 && NB == 0)
        {
            trenesA = trenesB = 0;
        }
        if(NA != 0 && NB == 0)
        {
            trenesA = NA;
            trenesB = NB;
        }
        else
        {
            // Hay qye ordenar los tiempos para que cuando se fije si un tiempo fue usado
            // (para ver si un tren esta disponible) que un horario posterior no use un tren de viaje temprano.
            // Si pasa esto luego si queremos usarlo para otro mas temprano, no va a haber disponibles.
            vector<bool> viajeAB_usado, viajeBA_usado;
            for(short i=0; i<NA; i++)
            {
                viajeAB_usado.push_back(false);
                for(short j=0; j<NA-1; j++)
                {
                    if(Mayor(tiempoAB_salida[j], tiempoAB_salida[j+1]) == 1)
                    {
                        Intercambiar(tiempoAB_salida[j], tiempoAB_salida[j+1]);
                        Intercambiar(tiempoAB_llegada[j], tiempoAB_llegada[j+1]);
                    }
                    if(Mayor(tiempoAB_llegada_ordenada[j], tiempoAB_llegada_ordenada[j+1]) == 1) Intercambiar(tiempoAB_llegada_ordenada[j], tiempoAB_llegada_ordenada[j+1]);
                }
            }
            for(short i=0; i<NB; i++)
            {
                viajeBA_usado.push_back(false);
                for(short j=0; j<NB-1; j++)
                {
                    if(Mayor(tiempoBA_salida[j], tiempoBA_salida[j+1]) == 1)
                    {
                        Intercambiar(tiempoBA_salida[j], tiempoBA_salida[j+1]);
                        Intercambiar(tiempoBA_llegada[j], tiempoBA_llegada[j+1]);
                    }
                    if(Mayor(tiempoBA_llegada_ordenada[j], tiempoBA_llegada_ordenada[j+1]) == 1) Intercambiar(tiempoBA_llegada_ordenada[j], tiempoBA_llegada_ordenada[j+1]);
                }
            }
            for(short i=0; i<NA; i++)
            {
                //cout << tiempoAB_salida[i].horas << ":" << tiempoAB_salida[i].minutos << " " << tiempoAB_llegada[i].horas << ":" << tiempoAB_llegada[i].minutos << endl;
                bool hay_tren = false, tren_usado = false;
                for(short j=0; j<NB; j++)
                {
                    tiempo ttemp = tiempoBA_llegada_ordenada[j];
                    ttemp.minutos += T;
                    if(ttemp.minutos >= MINS_POR_HORA)
                    {
                        ttemp.horas += 1;
                        ttemp.minutos -= MINS_POR_HORA;
                    }
                    short mayor = Mayor(ttemp, tiempoAB_salida[i]);
                    if(!tren_usado && !viajeBA_usado[j] && (mayor == 0 || mayor == 2)) /////// Ta entrando varias veces a usar varios trenes en vez de uno.
                    {
                        hay_tren = true;
                        viajeBA_usado[j] = true;
                        tren_usado = true;
                    }
                }
                if(!hay_tren) trenesA++;
            }
            for(short i=0; i<NB; i++)
            {
                //cout << tiempoBA_salida[i].horas << ":" << tiempoBA_salida[i].minutos << " " << tiempoBA_llegada[i].horas << ":" << tiempoBA_llegada[i].minutos << endl;
                bool hay_tren = false,  tren_usado = false;;
                for(short j=0; j<NA; j++)
                {
                    tiempo ttemp = tiempoAB_llegada_ordenada[j];
                    ttemp.minutos += T;
                    if(ttemp.minutos >= MINS_POR_HORA)
                    {
                        ttemp.horas += 1;
                        ttemp.minutos -= MINS_POR_HORA;
                    }
                    short mayor = Mayor(ttemp, tiempoBA_salida[i]);
                    if(!tren_usado && !viajeAB_usado[j] && (mayor == 0 || mayor == 2))
                    {
                        hay_tren = true;
                        viajeAB_usado[j] = true;
                        tren_usado = true;
                    }
                }
                if(!hay_tren) trenesB++;
            }
        }
        fout << "Case #" << actual << ": " << trenesA << " " << trenesB << endl;
        cout << "Case #" << actual << ": " << trenesA << " " << trenesB << endl;
    }
    fin.close();
    fout.close();
    cout << endl;
    system("PAUSE");
    return EXIT_SUCCESS;
}
