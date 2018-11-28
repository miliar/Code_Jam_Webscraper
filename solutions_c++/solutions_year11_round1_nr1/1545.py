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
bool esEntero(float number){
    int aux = (int)number;
    if(aux - number == 0)
        return true;
    else
        return false;
}

//-----------------------------------------------------

int main()
{

    /**
     *Archivos de entrada y salida. Estos siempre son los mismos
    */
    ifstream entrada("A-small.in", ios::in);
    ofstream salida ("A-small.out", ios::out);
    //--------

    /**
     *------Declaracion de variables necesarias para el programa-------
    */

    //--------------------------------------------------

    /**
     *----- Siempre primero me dan el numero de casos N
    */
    int Casos;
    int N;
    int Pd;
    int Pg;
    bool posible;
    entrada >> Casos;
    //Hasta aca anda todo bien.

    //-------------------------------------------------
    //Dentro de este for calculo cada caso
    for(int i = 0; i < Casos; i++){

        /**
         *----Para cada caso, primero tengo la cantidad de datos
        */
        entrada >> N >> Pd >> Pg;
        //La cantidad de datos de cada caso tambien la calcula bien

    //--------------------------------------------------

        /**
         *------ Luego seteo las condiciones inciales para cada caso. Inicializo las variables
        */

        posible = false;
    //--------------------------------------------------

        /**
         *------ Dentro de este for acomodo cada dato para ser procesado, por ejemplo, en arrays o en listas.
         *       En esta parte es donde paso los datos desde el archivo al programa.
        */

        for(int j = 1; j <= N && posible == false; j++){
            float valor = j*Pd/100.0;
            if(esEntero(valor)){
                posible = true;
            }
        }
        if(Pg == 100 && Pd < 100)
            posible = false;
        if(Pg == 0 && Pd > 0)
            posible = false;

        if(posible)
            salida << "Case #" << i+1 << ": Possible" << endl;
        else
            salida << "Case #" << i+1 << ": Broken" << endl;

    }

    //La despedida
    cout << "Chau mundo" <<endl;
    return 0;
}


