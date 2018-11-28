#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

/**
 *Algunas funciones para el programa
*/
bool existeCombinacion(char combinations[36][3], char elemento1, char elemento2){
    for(int i = 0; i < 36; i++){
        //Si los elementos estan en alguna fila de la matriz de combinaciones
        if((combinations[i][0] == elemento1 && combinations[i][1] == elemento2) || (combinations[i][0] == elemento2 && combinations[i][1] == elemento1))
            return true;
    }
    return false;
}

char buscarCombinacion(char combinations[36][3], char elemento1, char elemento2){
    for(int i = 0; i < 36; i++){
        //Si los elementos estan en alguna fila de la matriz de combinaciones
        if((combinations[i][0] == elemento1 && combinations[i][1] == elemento2) || (combinations[i][0] == elemento2 && combinations[i][1] == elemento1)){
            char aux = combinations[i][2];
            return aux;
        }
    }
    return '9';
}

bool buscarOpuesto(char opuestos[28][2], string resultado){
    for(int i = 0; i < 28; i++){
        if(resultado.find(opuestos[i][0]) != string::npos && resultado.find(opuestos[i][1]) != string::npos){
            return true;
        }
    }
    return false;
}

string setString(string resultado){
    if(resultado.empty())
        return "[]";
    string retorno;
    retorno.clear();
    retorno.push_back('[');
    retorno.push_back(resultado.at(0));
    for(int i = 1; i < resultado.size(); i++){
        retorno.append(", ");
        retorno.push_back(resultado.at(i));
    }
    retorno.push_back(']');
    return retorno;
}

//-----------------------------------------------------

int main()
{

    /**
     *Archivos de entrada y salida. Estos siempre son los mismos
    */
    ifstream entrada("B-large.in", ios::in);
    ofstream salida ("B-large.out", ios::out);
    //--------

    /**
     *------Declaracion de variables necesarias para el programa-------
    */
    char combinaciones[36][3];
    char opuestos[28][2];

    string combinacion;
    string opuesto;
    string formula;
    string resultado;

    int cantidadCombinaciones;
    int cantidadOpuestos;
    int largoFormula;

    //--------------------------------------------------

    /**
     *----- Siempre primero me dan el numero de casos N
    */
    int Casos;
    entrada >> Casos;
    //Hasta aca anda todo bien.

    //-------------------------------------------------
    //Dentro de este for calculo cada caso
    for(int i = 0; i < Casos; i++){

        /**
         *------ Luego seteo las condiciones inciales para cada caso. Inicializo las variables
        */
        for(int indiceCombinaciones = 0; indiceCombinaciones < 36; indiceCombinaciones++){
            combinaciones[indiceCombinaciones][0] = '0';
            combinaciones[indiceCombinaciones][1] = '0';
            combinaciones[indiceCombinaciones][2] = '0';
        }
        for(int indiceOpuestos = 0; indiceOpuestos < 28; indiceOpuestos++){
            opuestos[indiceOpuestos][0] = '0';
            opuestos[indiceOpuestos][1] = '0';
        }
        combinacion.clear();
        opuesto.clear();
        formula.clear();
        resultado.clear();
        cantidadCombinaciones = 0;
        cantidadOpuestos = 0;
        largoFormula = 0;

    //--------------------------------------------------

        entrada >> cantidadCombinaciones;
        for(int indiceCombinaciones = 0; indiceCombinaciones < cantidadCombinaciones; indiceCombinaciones++){
            entrada >> combinacion;
            combinaciones[indiceCombinaciones][0] = combinacion.at(0);   //Revisar si funciona
            combinaciones[indiceCombinaciones][1] = combinacion.at(1);
            combinaciones[indiceCombinaciones][2] = combinacion.at(2);
        }
        entrada >> cantidadOpuestos;
        for(int indiceOpuestos = 0; indiceOpuestos < cantidadOpuestos; indiceOpuestos++){
            entrada >> opuesto;
            opuestos[indiceOpuestos][0] = opuesto.at(0);
            opuestos[indiceOpuestos][1] = opuesto.at(1);
        }
        //Hasta aca tengo armados los vectores de combinaciones y de opuestos
        entrada >> largoFormula;
        entrada >> formula;
        if(formula.size() == 1)
            salida << "Case #" << i+1 << ": " << '[' << formula << ']' << endl;
        else{
            bool agregarUltimo = true;
            for(int indiceFormula = 0; indiceFormula < formula.size()-1; indiceFormula++){
                char elemento1 = formula.at(indiceFormula);
                char elemento2 = formula.at(indiceFormula + 1);

                resultado.push_back(formula.at(indiceFormula)); //Agrego el elemento y me fijo si elimina

                if(buscarOpuesto(opuestos,resultado)){
                    resultado.clear();
                }

                else if(existeCombinacion(combinaciones, elemento1, elemento2)){    //Implementar esta funcion!!!!!!!
                    resultado.erase(resultado.size()-1, 1); //Borro el ultimo elemento porque existe una combinacion
                    resultado.push_back(buscarCombinacion(combinaciones, elemento1, elemento2));   //implementar esta tambien
                    if(indiceFormula == formula.size()-2)
                        agregarUltimo = false;
                    indiceFormula++;
                }

                if(buscarOpuesto(opuestos, resultado))   //implementar esta tambien
                    resultado.clear();

                elemento1 = '-';
                elemento2 = '-';
            }

            if(agregarUltimo){
                resultado.push_back(formula.at(formula.size()-1));
                if(buscarOpuesto(opuestos, resultado))
                    resultado.clear();
            }
            salida << "Case #" << i+1 << ": " << setString(resultado) << endl;
        }

    }

    //La despedida
    cout << "Chau mundo" <<endl;
    return 0;
}


