#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <list>

using namespace std;

bool compararNumeros(unsigned int primero, unsigned int segundo){
    return ( primero*primero > segundo*segundo) ;
}


int main(int argc, char *argv[])
{
    ifstream infile;
    ofstream outfile;

    infile.open("entrada.in", ifstream::in);
    outfile.open("salida.out", ofstream::out);

    int cantidadInstancias;
    int cardinal;
    infile >> cantidadInstancias;

    for(int instancia=1;instancia<=cantidadInstancias;instancia++){
        infile >> cardinal;
        list<int> v1;
        list<int> v2;
        list<int>::iterator iterador1;
        list<int>::iterator iterador2;
        
        int temp;
        int numero1;
        int numero2;
        int escalar = 0;
        for(int i = 0; i<cardinal;i++){
            infile >> temp;
            v1.push_back(temp);
        }
        for(int i = 0; i<cardinal;i++){
            infile >> temp;
            v2.push_back(temp);
        }
        //ORDENO LOS ELEMENTOS EN ORDEN DECRECIENTE SIN IMPORTAR EL SIGNO
        v1.sort(compararNumeros);
        v2.sort(compararNumeros);

        while(v1.size()>0){
            iterador1=v1.begin();
            
            numero1 = *iterador1;
            if(numero1>=0){
                list<int>::iterator ultimo = NULL;
                //BUSCO EL PRIMER NEGATIVO O ULTIMO POSITIVO

                    bool encontre = false;
                    for(iterador2=v2.begin();iterador2!=v2.end();iterador2++){
                        numero2 = *iterador2;

                        if(numero2<0){
                            //LO ENCONTRE, HAGO LA CUENTA Y LO SUMO, ELIMINO AMBOS ELEMENTOS
                            escalar += numero1*numero2;
                            v1.erase(iterador1);
                            v2.erase(iterador2);
                            encontre= true;
                            break;
                        }else{
                            //es positivo, lo sumo por si es el ultimo

                            ultimo = iterador2;
                        }
                    }
                    //SI LLEGUE AL FINAL
                    if(!encontre){
                            escalar += numero1*(*ultimo);
                            v1.erase(iterador1);
                            v2.erase(ultimo);
                    }
            }else{
                //BUSCO EL PRIMER POSITIVO O ULTIMO NEGATIVO
                list<int>::iterator ultimo = NULL;
                
                    for(iterador2=v2.begin();iterador2!=v2.end();iterador2++){
                        numero2 = *iterador2;
                        if(numero2>0){
                            //LO ENCONTRE, HAGO LA CUENTA Y LO SUMO, ELIMINO AMBOS ELEMENTOS
                            escalar += numero1*numero2;
                            v1.erase(iterador1);
                            v2.erase(iterador2);
                            break;
                        }else{
                            //es positivo, lo sumo por si es el ultimo
                            ultimo = iterador2;
                        }
                    }
                    //SI LLEGUE AL FINAL
                    if(iterador2 == v2.end()){
                            escalar += numero1*(*ultimo);
                            v1.erase(iterador1);
                            v2.erase(ultimo);
                    }
            }
        }

        outfile << "Case #" << instancia << ": " << escalar << endl;

        //IMPRIMO V1
        
        for(iterador1=v1.begin();iterador1!=v1.end();iterador1++){
            cout << *iterador1<< endl;
        }

        //IMPRIMO V2
        for(iterador2=v2.begin();iterador2!=v2.end();iterador2++){
            cout << *iterador2<< endl;
        }
        

    }
    
    //system("PAUSE");
    infile.close();
    outfile.close();
    return EXIT_SUCCESS;
}
