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


//-----------------------------------------------------

int main()
{

    /**
     *Archivos de entrada y salida. Estos siempre son los mismos
    */
    ifstream entrada("A-large.in", ios::in);
    ofstream salida ("A-large.out", ios::out);
    //--------

    /**
     *------Declaracion de variables necesarias para el programa-------
    */
    queue<int> ColaBlue;
    queue<int> ColaOrange;
    vector<char> ColaColor;
    char color;
    int valor;
    int tiempo;
    int posicionBlue;
    int posicionOrange;
    //--------------------------------------------------

    /**
     *----- Siempre primero me dan el numero de casos N
    */
    int Casos;
    int cantidadDatos;
    entrada >> Casos;

    //Hasta aca anda todo bien.

    //-------------------------------------------------
    //Dentro de este for calculo cada caso
    for(int i = 0; i < Casos; i++){

        /**
         *----Para cada caso, primero tengo la cantidad de datos
        */
        entrada >> cantidadDatos;
        //La cantidad de datos de cada caso tambien la calcula bien

    //--------------------------------------------------

        /**
         *------ Luego seteo las condiciones inciales para cada caso. Inicializo las variables
        */
        ColaColor.clear();
        ColaColor.reserve(cantidadDatos);
        tiempo = 0;
        color = ' ';
        valor = 0;
        posicionBlue = 1;
        posicionOrange = 1;

    //--------------------------------------------------

        /**
         *------ Dentro de este for acomodo cada dato para ser procesado, por ejemplo, en arrays o en listas.
         *       En esta parte es donde paso los datos desde el archivo al programa.
        */
        for(int j = 0; j < cantidadDatos; j++){
            entrada >> color;
            entrada >> valor;
            ColaColor[j] = color;
            if(color == 'B')
                ColaBlue.push(valor);
            else if(color == 'O')
                ColaOrange.push(valor);
            else
                cout << "No es ni blue ni organge????" << endl;
        }
        //Hasta aca tengo 2 colas con los botones a los que tiene que ir cada robot, y un vector para saber el orden de los botones.

    //------------------------------------------------
        /**
         *------ Aca proceso los datos que saque del archivo en el paso anterior
        */
        char botonApretado;
        for(int j = 0; j < cantidadDatos; j++){
            botonApretado = false;
            while(!botonApretado){
                //Robot azul
                if(posicionBlue < ColaBlue.front())
                    posicionBlue++;
                else if(posicionBlue > ColaBlue.front())
                    posicionBlue--;
                else if(posicionBlue == ColaBlue.front()){
                    if(ColaColor[j] == 'B'){
                        botonApretado = true;
                        ColaBlue.pop();
                    }
                }
                else
                    cout << "El robot azul fallo" << endl;

                //Robot naranja.
                if(posicionOrange < ColaOrange.front())
                    posicionOrange++;
                else if(posicionOrange > ColaOrange.front())
                    posicionOrange--;
                else if(posicionOrange == ColaOrange.front()){
                    if(ColaColor[j] == 'O'){
                        botonApretado = true;
                        ColaOrange.pop();
                    }
                }
                else
                    cout << "El robot naranja fallo" << endl;
                tiempo++;
            }
        }
        salida << "Case #" << i+1 << ": " << tiempo << endl;


    //-------------------------------------------------
    }

    //La despedida
    cout << "Chau mundo" <<endl;
    return 0;
}
