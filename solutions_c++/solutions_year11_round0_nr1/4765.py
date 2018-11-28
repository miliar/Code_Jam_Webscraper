//Setear librerias
#include <iostream>
#include <list>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

//Setear ambiente
#define tipo_datos string
#define tipo_carga 1 //0-> small, 1 -> large, 2-> test
#define tipo_rf 0 //tipo de retorno de read function: 0-> devuelve una lista, 1-> devuleve un vector
#define tomar_linea 0 //1->la read function levanta lineas enteras en forma de strings, 0->levanta datos separados por espacios
#define reservar 0 //numero de elementos de un vector que se reservan, si es 0 no se reserva nada.
#define test_rf 0 //test read function

//Setear atajos
#define db system("pause");

using namespace std;

#if tomar_linea
#define tipo_datos string
#endif

#if tipo_rf
#define tipo_cont vector
#else
#define tipo_cont list
#endif

#define func(arg) tipo_cont<tipo_datos> *leer_in(arg)
func(string);

class bot
{
    public:
        int pos, nm, req, cd;
        bot() {reset();};
        void cnm() {nm=0; req=0;};
        void snm(int a) {nm=a; req=abs(nm-pos)+1;};
        void reset() {pos=1; req=0; nm=0; cd=0;};
};

int main()
{
    tipo_cont<tipo_datos> *inputs;
    tipo_cont<tipo_datos>::iterator it;
    fstream arch;
    int ciclos, temp, ntemp, lk;
    bot tob[2];

    #if tipo_carga==2
    inputs=leer_in("test.txt");
    #elif tipo_carga
    inputs=leer_in("A-large.in");
    #else
    inputs=leer_in("A-small-attempt2.in");
    #endif

    #if test_rf
    for (it=inputs->begin(); it!=inputs->end(); it++)
        cout << *it << endl;
    db
    #endif

    it=inputs->begin();

    arch.open("outputs.txt", ios::out | ios::app);
    for(int i=0; i<atoi(inputs->front().c_str()); i++)
    {
        arch << "Case #" << i+1 << ": ";
        ciclos=0;
        lk=atoi((*(++it)).c_str());
        tob[0].reset();
        tob[1].reset();
        for(int j=0; j<lk; j++)
        {
            temp = (*++it=="O") ? 0 : 1;
            ntemp = (*it=="O") ? 1 : 0;
            tob[temp].snm(atoi((*++it).c_str()));
            if(tob[temp].req>tob[temp].cd)
            {
                ciclos+=tob[temp].req-tob[temp].cd;
                tob[ntemp].cd+=tob[temp].req-tob[temp].cd;
                tob[temp].cd=0;
            }
            else
            {
                ciclos++;
                tob[ntemp].cd++;
                tob[temp].cd=0;
            }
            tob[temp].pos=tob[temp].nm;
            tob[temp].cnm();
        }

        arch << ciclos;
        arch << endl;
    }
    arch.close();


    return 0;
}

func(string ruta)
{
    fstream arch;
    tipo_cont<tipo_datos> *res;
    res=new tipo_cont<tipo_datos>;
    tipo_datos temp;

    arch.open(ruta.c_str(), ios::in);
    if(arch.fail())
        return NULL;

    #if reservar > 0 && tipo_rf
    res->reserve(reservar);
    #endif

    while(!arch.eof())
    {
        #if tomar_linea
        getline(arch,temp);
        #else
        arch >> temp;
        #endif
        res->push_back(temp);
    }

    arch.close();

    return res;
}

