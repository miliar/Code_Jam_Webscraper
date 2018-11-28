#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <list>

using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("A.out");

list<int> bases;
list<int>::iterator it;
int T, X, K;


bool sumar(int numero, int base, int &total)
{
    if (numero > 0)
    {
        int aux = numero%base;
        total += aux*aux;
        sumar(numero/base, base, total);
    }
}

bool enBase(int numero, int base)
{
    int veces = base*base;
    int total;
    
    for (int i=0; i<veces; i++)
    {
        total = 0;
        sumar(numero, base, total);
        if (total == 1)
        {
            return true;
        }
        numero = total;
    }
    return false;
}

int main()
{
    string str;
    bool resuelto;
    int aux;
    //input
    getline(in,str);
    istringstream iss(str);
    iss>>T;
    
    for (int X = 1; X<=T; X++)
    {
        //initialization
        bases.clear();
        //input
        getline(in,str);
        istringstream iss(str);
        while (!iss.eof())
        {
            iss>>aux;
            bases.push_back(aux);
        }
        resuelto = false;
        
        //algorithm
        K = 2;
        while (true)
        {
            for (it=bases.begin(); it!=bases.end(); it++)
            {
                if (!enBase(K, *it))
                   break;
            }
            if (it==bases.end())
                break;
            K++;
        }
        out<<"Case #"<<X<<": "<<K<<endl;
    }
    return EXIT_SUCCESS;
}
