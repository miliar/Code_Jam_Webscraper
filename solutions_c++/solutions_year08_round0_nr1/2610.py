#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void parse( char inFileName[], char outFileName[]){
   int testCases, cantEngines, cantQueries, i, j, e;
   string auxAdvance;
   ifstream inFile;
   ofstream outFile;
   inFile.open(inFileName, ifstream::in);
   outFile.open(outFileName, ofstream::out);
   inFile>>testCases;
      for(i=1; i<=testCases; i++){
        inFile>>cantEngines;
        getline(inFile, auxAdvance);//Avanzo la linea
        string engines[cantEngines];
        for(j=0; j<cantEngines; j++){
            getline(inFile, engines[j]);
            //outFile<<"Engine #"<<j<<": "<<engines[j]<<endl;
        }
        inFile>>cantQueries;
        getline(inFile, auxAdvance);//Avanzo la linea
        string queries[cantQueries];
        for(j=0; j<cantQueries; j++){
            getline(inFile, queries[j]);
            //outFile<<"Query #"<<j<<": "<<queries[j]<<endl;
        }

        // Tengo las engines y las queries cargadas en sus respectivos arrays
        int ini = 0;
        int cantPasos = 0;
        int maxPaso = 0;
        int nuevoEngine = 0;
        int cantCambios = 0;
        for(e=0;e<cantEngines;e++){
            while(ini<cantQueries && queries[ini] != engines[e]){
                ini++;
                cantPasos++;
            }
            if (maxPaso<cantPasos){
                maxPaso = cantPasos;
                nuevoEngine = e;
            }
            ini = ini - cantPasos; //vuelvo los pasos que avancé
            cantPasos = 0; //reinicio mi conteo de pasos
        }
        int engineActual = nuevoEngine;
        while(ini<cantQueries){
            for(e=0;e<cantEngines;e++){
                while(ini<cantQueries && queries[ini] != engines[e]){
                    ini++;
                    cantPasos++;
                }
                if (maxPaso<cantPasos){
                    maxPaso = cantPasos;
                    nuevoEngine = e;
                }
                ini = ini - cantPasos; //vuelvo los pasos que avancé
                cantPasos = 0; //reinicio mi conteo de pasos
            }
            //en nuevoEngine tengo el engine que me permite dar el paso mayor
            // y en maxPaso tengo el tamaño del paso
             if(nuevoEngine != engineActual){
                //outFile<<"Cambio "<<engines[engineActual]<<" por "<<engines[nuevoEngine]<<endl;
                cantCambios++;
                engineActual = nuevoEngine;
            }
            ini = ini+maxPaso;
            maxPaso = 0;
            cantPasos = 0;

        }
        if(i>1)outFile<<endl;
        outFile<<"Case #"<<i<<": "<<cantCambios;
      }
      inFile.close();
      outFile.close();
 }

int main()
{
parse("A-large.in", "A-large.out");

  return 0;
}
